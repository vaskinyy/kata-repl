import unittest

from repl import lexems
from repl.lexer import Token
from repl.parser import Parser


class Test_Parser(unittest.TestCase):
    def test_adding(self):
        parser = Parser()
        tree = parser.run("1 + 7")
        self.assertEqual(tree.op, Token(lexems.PLUS, lexems.PLUS))
        self.assertEqual(tree.left.val, Token(lexems.DIGIT, 1))
        self.assertEqual(tree.right.val, Token(lexems.DIGIT, 7))

    def test_multiply(self):
        parser = Parser()
        tree = parser.run("1 + 7 * 5")
        self.assertEqual(tree.op, Token(lexems.PLUS, lexems.PLUS))
        self.assertEqual(tree.left.val, Token(lexems.DIGIT, 1.0))

    def test_brackets(self):
        parser = Parser()
        tree = parser.run("(1 + 7) * 5")
        self.assertEqual(tree.op, Token(lexems.MULTIPLY, lexems.MULTIPLY))
        self.assertEqual(tree.right.val, Token(lexems.DIGIT, 5.0))

    def test_assignment(self):
        parser = Parser()
        tree = parser.run("x = 3")
        self.assertEqual(tree.op, Token(lexems.ASSIGNMENT, lexems.ASSIGNMENT))
        self.assertEqual(tree.right.val, Token(lexems.DIGIT, 3.0))
        self.assertEqual(tree.left.val, Token(lexems.LETTER, 'x'))

    def test_assignment_complex(self):
        parser = Parser()
        tree = parser.run("x = y = 3")
        self.assertEqual(tree.op, Token(lexems.ASSIGNMENT, lexems.ASSIGNMENT))
        self.assertEqual(tree.right.op, Token(lexems.ASSIGNMENT, lexems.ASSIGNMENT))
        self.assertEqual(tree.left.val, Token(lexems.LETTER, 'x'))

    def test_bad_fn_def(self):
        parser = Parser()
        tree = parser.run("fn avg => (x + y) / 2")
        self.assertEqual(Token(lexems.LETTER, "avg"), tree.name)

    def test_fn_def(self):
        parser = Parser()
        tree = parser.run("fn avg x y => (x + y) / 2")
        self.assertEqual(Token(lexems.LETTER, "avg"), tree.name)
        self.assertEqual([Token(lexems.LETTER, "x"), Token(lexems.LETTER, "y")], tree.arguments)
        self.assertEqual(Token(lexems.DIVIDE, lexems.DIVIDE), tree.definition.op)

    def test_fn_def_add(self):
        parser = Parser()
        tree = parser.run("fn add x y => x + z")
        self.assertEqual(Token(lexems.LETTER, "add"), tree.name)
        self.assertEqual([Token(lexems.LETTER, "x"), Token(lexems.LETTER, "y")], tree.arguments)
        self.assertEqual(Token(lexems.PLUS, lexems.PLUS), tree.definition.op)

    def test_fn_def_echo(self):
        parser = Parser()
        tree = parser.run("fn echo x => x")
        self.assertEqual(Token(lexems.LETTER, "echo"), tree.name)
        self.assertEqual([Token(lexems.LETTER, "x")],tree.arguments)
        self.assertEqual(Token(lexems.LETTER, "x"), tree.definition.val)

    def test_fn_def_call(self):
        parser = Parser()
        tree = parser.run("fn avg x y => (x + y) / 2")
        self.assertEqual(Token(lexems.LETTER, "avg"), tree.name)
        self.assertEqual([Token(lexems.LETTER, "x"), Token(lexems.LETTER, "y")], tree.arguments)
        self.assertEqual(Token(lexems.DIVIDE, lexems.DIVIDE), tree.definition.op)

        tree = parser.run("avg 1 2")
        self.assertEqual(Token(lexems.LETTER, "avg"), tree.name)
        self.assertEqual(Token(lexems.DIGIT, 1.0), tree.arguments[0].val)
        self.assertEqual(Token(lexems.DIGIT, 2.0), tree.arguments[1].val)

    def test_fn_def_add_call(self):
        parser = Parser()
        tree = parser.run("fn add x y => x + z")
        self.assertEqual(Token(lexems.LETTER, "add"), tree.name)
        self.assertEqual([Token(lexems.LETTER, "x"), Token(lexems.LETTER, "y")], tree.arguments)
        self.assertEqual(Token(lexems.PLUS, lexems.PLUS), tree.definition.op)

        tree = parser.run("add x+1 y")
        self.assertEqual(Token(lexems.LETTER, "add"), tree.name)
        self.assertEqual(Token(lexems.PLUS, lexems.PLUS), tree.arguments[0].op)
        self.assertEqual(Token(lexems.LETTER, "y"), tree.arguments[1].val)

    def test_fn_def_echo_call_no_def(self):
        parser = Parser()
        tree = parser.run("fn echo x => x")
        self.assertEqual(Token(lexems.LETTER, "echo"), tree.name)
        self.assertEqual([Token(lexems.LETTER, "x")],tree.arguments)
        self.assertEqual(Token(lexems.LETTER, "x"), tree.definition.val)

        with self.assertRaises(Exception) as context:
            tree = parser.run("echo1 11")

    def test_fn_def_echo_call_no_args(self):
        parser = Parser()
        tree = parser.run("fn echo => 2")
        self.assertEqual(Token(lexems.LETTER, "echo"), tree.name)
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

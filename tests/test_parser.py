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

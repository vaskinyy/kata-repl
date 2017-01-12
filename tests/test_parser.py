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

    def test_multipl(self):
        parser = Parser()
        tree = parser.run("1 + 7 * 5")
        print(tree)
        self.assertEqual(tree.op, Token(lexems.PLUS, lexems.PLUS))
        self.assertEqual(tree.left.val, Token(lexems.DIGIT, 1))
        self.assertEqual(tree.right.val, Token(lexems.DIGIT, 7))


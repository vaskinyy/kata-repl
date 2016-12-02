import unittest

from repl import lexems
from repl.lexer import Lexer, Token


class Test_Lexer(unittest.TestCase):
    def setUp(self):
        self.lexer = Lexer()

    def test_example_assignment(self):
        tokens = self.lexer.parse("x = 7")
        result = [Token(lexems.LETTER, 'x'),
                  Token(lexems.ASSIGNMENT, lexems.ASSIGNMENT),
                  Token(lexems.DIGIT, 7.0),
                  Token(lexems.EOF, lexems.EOF)]
        self.assertEqual(tokens, result)

    def test_example_operation(self):
        tokens = self.lexer.parse("x + 6")
        result = [Token(lexems.LETTER, 'x'),
                  Token(lexems.PLUS, lexems.PLUS),
                  Token(lexems.DIGIT, 6.0),
                  Token(lexems.EOF, lexems.EOF)]
        self.assertEqual(tokens, result)

    def test_example_assignment_chain(self):
        tokens = self.lexer.parse("x = y = 7")
        result = [Token(lexems.LETTER, 'x'),
                  Token(lexems.ASSIGNMENT, lexems.ASSIGNMENT),
                  Token(lexems.LETTER, 'y'),
                  Token(lexems.ASSIGNMENT, lexems.ASSIGNMENT),
                  Token(lexems.DIGIT, 7.0),
                  Token(lexems.EOF, lexems.EOF)]
        self.assertEqual(tokens, result)

    def test_example_assignment_chain_hard(self):
        tokens = self.lexer.parse("x = 13 + (y = 3)")
        result = [Token(lexems.LETTER, 'x'),
                  Token(lexems.ASSIGNMENT, lexems.ASSIGNMENT),
                  Token(lexems.DIGIT, 13.0),
                  Token(lexems.PLUS, lexems.PLUS),
                  Token(lexems.OPEN_BRACKET, lexems.OPEN_BRACKET),
                  Token(lexems.LETTER, 'y'),
                  Token(lexems.ASSIGNMENT, lexems.ASSIGNMENT),
                  Token(lexems.DIGIT, 3.0),
                  Token(lexems.CLOSE_BRACKET, lexems.CLOSE_BRACKET),
                  Token(lexems.EOF, lexems.EOF)]
        self.assertEqual(tokens, result)

    def test_example_fn_definition(self):
        tokens = self.lexer.parse("fn avg => (x + y) / 2")
        result = [Token(lexems.FN_KEYWORD, lexems.FN_KEYWORD),
                  Token(lexems.LETTER, "avg"),
                  Token(lexems.FN_OPERATOR, lexems.FN_OPERATOR),
                  Token(lexems.OPEN_BRACKET, lexems.OPEN_BRACKET),
                  Token(lexems.LETTER, 'x'),
                  Token(lexems.PLUS, lexems.PLUS),
                  Token(lexems.LETTER, 'y'),
                  Token(lexems.CLOSE_BRACKET, lexems.CLOSE_BRACKET),
                  Token(lexems.DIVIDE, lexems.DIVIDE),
                  Token(lexems.DIGIT, 2.0),
                  Token(lexems.EOF, lexems.EOF)]
        self.assertEqual(tokens, result)

    def test_example_fn_definition_error(self):
        tokens = self.lexer.parse("fn add x y => x + z")
        result = [Token(lexems.FN_KEYWORD, lexems.FN_KEYWORD),
                  Token(lexems.LETTER, "add"),
                  Token(lexems.LETTER, 'x'),
                  Token(lexems.LETTER, 'y'),
                  Token(lexems.FN_OPERATOR, lexems.FN_OPERATOR),
                  Token(lexems.LETTER, 'x'),
                  Token(lexems.PLUS, lexems.PLUS),
                  Token(lexems.LETTER, 'z'),
                  Token(lexems.EOF, lexems.EOF)]
        self.assertEqual(tokens, result)

    def test_example_fn_definition_echo(self):
        tokens = self.lexer.parse("fn echo x => x")
        result = [Token(lexems.FN_KEYWORD, lexems.FN_KEYWORD),
                  Token(lexems.LETTER, "echo"),
                  Token(lexems.LETTER, 'x'),
                  Token(lexems.FN_OPERATOR, lexems.FN_OPERATOR),
                  Token(lexems.LETTER, 'x'),
                  Token(lexems.EOF, lexems.EOF)]
        self.assertEqual(tokens, result)

    def test_example_fn_definition_add(self):
        tokens = self.lexer.parse("fn add x y => x+y")
        result = [Token(lexems.FN_KEYWORD, lexems.FN_KEYWORD),
                  Token(lexems.LETTER, "add"),
                  Token(lexems.LETTER, 'x'),
                  Token(lexems.LETTER, 'y'),
                  Token(lexems.FN_OPERATOR, lexems.FN_OPERATOR),
                  Token(lexems.LETTER, 'x'),
                  Token(lexems.PLUS, lexems.PLUS),
                  Token(lexems.LETTER, 'y'),
                  Token(lexems.EOF, lexems.EOF)]
        self.assertEqual(tokens, result)

    def test_example_fn_definition_inc(self):
        tokens = self.lexer.parse("fn inc x=>x+1")
        result = [Token(lexems.FN_KEYWORD, lexems.FN_KEYWORD),
                  Token(lexems.LETTER, "inc"),
                  Token(lexems.LETTER, 'x'),
                  Token(lexems.FN_OPERATOR, lexems.FN_OPERATOR),
                  Token(lexems.LETTER, 'x'),
                  Token(lexems.PLUS, lexems.PLUS),
                  Token(lexems.DIGIT, 1.0),
                  Token(lexems.EOF, lexems.EOF)]
        self.assertEqual(tokens, result)

    def test_example_fn_call_inc(self):
        tokens = self.lexer.parse("a = inc a")
        result = [Token(lexems.LETTER, "a"),
                  Token(lexems.ASSIGNMENT, lexems.ASSIGNMENT),
                  Token(lexems.LETTER, 'inc'),
                  Token(lexems.LETTER, 'a'),
                  Token(lexems.EOF, lexems.EOF)]
        self.assertEqual(tokens, result)

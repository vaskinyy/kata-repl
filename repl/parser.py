from repl.lexems import EOF, DIGIT, PLUS, MINUS
from repl.lexer import Lexer, Token


class Parser(object):
    def __init__(self):
        self.lexer = Lexer()
        self.tokens = []
        self.position = 0

    def run(self, line):
        self.clear()
        self.tokens = self.lexer.parse(line)
        return self.expr()

    def clear(self):
        self.tokens.clear()
        self.position = 0

    def current(self):
        return self.get_token(position=self.position)

    def lookup(self):
        return self.get_token(position=self.position + 1)

    def next(self):
        val = self.current()
        self.position += 1
        return val

    def get_token(self, position):
        if position >= len(self.tokens):
            return Token(EOF, '')
        return self.tokens[position]

    # expression::= factor | expression operator expression
    # factor::= number | identifier | assignment | '('expression')' | function - call
    #
    # operator::= '+' | '-' | '*' | '/' | '%'
    #
    # letter::= 'a' | 'b' | ... | 'y' | 'z' | 'A' | 'B' | ... | 'Y' | 'Z'
    # digit::= '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9'

    def expr(self):
        first = self.next()
        second = self.next()
        third = self.next()
        if first.type == DIGIT and second.type == MINUS and third.type == DIGIT:
            return first.value - third.value

        if first.type == DIGIT and second.type == PLUS and third.type == DIGIT:
            return first.value + third.value

        if first.type == DIGIT:
            return first.value

        return ""

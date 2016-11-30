from repl.lexer import Lexer, Token, EOF, DIGIT, PLUS, MINUS


class Interpreter(object):
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
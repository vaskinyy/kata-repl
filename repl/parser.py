from repl import lexems
from repl.lexer import Lexer, Token
from repl.op import LiteralNode, BinaryNode


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
            return Token(lexems.EOF, '')
        return self.tokens[position]

    # expression::= factor | expression operator expression
    # factor::= number | identifier | assignment | '('expression')' | function - call
    #
    # operator::= '+' | '-' | '*' | '/' | '%'
    #
    # letter::= 'a' | 'b' | ... | 'y' | 'z' | 'A' | 'B' | ... | 'Y' | 'Z'
    # digit::= '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9'

    def factor(self):
        token = self.current()
        if token.type == lexems.OPEN_BRACKET:
            self.next()
            res = self.expr()
            self.next()
            return res
        self.next()
        return LiteralNode(token)

    def term(self):
        node = self.factor()
        while self.current().type in [lexems.MULTIPLY, lexems.PERCENT, lexems.DIVIDE]:
            op_token = self.next()
            right = self.factor()
            node = BinaryNode(node, op_token, right)
        return node

    def expr(self):
        node = self.term()
        while self.current().type in [lexems.PLUS, lexems.MINUS]:
            op_token = self.next()
            right = self.term()
            node = BinaryNode(node, op_token, right)
        return node

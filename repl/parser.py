from repl.lexems import *
from repl.lexer import Lexer, Token
from repl.op import LiteralNode, BinaryNode, VariableDefinitionNode


class Parser(object):
    def __init__(self):
        self.lexer = Lexer()
        self.tokens = []
        self.position = 0

    def run(self, line):
        self.clear()
        self.tokens = self.lexer.parse(line)
        res = self.expr()
        if self.next() != Token(EOF, ""):
            raise(Exception("Error: Invalid input"))
        return res

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
            return Token(EOF, "")
        return self.tokens[position]

    def factor(self):
        token = self.next()

        node = LiteralNode(token)
        if token.type == MINUS and self.current().type == DIGIT:
            token = self.next()
            token.value = -token.value
            node = LiteralNode(token)
        elif token.type == LETTER and self.current().type == ASSIGNMENT:
            node = VariableDefinitionNode(token)
            op_token = self.next()
            right = self.expr()
            node = BinaryNode(node, op_token, right)
        elif token.type == OPEN_BRACKET:
            res = self.expr()
            self.next()
            return res

        return node

    def term(self):
        node = self.factor()
        while self.current().type in [MULTIPLY, PERCENT, DIVIDE]:
            op_token = self.next()
            right = self.factor()
            node = BinaryNode(node, op_token, right)
        return node

    def expr(self):
        node = self.term()
        while self.current().type in [PLUS, MINUS]:
            op_token = self.next()
            right = self.term()
            node = BinaryNode(node, op_token, right)
        return node

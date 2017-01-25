from repl import lexems
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

    def factor(self):
        token = self.next()

        node = LiteralNode(token)
        if token.type == lexems.MINUS and self.current().type == lexems.DIGIT:
            token = self.next()
            token.value = -token.value
            node = LiteralNode(token)
        elif token.type == lexems.LETTER and self.current().type == lexems.ASSIGNMENT:
            node = VariableDefinitionNode(token)
            op_token = self.next()
            right = self.expr()
            node = BinaryNode(node, op_token, right)
        elif token.type == lexems.OPEN_BRACKET:
            res = self.expr()
            self.next()
            return res

        return node

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

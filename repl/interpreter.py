from repl import lexems
from repl.parser import Parser
from repl.visitor import NodeVisitor


class Interpreter(NodeVisitor):
    def __init__(self):
        self.parser = Parser()

    def run(self, line):
        self.parser.clear()
        tree = self.parser.run(line)
        return self.visit(tree)

    def visit_BinaryNode(self, node):
        if node.op.type == lexems.PLUS:
            return self.visit(node.left) + self.visit(node.right)
        elif node.op.type == lexems.MINUS:
            return self.visit(node.left) - self.visit(node.right)
        elif node.op.type == lexems.MULTIPLY:
            return self.visit(node.left) * self.visit(node.right)
        elif node.op.type == lexems.DIVIDE:
            return self.visit(node.left) / self.visit(node.right)
        elif node.op.type == lexems.PERCENT:
            return self.visit(node.left) % self.visit(node.right)

    def visit_LiteralNode(self, node):
        return node.val.value


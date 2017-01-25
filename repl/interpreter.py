from repl.lexems import *
from repl.parser import Parser
from repl.visitor import NodeVisitor


class Interpreter(NodeVisitor):
    def __init__(self):
        self.parser = Parser()
        self.variables = {}

    def input(self, line):
        self.parser.clear()
        tree = self.parser.run(line)
        return self.visit(tree)

    def visit_BinaryNode(self, node):
        if node.op.type == PLUS:
            return self.visit(node.left) + self.visit(node.right)
        elif node.op.type == MINUS:
            return self.visit(node.left) - self.visit(node.right)
        elif node.op.type == MULTIPLY:
            return self.visit(node.left) * self.visit(node.right)
        elif node.op.type == DIVIDE:
            return self.visit(node.left) / self.visit(node.right)
        elif node.op.type == PERCENT:
            return self.visit(node.left) % self.visit(node.right)
        elif node.op.type == ASSIGNMENT:
            left = self.visit(node.left)
            val = self.visit(node.right)
            self.variables[left] = val
            return val

    def visit_LiteralNode(self, node):
        if node.val.type == LETTER:
            if not node.val.value in self.variables:
                raise Exception("Undefined variable {}".format(node.val.value))
            return self.variables[node.val.value]

        if node.val.type == EOF:
            return node.val.value

        return node.val.value

    def visit_VariableDefinitionNode(self, node):
        return node.val.value

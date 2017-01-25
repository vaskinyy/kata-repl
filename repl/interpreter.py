from repl import lexems
from repl.parser import Parser
from repl.visitor import NodeVisitor


class Interpreter(NodeVisitor):
    def __init__(self):
        self.parser = Parser()
        self.variables = {}

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
        elif node.op.type == lexems.ASSIGNMENT:
            left = self.visit(node.left)
            val = self.visit(node.right)
            self.variables[left] = val
            return val

    def visit_LiteralNode(self, node):
        if node.val.type == lexems.LETTER:
            if not node.val.value in self.variables:
                raise Exception("Undefined variable {}".format(node.val.value))
            return self.variables[node.val.value]

        return node.val.value

    def visit_VariableDefinitionNode(self, node):
        return node.val.value

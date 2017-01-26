from repl.lexems import *
from repl.parser import Parser
from repl.visitor import NodeVisitor


class Interpreter(NodeVisitor):
    def __init__(self):
        self.parser = Parser()
        self.variables = {}
        self.functions = {}

    def input(self, line):
        self.parser.clear()
        tree = self.parser.run(line)
        return self.visit(tree, None)

    def visit_BinaryNode(self, node, var_values, check):
        if check:
            self.visit(node.left, var_values, check)
            self.visit(node.right, var_values, check)
            return None
        if node.op.type == PLUS:
            return self.visit(node.left, var_values) + self.visit(node.right, var_values)
        elif node.op.type == MINUS:
            return self.visit(node.left, var_values) - self.visit(node.right, var_values)
        elif node.op.type == MULTIPLY:
            return self.visit(node.left, var_values) * self.visit(node.right, var_values)
        elif node.op.type == DIVIDE:
            return self.visit(node.left, var_values) / self.visit(node.right, var_values)
        elif node.op.type == PERCENT:
            return self.visit(node.left, var_values) % self.visit(node.right, var_values)
        elif node.op.type == ASSIGNMENT:
            left = self.visit(node.left, var_values)
            val = self.visit(node.right, var_values)
            self.variables[left] = val
            return val

    def visit_LiteralNode(self, node, var_values, check):
        if node.val.type == LETTER:

            vardict = self.variables
            if var_values != None:
                vardict = var_values

            if node.val.value not in vardict:
                raise Exception("Undefined variable {}".format(node.val.value))
            return vardict[node.val.value]

        if check:
            return None

        if node.val.type == EOF:
            return node.val.value

        return node.val.value

    def visit_VariableDefinitionNode(self, node, var_values, check):
        if node.val.value in self.functions:
            raise Exception("Already defined variable {}".format(node.name.value))
        return node.val.value

    def visit_FunctionDefinitionNode(self, node, var_values, check):
        if node.name.value in self.variables:
            raise Exception("Already defined variable {}".format(node.name.value))

        self.functions[node.name.value] = node

        # calc parameters
        local_varvalues = {}
        for (i, argnode) in enumerate(node.arguments):
            local_varvalues[argnode.value] = None

        # check variables
        self.visit(node.definition, local_varvalues, True)
        return ""

    def visit_FunctionCallNode(self, node, var_values, check):
        if node.name.value not in self.functions:
            raise Exception("Undefined function {}".format(node.name.value))
        function_node = self.functions[node.name.value]

        #calc parameters
        local_varvalues = {}
        for (i, argnode) in enumerate(function_node.arguments):
            local_varvalues[argnode.value] = self.visit(node.arguments[i], None)

        return self.visit(function_node.definition, local_varvalues)

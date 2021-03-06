

class BinaryNode(object):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

    def __str__(self):
        return "{} ({}, {})".format(self.op, self.left.__str__(), self.right.__str__())


class LiteralNode(object):
    def __init__(self, val):
        self.val = val

    def __str__(self):
        return self.val


class VariableDefinitionNode(object):
    def __init__(self, val):
        self.val = val

    def __str__(self):
        return self.val


class FunctionDefinitionNode(object):
    def __init__(self, name, arguments, definition):
        self.name = name
        self.arguments = arguments
        self.definition = definition

    def __str__(self):
        return "fn {}, {}".format(self.name, self.arguments)


class FunctionCallNode(object):
    def __init__(self, name, arguments):
        self.name = name
        self.arguments = arguments

    def __str__(self):
        return "fn {}, {}".format(self.name, self.arguments)


class BinaryNode(object):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right


class LiteralNode(object):
    def __init__(self, val):
        self.val = val

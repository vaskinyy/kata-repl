

class NodeVisitor(object):
    def visit(self, node, var_values, check=False):
        method_name = 'visit_' + type(node).__name__
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node, var_values, check)

    def generic_visit(self, node, var_values, check):
        raise Exception('No visit_{} method'.format(type(node).__name__))
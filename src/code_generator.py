class CodeGenerator:
    def __init__(self):
        self.code = []

    def visit(self, node):
        method_name = 'visit_' + type(node).__name__
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        raise Exception('No visit_{} method'.format(type(node).__name__))

    def visit_Program(self, node):
        for child in node.children:
            self.visit(child)

    def visit_Assign(self, node):
        target = node.children[0].value
        value = self.visit(node.children[1])
        self.code.append(('STORE', target, value))

    def visit_Number(self, node):
        return node.value

    def visit_BinOp(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        op = node.op
        if op == '+':
            return left + right
        elif op == '-':
            return left - right
        elif op == '*':
            return left * right
        elif op == '/':
            return left / right

def generate_code(ast):
    generator = CodeGenerator()
    generator.visit(ast)
    return generator.code

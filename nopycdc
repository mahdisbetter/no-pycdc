import ast
import random

class CustomBlockTransformer(ast.NodeTransformer):
    def visit_FunctionDef(self, node):
        node.body.insert(0, self.create_custom_block())
        node.body.append(self.create_custom_block())
        return self.generic_visit(node)

    def visit_AsyncFunctionDef(self, node):
        node.body.insert(0, self.create_custom_block())
        node.body.append(self.create_custom_block())
        return self.generic_visit(node)
    
    def visit_ClassDef(self, node):
        node.body.insert(0, self.create_custom_block())
        node.body.append(self.create_custom_block())
        return self.generic_visit(node)

    def visit_While(self, node):
        node.body.insert(0, self.create_custom_block())
        node.body.append(self.create_custom_block())
        return self.generic_visit(node)

    def visit_For(self, node):
        node.body.insert(0, self.create_custom_block())
        node.body.append(self.create_custom_block())
        return self.generic_visit(node)

    def visit_If(self, node):
        node.body.insert(0, self.create_custom_block())

        for stmt in node.orelse:
            if isinstance(stmt, ast.If):
                self.visit_If(stmt)
            elif hasattr(stmt, 'body'):
                stmt.body.insert(0, self.create_custom_block())
                stmt.body.append(self.create_custom_block())
        node.body.append(self.create_custom_block())
        return self.generic_visit(node)

    def visit_ExceptHandler(self, node):
        if hasattr(node, 'body'):
            node.body.insert(0, self.create_custom_block())
            node.body.append(self.create_custom_block())
        return self.generic_visit(node)

    def visit_Try(self, node):
        if hasattr(node, 'body'):
            node.body.insert(0, self.create_custom_block())
            node.body.append(self.create_custom_block())
        if node.finalbody:
            for stmt in node.finalbody:
                if hasattr(stmt, 'body'):
                    stmt.body.insert(0, self.create_custom_block())
                    stmt.body.append(self.create_custom_block())
        return self.generic_visit(node)

    def create_custom_block(self):
        return ast.parse("""
match 0:
  case 1:
    print()
  case _:
    ...
""").body[0]

    def create_custom_block_2(self):
        return ast.parse("""
try:
  raise TypeError
except* (TypeError):
  ...
""").body[0]

def random_blocks(body):
    num_blocks = min(5, len(body) + 1)
    positions = sorted(random.sample(range(len(body) + 1), k=num_blocks))
    for pos in positions:
        body.insert(pos, CustomBlockTransformer().create_custom_block())
        body.insert(pos, CustomBlockTransformer().create_custom_block_2())

def add_custom_blocks(source_code):
    tree = ast.parse(source_code)
    transformer = CustomBlockTransformer()
    transformed_tree = transformer.visit(tree)
    random_blocks(transformed_tree.body)

    return ast.unparse(transformed_tree)

def main(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        source_code = file.read()

    new_source_code = '''
try:
  raise TypeError
except* (TypeError):
  ...\n
'''+source_code+'''\n
try:
  raise TypeError
except* (TypeError):
  ...
'''
    new_source_code = add_custom_blocks(new_source_code)

    with open(filename, 'w', encoding='utf-8') as file:
        file.write(new_source_code)


filename = input('filename: ')
main(filename)

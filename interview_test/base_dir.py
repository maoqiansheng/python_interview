import os

abs_path = os.path.abspath(__file__)
print(abs_path)
pre_path = os.path.dirname(abs_path)
print(pre_path)
base_dir = os.path.dirname(pre_path)
print(base_dir)

add_path = os.path.join(base_dir, 'template')
print(add_path)
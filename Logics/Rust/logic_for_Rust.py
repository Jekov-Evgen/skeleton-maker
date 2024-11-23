import os

def create_project_Rust(name, path):
    new_path = os.path.join(path, name)
    os.mkdir(new_path)
    os.chdir(new_path)
    os.system(f"cargo new {name}")
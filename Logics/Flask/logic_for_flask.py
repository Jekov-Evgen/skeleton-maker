import os
from Logics.Flask.skeleton_code.code import CONST_FLASK

def create_project_Flask(name : str, path):
    new_path = os.path.join(path, name)
    os.mkdir(new_path)
    os.chdir(new_path)
    
    with open("app.py", "w") as f:
        f.write(CONST_FLASK)
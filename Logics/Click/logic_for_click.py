import os
from Logics.Click.skeleton_code.code import CONST_CLICK

def create_project_click(name : str, path):
    new_path = os.path.join(path, name)
    os.mkdir(new_path) 
    os.chdir(new_path)
    
    with open("cli_app.py", 'w') as f:
        f.write(CONST_CLICK)
    
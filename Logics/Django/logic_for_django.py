import os
from Logics.Django.skeleton_code.cod import CONST_GIT

def create_project_Django(name : str):
    desktop_path = os.path.join(os.path.expanduser("~"), r"OneDrive\Desktop")
    new_path = os.path.join(desktop_path, name)    
    os.mkdir(new_path)
    
    os.chdir(new_path)
    os.system(f"django-admin startproject {name}")
    
    os.chdir(os.path.join(new_path, name))
    
    with open(".gitignore", 'w') as f:
        f.write(CONST_GIT)
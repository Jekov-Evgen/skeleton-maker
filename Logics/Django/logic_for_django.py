import os
from Logics.Django.skeleton_code.cod import CONST_GIT

def create_project_Django(name : str, path):
    new_path = os.path.join(path, name)    
    os.mkdir(new_path)
    
    os.chdir(new_path)
    os.system(f"django-admin startproject {name}")
    
    os.chdir(os.path.join(new_path, name))
    
    with open(".gitignore", 'w') as f:
        f.write(CONST_GIT)
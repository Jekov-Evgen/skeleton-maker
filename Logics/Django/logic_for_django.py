import os

def create_project_Django(name : str):
    desktop_path = os.path.join(os.path.expanduser("~"), r"OneDrive\Desktop")
    new_path = os.path.join(desktop_path, name)    
    os.mkdir(new_path)
    
    os.chdir(new_path)
    os.system(f"django-admin startproject {name}")
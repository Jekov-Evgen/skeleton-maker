import os

def create_project_Qt(name : str):
    desktop_path = os.path.join(os.path.expanduser("~"), r"OneDrive\Desktop")
    new_path = os.path.join(desktop_path, name)    
    os.mkdir(new_path)
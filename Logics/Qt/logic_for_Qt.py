import os
from Logics.Qt.skeleton_code.code import CONST_COD_MAIN

def create_project_Qt(name : str):
    desktop_path = os.path.join(os.path.expanduser("~"), r"OneDrive\Desktop")
    new_path = os.path.join(desktop_path, name)    
    os.mkdir(new_path)
    
    name_main = "main.py"
    main_file = os.path.join(new_path, name_main)
    
    with open(main_file, 'w') as f:
        f.write(CONST_COD_MAIN)
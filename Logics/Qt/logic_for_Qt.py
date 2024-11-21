import os
from Logics.Qt.skeleton_code.code import CONST_COD_MAIN, CONST_COD_MAIN_WINDOW

def create_project_Qt(name : str):
    desktop_path = os.path.join(os.path.expanduser("~"), r"OneDrive\Desktop")
    new_path = os.path.join(desktop_path, name)    
    os.mkdir(new_path)
    
    name_main = "main.py"
    main_file = os.path.join(new_path, name_main)
    folder_UI = os.path.join(new_path, "GUI")
    file_main_window = os.path.join(folder_UI, "main_window.py")
    folder_style = os.path.join(folder_UI, "style")
    style_file = os.path.join(folder_style, "style_Qt.py")
    
    os.mkdir(folder_UI)
    os.mkdir(folder_style)
    
    with open(main_file, 'w') as f:
        f.write(CONST_COD_MAIN)
    
    with open(file_main_window, 'w') as f:
        f.write(CONST_COD_MAIN_WINDOW)
    
    with open(style_file, 'w'):
        pass
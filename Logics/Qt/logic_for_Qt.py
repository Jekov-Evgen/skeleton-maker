import os
from Logics.Qt.skeleton_code.code import CONST_COD_MAIN, CONST_COD_MAIN_WINDOW, CONST_GIT

def create_project_Qt(name : str, path):
    new_path = os.path.join(path, name)    
    os.mkdir(new_path)
    
    name_main = "main.py"
    main_file = os.path.join(new_path, name_main)
    folder_UI = os.path.join(new_path, "GUI")
    file_main_window = os.path.join(folder_UI, "main_window.py")
    folder_style = os.path.join(folder_UI, "style")
    style_file = os.path.join(folder_style, "style_Qt.py")
    image_folder = os.path.join(new_path, "image")
    logics_folder = os.path.join(new_path, "Logics")
    git_ignore = os.path.join(new_path, ".gitignore")
    
    os.mkdir(folder_UI)
    os.mkdir(folder_style)
    os.mkdir(image_folder)
    os.mkdir(logics_folder)
    
    with open(main_file, 'w') as f:
        f.write(CONST_COD_MAIN)
    
    with open(file_main_window, 'w') as f:
        f.write(CONST_COD_MAIN_WINDOW)
    
    with open(style_file, 'w'):
        pass
    
    with open(git_ignore, 'w') as f:
        f.write(CONST_GIT)
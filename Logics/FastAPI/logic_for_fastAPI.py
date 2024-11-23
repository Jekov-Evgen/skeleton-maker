import os
from Logics.FastAPI.skeleton_code.code import CONST_MAIN_PY, CONST_ENDPOINTS_PY, CONST_COMMON_PY, CONST_CONFIG_PY, CONST_ENV, CONST_REQUIMENTS_TXT, CONST_TEST_MAIN_PY, CONST_USER_PY

def create_project_FastAPI(name, path):
    new_path = os.path.join(path, name)
    
    os.mkdir(new_path)
    os.chdir(new_path)
    os.mkdir(os.path.join(new_path, "app"))
    os.chdir(os.path.join(new_path, "app"))
    
    path_app = os.path.join(new_path, "app")
    
    with open("__init__.py", 'w'):
        pass
    
    with open("main.py", 'w') as f:
        f.write(CONST_MAIN_PY)
    
    os.mkdir("api")
    os.mkdir("core")
    os.mkdir("dependencies")
    os.mkdir("models")
    os.mkdir("tests")
    
    os.chdir(os.path.join(path_app, "api"))
    
    with open("__init__.py", 'w'):
        pass
    
    with open("endpoints.py", 'w') as f:
        f.write(CONST_ENDPOINTS_PY)
    
    os.chdir(os.path.join(path_app, "core"))
    
    with open("__init__.py", 'w'):
        pass
    
    with open("config.py", 'w') as f:
        f.write(CONST_CONFIG_PY)
    
    os.chdir(os.path.join(path_app, "dependencies"))
    
    with open("__init__.py", 'w'):
        pass
    
    with open("common.py", 'w') as f:
        f.write(CONST_COMMON_PY)
    
    os.chdir(os.path.join(path_app, "models"))
    
    with open("__init__.py", 'w'):
        pass
    
    with open("user.py", 'w') as f:
        f.write(CONST_USER_PY)
    
    os.chdir(os.path.join(path_app, "tests"))
    
    with open("__init__.py", 'w'):
        pass
    
    with open("test_main.py", 'w') as f:
        f.write(CONST_TEST_MAIN_PY)
    
    os.chdir(new_path)
    
    with open(".env", 'w') as f:
        f.write(CONST_ENV)
    
    with open("requirements.txt", 'w') as f:
        f.write(CONST_REQUIMENTS_TXT)
    
    with open("README.md", 'w'):
        pass
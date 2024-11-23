import os

def create_project_FastAPI(name, path):
    new_path = os.path.join(path, name)
    
    os.mkdir(new_path)
    os.chdir(new_path)
    os.mkdir(os.path.join(new_path, "app"))
    os.chdir(os.path.join(new_path, "app"))
    
    path_app = os.path.join(new_path, "app")
    
    with open("__init__.py", 'w') as f:
        pass
    
    with open("main.py", 'w') as f:
        pass
    
    os.mkdir("api")
    os.mkdir("core")
    os.mkdir("dependencies")
    os.mkdir("models")
    os.mkdir("tests")
    
    os.chdir(os.path.join(path_app, "api"))
    
    with open("__init__.py", 'w') as f:
        pass
    
    with open("endpoints.py", 'w') as f:
        pass
    
    os.chdir(os.path.join(path_app, "core"))
    
    with open("__init__.py", 'w') as f:
        pass
    
    with open("config.py", 'w') as f:
        pass
    
    os.chdir(os.path.join(path_app, "dependencies"))
    
    with open("__init__.py", 'w') as f:
        pass
    
    with open("common.py", 'w') as f:
        pass
    
    os.chdir(os.path.join(path_app, "models"))
    
    with open("__init__.py", 'w') as f:
        pass
    
    with open("user.py", 'w') as f:
        pass
    
    os.chdir(os.path.join(path_app, "tests"))
    
    with open("__init__.py", 'w') as f:
        pass
    
    with open("test_main.py", 'w') as f:
        pass
    
    os.chdir(new_path)
    
    with open(".env", 'w') as f:
        pass
    
    with open("requirements.txt", 'w') as f:
        pass
    
    with open("README.md", 'w'):
        pass
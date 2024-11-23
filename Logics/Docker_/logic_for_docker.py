import os
from Logics.Docker_.skeleton_code.code import CONST_PYTHON_DOCKER, CONST_HTML_DOCKER, CONST_DOCKER_FILE, CONST_PYTHON_CLIENT, CONST_CLIENT_DOCKER_FILE, CONST_DOCKER_COMPOSE_YML

def create_project_Docker(name, path):
    new_path = os.path.join(path, name)
    os.mkdir(new_path)
    os.chdir(new_path)
    
    os.mkdir(os.path.join(new_path, "client"))
    os.mkdir(os.path.join(new_path, "server"))
    
    with open("docker-compose.yml", 'w') as f:
        f.write(CONST_DOCKER_COMPOSE_YML)
    
    os.chdir(os.path.join(new_path, "server"))
    
    with open("server.py", 'w') as f:
        f.write(CONST_PYTHON_DOCKER)
    
    with open("index.html", 'w') as f:
        f.write(CONST_HTML_DOCKER)
    
    with open("Dockerfile", 'w') as f:
        f.write(CONST_DOCKER_FILE)
        
    os.chdir(os.path.join(new_path, "client"))
    
    with open("client.py", 'w') as f:
        f.write(CONST_PYTHON_CLIENT)
        
    with open("Dockerfile", 'w') as f:
        f.write(CONST_CLIENT_DOCKER_FILE)
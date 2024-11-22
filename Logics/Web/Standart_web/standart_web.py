import os
from Logics.Web.Standart_web.code import get_html, CONST_CSS, CONST_JS

def create_standard_web_project(name : str, path):
    html_cod = get_html(name)
    
    new_path = os.path.join(path, name)
    os.mkdir(new_path)
    os.chdir(new_path)
    
    html = "html"
    css = "css"
    js = "js"
    
    os.mkdir(os.path.join(new_path, html))
    os.chdir(os.path.join(new_path, html))
    
    with open("index.html", 'w') as f:
        f.write(html_cod)
        
    os.chdir(new_path)
    os.mkdir(os.path.join(new_path, css))
    os.chdir(os.path.join(new_path, css))
    
    with open("style.css", 'w') as f:
        f.write(CONST_CSS)
        
    os.chdir(new_path)
    os.mkdir(os.path.join(new_path, js))
    os.chdir(os.path.join(new_path, js))
    
    with open("script.js", 'w') as f:
        f.write(CONST_JS)
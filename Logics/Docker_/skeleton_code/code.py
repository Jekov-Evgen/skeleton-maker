CONST_PYTHON_DOCKER = """
import http.server
import socketserver

handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", 1234), handler) as httpd:

   httpd.serve_forever()
"""


CONST_HTML_DOCKER = """
Docker-Compose is magic!
"""

CONST_DOCKER_FILE = """
FROM python:latest

ADD server.py /server/
ADD index.html /server/

WORKDIR /server/
"""

CONST_PYTHON_CLIENT = """
import urllib.request

fp = urllib.request.urlopen("http://localhost:1234/")

encodedContent = fp.read()
decodedContent = encodedContent.decode("utf8")

print(decodedContent)

fp.close()
"""

CONST_CLIENT_DOCKER_FILE = """
FROM python:latest

ADD client.py /client/

WORKDIR /client/
"""

CONST_DOCKER_COMPOSE_YML = """
services:

  server:

    build: server/

    command: python ./server.py
    
    ports:
      - 1234:1234

  client:

    build: client/
 
    command: python ./client.py

    network_mode: host

    depends_on:
      - server
"""
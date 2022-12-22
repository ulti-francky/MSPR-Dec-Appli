from simple_http_server import route, server
from simple_http_server import Parameter
import random

@route("/")
def index():
    f = open("acceuil.html","r")
    html = f.read()
    f.close()
    return html   



@route("/index.html",) 
def index():
    f = open("index.html","r")
    html = f.read()
    f.close()
    return html

@route("/acceuil.html",) 
def index():
    f = open("acceuil.html","r")
    html = f.read()
    f.close()
    return html     

server.start(port=8000)
import cherrypy
import os
from pages import *
from pageForm import *

local_dir = os.path.dirname(__file__)

index()

server_config={
'server.socket_host': '127.0.0.1',
'server.socket_port': 80
}
cherrypy.config.update(server_config)

local_config = {
    "/": {
        "tools.staticdir.on": True,
        "tools.staticdir.dir": local_dir,
    },
    "/#": {
        "request.dispatch": cherrypy.dispatch.MethodDispatcher(),
    }
}




root = index()
root.sobre = PaginaAbout()
root.ciclodecursos = PaginaCursos()
root.fippetec = PaginaEtec()
root.festalinux = PaginaLinux()
root.maratonadeprogramacao = PaginaMaratona()
root.rotaAluno = PaginaForm()

cherrypy.quickstart(root,config=local_config)

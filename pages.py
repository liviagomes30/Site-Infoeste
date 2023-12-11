import cherrypy
from classes.aluno import *

class index():
    header = open("html/headerIndex.html", encoding="utf-8").read()
    titulo = open("html/titulo.html", encoding="utf-8").read()
    cards = open("html/cards.html", encoding="utf-8").read()
    contact = open("html/contact.html", encoding="utf-8").read()

    @cherrypy.expose()
    def index(self, id=0, tnome=''):
        html = self.header 
        html += self.titulo
        html += self.cards
        html += self.contact
        return html
    

class PaginaAbout():
    header = open("html/header.html", encoding="utf-8").read()
    body = open("html/pageSobre.html", encoding="utf-8").read()

    @cherrypy.expose()
    def index(self):
        html = self.header + self.body

        return html
    
class PaginaCursos():
    header = open("html/header.html", encoding="utf-8").read()
    body = open("html/ciclodecursos.html", encoding="utf-8").read()
    @cherrypy.expose()
    def index(self):
        html = self.header + self.body

        return html
    
class PaginaEtec():
    header = open("html/header.html", encoding="utf-8").read()
    body = open("html/fippetec.html", encoding="utf-8").read()

    @cherrypy.expose()
    def index(self):
        html = self.header + self.body

        return html

class PaginaLinux():
    header = open("html/header.html", encoding="utf-8").read()
    body = open("html/festalinux.html", encoding="utf-8").read()

    @cherrypy.expose()
    def index(self):
        html = self.header + self.body

        return html
    

class PaginaMaratona():

    header = open("html/header.html", encoding="utf-8").read()
    body = open("html/maratona.html", encoding="utf-8").read()

    @cherrypy.expose()
    def index(self):
        html = self.header + self.body

        return html
    


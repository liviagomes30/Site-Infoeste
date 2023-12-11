import cherrypy
from classes.aluno import *
import re

class PaginaForm():
    header = open("html/headerIndex.html", encoding="utf-8").read()

    @cherrypy.expose()
    def index(self):
        return self.montaFormulario()


    def montaFormulario(self, pId=0, tnome='', temail='', telefone='', selOpcao=1):
        form = open ("html/inscricao.html", encoding="utf-8").read()
        str = self.header
        str += form  % (pId, tnome, temail, telefone, selOpcao)
        
        objAluno = Aluno()
        dados = objAluno.obterAlunos() 
        if dados != []:
            str += self.montaTabela(dados)
        return str
    
    @cherrypy.expose()
    def montaTabela(self, dados):
        dados_cadastrados = open("html/dadoscadastrados.html", encoding="utf-8").read()
        dados_linha = open("html/dados_linha.html", encoding="utf-8").read()
        html = dados_cadastrados

        for linha in dados:
            html += dados_linha  % (linha['aluno_id'], linha['aluno_nome'], linha['aluno_email'], linha['aluno_tel'], linha['aluno_curso'], linha['aluno_id'], linha['aluno_id'])
        html += ''' </table> <br> <br>'''
        return html

    @cherrypy.expose()
    def gravarAluno(self, txtId, tnome, temail, telefone, selOpcao, bgravar):
        if len(tnome) > 0:
            #valida email
            if not re.match(r"[^@]+@[^@]+\.[^@]+", temail):
                return '''
                                <script>
                                    alert("O formato do e-mail é inválido");
                                    window.location.href = "/rotaAluno";
                                </script>
                            '''

                #valida tel
            if not re.match(r"\d{10,11}", telefone):
                return '''
                                <script>
                                    alert("O formato do telefone é inválido. Deve conter 10 ou 11 dígitos");
                                    window.location.href = "/rotaAluno";
                                </script>
                            '''

            objAluno = Aluno()
            objAluno.set_nome(tnome)
            objAluno.set_email(temail)
            objAluno.set_tel(telefone)
            objAluno.set_curso(selOpcao)

            retorno = 0
            if int(txtId) == 0:  # nova espécie
                retorno = objAluno.gravar()
            else: 
                objAluno.set_id(int(txtId))
                retorno = objAluno.alterar()
            if retorno > 0:
                return '''
                        <script>
                           alert("O aluno %s foi gravado com sucesso!!")
                           window.location.href = "/rotaAluno"
                        </script>
                       ''' % (tnome)
            else:  
                return '''
                        <h2> Erro ao gravar o aluno %s</h2>
                        <a href="/rotaAluno">voltar</a>
                        ''' % (tnome)
        else: 
            return '''
                   <h2> O nome do aluno deve ser informado</h2>
                   <a href="/rotaAluno">voltar</a>
               '''

    @cherrypy.expose()
    def excluirAluno(self, idAluno):
        objAluno = Aluno()
        objAluno.set_id(int(idAluno))
        if objAluno.excluir() > 0:
            newAluno = Aluno()
            obj = newAluno.obterAlunos()
            if obj == []:
                newAluno.clean()
            raise cherrypy.HTTPRedirect('/rotaAluno')
        else:
            return '''
            <h2>Não foi possível excluir o aluno!!</h2>
            [<a href="/rotaAluno">Voltar</a>]
            '''

    @cherrypy.expose()
    def alterarAluno(self, idAluno):
        objAluno = Aluno()
        dadosAlunoSelec = objAluno.obterAluno(idAluno)
        return self.montaFormulario(dadosAlunoSelec[0]['aluno_id'],
                                    dadosAlunoSelec[0]['aluno_nome'],
                                    dadosAlunoSelec[0]['aluno_email'],
                                    dadosAlunoSelec[0]['aluno_tel'],
                                    dadosAlunoSelec[0]['aluno_curso']
                                    )

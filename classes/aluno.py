from classes.banco import Banco

class Aluno(): 
    
    def __init__(self):
        self.__id = 0
        self.__nome = ''
        self.__email = ''
        self.__tel = ''
        self.__curso = 1
        self.__banco = Banco() 

    
    def set_id(self, pId): 
        if pId > 0: 
            self.__id = pId
    def set_nome(self,tnome):
        if len(tnome) > 0:
            self.__nome = tnome

    def set_email(self,temail):
        self.__email = temail

    def set_tel(self,telefone):
        self.__tel = telefone

    def set_curso(self,selOpcao):
        self.__curso = selOpcao

    
    def get_id(self):
        return self.__id

    def get_nome(self):
        return self.__nome

    def get_email(self):
        return self.__email
    
    def get_tel(self):
        return self.__tel
    
    def get_curso(self):
        return self.__curso

    
    def obterAlunos(self):
        sql = '''
              SELECT aluno_id, aluno_nome, aluno_email, aluno_tel, aluno_curso
              FROM Aluno
              ORDER by aluno_id
              '''
        return self.__banco.executarSelect(sql)

    def gravar(self): # vai pegar os dados do objeto e gravar na tabela do banco
        sql = ''' INSERT INTO Aluno (aluno_nome,aluno_email,aluno_tel,aluno_curso)
                 values ("#nome", "#email", "#tel", #curso)
              '''
        sql = sql.replace('#nome',self.__nome)
        sql = sql.replace('#email', self.__email)
        sql = sql.replace('#tel', self.__tel)
        sql = sql.replace('#curso', self.__curso)
        return self.__banco.executarInsertUpdateDelete(sql)

    def obterAluno(self, pId=0):
        if pId != 0:
            self.__id = pId
        sql = ''' SELECT aluno_id, aluno_nome, aluno_email, aluno_tel, aluno_curso
                  FROM Aluno
                  where aluno_id = #id         '''
        sql = sql.replace('#id', str(self.__id))
        return self.__banco.executarSelect(sql)

    def excluir(self):
        sql = 'delete from Aluno where aluno_id = #id'
        sql = sql.replace('#id', str(self.__id))
        return self.__banco.executarInsertUpdateDelete(sql)

    def alterar(self):
        sql = 'update Aluno set aluno_nome = "#nome", aluno_email = "#email", aluno_tel = "#tel", aluno_curso =  "#curso" where aluno_id = #id'
        sql = sql.replace('#nome',self.__nome)
        sql = sql.replace('#email',self.__email)
        sql = sql.replace('#tel',self.__tel)
        sql = sql.replace('#curso',self.__curso)
        sql = sql.replace('#id',str(self.__id))
        return self.__banco.executarInsertUpdateDelete(sql)
    
    def clean(self):
        sql = 'delete from sqlite_sequence'
        return self.__banco.executarInsertUpdateDelete(sql)
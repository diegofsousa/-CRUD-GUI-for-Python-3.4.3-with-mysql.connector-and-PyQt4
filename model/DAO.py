import mysql.connector
from mysql.connector import errorcode
from ProjetoCRUD.controller.Usuarios import *

class dao:
    def __init__(self):
        try:
            self.con = mysql.connector.connect(user='root', password='961100', database='poo_df')
        except mysql.connector.Error as erro:
            if erro.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Usuário/Senha do banco MySql errado(s)")
            elif erro.errno == errorcode.ER_BAD_DB_ERROR:
                print("Banco de Dados inexistente!")
            else:
                print(erro)
        else:
            #print("Conexão feita com sucesso!")
            self.con.close

    def versão(self):
        try:
            cursor = self.con.cursor()
            cursor.execute('select version()')
            data = cursor.fetchone()
            cursor.close()
        except BaseException as os:  # BaseException é o pai de todas as excessões no pytho 3+
            data = None
        return data

    def listarUsuarios(self):
        try:
            lista = []
            cursor = self.con.cursor()
            cursor.execute('select * from usuarios')
            for (id, email, senha) in cursor:
                novo = Usuarios(id, email, senha)
                lista.append(novo)
            cursor.close()
        except BaseException as os:
            return False
        return lista

    def retornarUmUsuario(self, indice):
        lampada = False
        try:
            cursor = self.con.cursor()
            cursor.execute("select * from usuarios where id = '{}'".format(indice))
            ind = object
            for (id, email, senha) in cursor:
                ind = Usuarios(id, email, senha)
                lampada = True
            if lampada == False:
                return False
            cursor.close()
            #print("Valor de ind: {}".format(ind.id))
        except BaseException as os:
            print("Deu excessão")
            return False
        return ind

    def inserirUsuario(self, usuario):
        try:
            cursor = self.con.cursor()
            comando = ("INSERT INTO usuarios (email, senha) VALUES (%s, %s)")
            valores = (usuario.email, usuario.senha)
            cursor.execute(comando, valores)
            self.con.commit()
            cursor.close()
            cursor = self.con.cursor()
            cursor.execute('select * from usuarios')
            ultimo = object
            for (id, email, senha) in cursor:
                ultimo = Usuarios(id, email, senha)
            cursor.close()
        except BaseException as os:
            return False
        return ultimo

    def atualizarUsuario(self, indice, email, senha):
        try:
            cursor = self.con.cursor()
            comando = ("UPDATE usuarios SET email ='{}', senha='{}' WHERE id='{}'".format(email, senha, indice))
            cursor.execute(comando)
            self.con.commit()
            cursor.close()
            indiceAtualizado = self.retornarUmUsuario(indice)
        except BaseException as os:
            return False
        return indiceAtualizado

    def deletarUsuario(self, indice):
        try:
            objetoASerDeletado = self.retornarUmUsuario(indice)
            cursor = self.con.cursor()
            comando = ("DELETE FROM usuarios WHERE id='{}'".format(indice))
            cursor.execute(comando)
            self.con.commit()
            cursor.close()
        except BaseException as os:
            return False
        return objetoASerDeletado

ver = dao()
#-------------listando-------------
#lista = ver.listarUsuarios()
#for i in range(len(lista)):
#    print("ID: {} - Email: {} - Senha: {}" .format(lista[i].indice, lista[i].email, lista[i].senha))

#-------------inserindo um elemento-
#novo = Usuarios(None, "testandonovo@gg.com", "4567")
#ultimo = ver.inserirUsuario(novo)
#
#print(ultimo.indice, ultimo.email, ultimo.senha)

#------------atualizando um elemento-
#atualiza = ver.atualizarUsuario(9,"emailatualizado@e.com", "novasenha")
#print(atualiza.indice, atualiza.email, atualiza.senha)

#-----------deletando um elemento---
#deletado = ver.deletarUsuario(6)
#print(deletado.indice, deletado.email, deletado.senha)


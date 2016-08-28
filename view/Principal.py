from ProjetoCRUD.controller.Usuarios import *
from ProjetoCRUD.model.DAO import *

class principal:
    def __init__(self):
        self.con = dao()
        self.opcao = 10

        while self.opcao != 0:
            print("PROJETO MVC + CRUD"
                  "\n 1 - Listar todos os elementos"
                  "\n 2 - Inserir um elemento"
                  "\n 3 - Consultar um elemento"
                  "\n 4 - Atualizar um elemento"
                  "\n 5 - Deletar um elemento"
                  "\n 0 - Finalizar aplicação")

            self.opcao = int(input("\nSelecione uma opção: "))

            if self.opcao == 1:
                self.op1()
                input()
            elif self.opcao == 2:
                self.op2()
                input()
            elif self.opcao == 3:
                self.op3()
                input()
            elif self.opcao == 4:
                self.op4()
                input()
            elif self.opcao == 5:
                self.op5()
                input()
            elif self.opcao == 0:
                print("\nAplicação finalizada")
            else: print("Comando inválido")


    def op1(self):
        lista = self.con.listarUsuarios()
        for i in range(len(lista)):
            print("ID: {} - Email: {} - Senha: {}" .format(lista[i].indice, lista[i].email, lista[i].senha))

    def op2(self):
        email = input("Insira um email: ")
        senha = input("Insira uma senha: ")
        novo = Usuarios(None, email, senha)
        novo = self.con.inserirUsuario(novo)

        if novo == False:
            print("\nOperação não sucedida!")
        else:
            print("\n\nSucesso ao adicionar!")
            print("ID: {} - Email: {} - Senha: {}".format(novo.indice, novo.email, novo.senha))

    def op3(self):
        id = input("Insira o ID do elemento: ")
        id = self.con.retornarUmUsuario(id)

        if id == False:
            print("\nOperação não sucedida!")
        else:
            print("\n\nElemento achado")
            print("ID: {} - Email: {} - Senha: {}".format(id.indice, id.email, id.senha))

    def op4(self):
        ind = input("Insira o ID do elemento: ")
        id = self.con.retornarUmUsuario(ind)

        if id == False:
            print("\nOperação não sucedida!")
        else:
            print("\n\nElemento achado")
            print("ID: {} - Email: {} - Senha: {}".format(id.indice, id.email, id.senha))
            print("Informe os novos atributos:")
            email = input("Informe o novo email: ")
            senha = input("Informe a nova senha: ")
            id = self.con.atualizarUsuario(ind, email, senha)

            if id == False:
                print("\nOperação não sucedida!")
            else:
                print("\n\nElemento atualizado!")
                print("ID: {} - Email: {} - Senha: {}".format(id.indice, id.email, id.senha))
    def op5(self):
        id = input("\nInforme o indice a ser excluído: ")
        excluso = self.con.deletarUsuario(id)

        if excluso == False:
            print("\nOperação não sucedida")
        else:
            print("Elemento excluído!")
            print("ID: {} - Email: {} - Senha: {}".format(excluso.indice, excluso.email, excluso.senha))

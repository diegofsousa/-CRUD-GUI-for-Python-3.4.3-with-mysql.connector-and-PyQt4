import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from ProjetoCRUD.controller.Usuarios import *
from ProjetoCRUD.model.DAO import *


class Listando(QDialog):
    def __init__(self,janela, parent=None):
        self.con = dao()
        super(Listando, self).__init__(parent)

        lista = QListWidget()
        listaDoBanco = self.con.listarUsuarios()
        for i in range(len(listaDoBanco)):
            item = QListWidgetItem("ID: {} - Email: {} - Senha: {}".format(listaDoBanco[i].indice, listaDoBanco[i].email, listaDoBanco[i].senha))
            lista.addItem(item)

        vbox = QVBoxLayout()
        vbox.addWidget(lista)
        self.setLayout(vbox)
        self.setWindowTitle("Listando")
        self.setGeometry(500,300,500,300)
        janela.ultimaAçao.setText("Ultima açao: Listou usuarios")

class Cadastrando(QDialog):
    def __init__(self, janela, parent=None):
        self.con = dao()
        super(Cadastrando, self).__init__(parent)

        lblEmail = QLabel("Email: ")
        self.campoEmail = QLineEdit("")

        lblSenha = QLabel("Senha: ")
        self.campoSenha = QLineEdit("")

        botaoSalvar = QPushButton("Salvar")

        camposDeEmails = QHBoxLayout()
        camposDeEmails.addWidget(lblEmail)
        camposDeEmails.addWidget(self.campoEmail)

        camposDeSenha = QHBoxLayout()
        camposDeSenha.addWidget(lblSenha)
        camposDeSenha.addWidget(self.campoSenha)

        vbox = QVBoxLayout()
        vbox.addLayout(camposDeEmails)
        vbox.addLayout(camposDeSenha)
        vbox.addWidget(botaoSalvar)

        self.connect(botaoSalvar, SIGNAL("clicked()"), self.salvar)

        self.setLayout(vbox)
        self.setWindowTitle("Cadastrar email")
        janela.ultimaAçao.setText("Ultima açao: Cadastrou usuario")
        self.setGeometry(500, 300, 300, 100)

    def salvar(self):
        print("Salvando...")
        print(self.campoEmail.displayText())
        if self.campoSenha.displayText() == "" or self.campoEmail.displayText() == "":
            msg = QMessageBox.warning(self, "Alerta",
                                      "Preencha todos os campos!", QMessageBox.Close)
        else:
            msg = QMessageBox.question(self, "Confirmaçao",
                                       "Deseja cadastrar?\n\nEmail: {}\nSenha: {}".format(self.campoEmail.displayText(), self.campoSenha.displayText()), QMessageBox.Yes | QMessageBox.No)
            if msg == 16384:
                print("Cadastrou!")
                novo = Usuarios(None, self.campoEmail.displayText(), self.campoSenha.displayText())
                novo = self.con.inserirUsuario(novo)

                if novo == False:
                    msg = QMessageBox.information(self, "Informaçao",
                                                  "Falha no cadastro!", QMessageBox.Close)
                else:
                    print("\n\nSucesso ao adicionar!")
                    print("ID: {} - Email: {} - Senha: {}".format(novo.indice, novo.email, novo.senha))
                    msg = QMessageBox.information(self, "Sucesso!",
                                                  "Cadastro efetuado:"
                                                  "\n\nID: {}"
                                                  "\nEmail: {}"
                                                  "\nSenha: {}".format(novo.indice, novo.email, novo.senha), QMessageBox.Close)
                    self.close()



class Consultando:
    def __init__(self, janela):
        self.con = dao()
        l = self.con.listarUsuarios()
        paraACaixa = []

        for i in range(len(l)):
            paraACaixa.append(str(l[i].indice))
        print(paraACaixa)

        msg = QInputDialog.getItem(None, 'Consulta por indice', 'Selecione o indice: ', paraACaixa, 1, True)
        print(msg[0])

        janela.ultimaAçao.setText("Ultima açao: Consultou usuario")

        if msg[1] == True:
            volta = self.con.retornarUmUsuario(msg[0])
            print(volta)

            if volta == False:
                msg = QMessageBox.warning(None, "Resultado",
                                          "Nao ha cadastros com este indice!", QMessageBox.Close)
            else:
                msg = QMessageBox.information(None, "Resultado",
                                          "Cadastro pesquisado:"
                                          "\n\nID: {}"
                                          "\nEmail: {}"
                                          "\nSenha: {}".format(volta.indice, volta.email, volta.senha), QMessageBox.Close)

class Atualizando(QDialog):
    def __init__(self,janela, parent=None):
        self.con = dao()
        l = self.con.listarUsuarios()
        paraACaixa = []

        for i in range(len(l)):
            paraACaixa.append(str(l[i].indice))
        print(paraACaixa)

        self.msg = QInputDialog.getItem(None, 'Consulta por indice', 'Selecione o indice: ', paraACaixa, 1, True)
        print(self.msg[0])

        janela.ultimaAçao.setText("Ultima açao: Atualizou usuario")

        if self.msg[1] == True:
            volta = self.con.retornarUmUsuario(self.msg[0])
            print(volta)

            if volta == False:
                msg = QMessageBox.warning(None, "Resultado",
                                          "Nao ha cadastros com este indice!", QMessageBox.Close)
            else:

                super(Atualizando, self).__init__()

                lbl = QLabel("Altere como o ID {} quiser:".format(self.msg[0]))

                lblEmail = QLabel("Email: ")
                self.campoEmail = QLineEdit(volta.email)

                lblSenha = QLabel("Senha: ")
                self.campoSenha = QLineEdit(volta.senha)

                botaoSalvar = QPushButton("Salvar")

                camposDeEmails = QHBoxLayout()
                camposDeEmails.addWidget(lblEmail)
                camposDeEmails.addWidget(self.campoEmail)

                camposDeSenha = QHBoxLayout()
                camposDeSenha.addWidget(lblSenha)
                camposDeSenha.addWidget(self.campoSenha)

                vbox = QVBoxLayout()
                vbox.addWidget(lbl)
                vbox.addLayout(camposDeEmails)
                vbox.addLayout(camposDeSenha)
                vbox.addWidget(botaoSalvar)

                self.connect(botaoSalvar, SIGNAL("clicked()"), self.salvar)

                self.setLayout(vbox)
                self.setWindowTitle("Alterar email")
                self.setGeometry(500, 300, 300, 100)
                self.exec_()

    def salvar(self):

        print("Salvando...")
        print(self.campoEmail.displayText())
        if self.campoSenha.displayText() == "" or self.campoEmail.displayText() == "":
            msg = QMessageBox.warning(self, "Alerta",
                                      "Preencha todos os campos!", QMessageBox.Close)
        else:
            msg = QMessageBox.question(self, "Confirmaçao",
                                       "Deseja atualizar para?\n\nEmail: {}\nSenha: {}".format(
                                           self.campoEmail.displayText(), self.campoSenha.displayText()),
                                       QMessageBox.Yes | QMessageBox.No)
            if msg == 16384:
                print("Cadastrou!")
                novo = self.con.atualizarUsuario(self.msg[0], self.campoEmail.displayText(), self.campoSenha.displayText())

                if novo == False:
                    msg = QMessageBox.information(self, "Informaçao",
                                                  "Falha no cadastro!", QMessageBox.Close)
                else:
                    print("\n\nSucesso ao adicionar!")
                    print("ID: {} - Email: {} - Senha: {}".format(novo.indice, novo.email, novo.senha))
                    msg = QMessageBox.information(self, "Sucesso!",
                                                  "Cadastro efetuado:"
                                                  "\n\nID: {}"
                                                  "\nEmail: {}"
                                                  "\nSenha: {}".format(novo.indice, novo.email, novo.senha),
                                                  QMessageBox.Close)
                    self.close()

class Deletar:
    def __init__(self, janela):
        self.con = dao()
        l = self.con.listarUsuarios()
        paraACaixa = []

        for i in range(len(l)):
            paraACaixa.append(str(l[i].indice))
        print(paraACaixa)

        janela.ultimaAçao.setText("Ultima açao: Deletou usuario")

        self.msg = QInputDialog.getItem(None, 'Consulta por indice', 'Selecione o indice: ', paraACaixa, 1, True)
        print(self.msg[0])

        if self.msg[1] == True:
            volta = self.con.retornarUmUsuario(self.msg[0])
            print(volta)

            if volta == False:
                msg = QMessageBox.warning(None, "Resultado",
                                          "Nao ha cadastros com este indice!", QMessageBox.Close)
            else:
                msg = QMessageBox.question(None, "Confirmaçao",
                                           "Deseja deletar este cadastro?\n\nID: {}\nEmail: {}\nSenha: {}".format(
                                               volta.indice, volta.email, volta.senha),
                                           QMessageBox.Yes | QMessageBox.No)
                if msg == 16384:
                    print("Deletou!")
                    excluso = self.con.deletarUsuario(volta.indice)

                    if excluso == False:
                        msg = QMessageBox.information(None, "Informaçao",
                                                      "Falha na exclusao!", QMessageBox.Close)
                    else:
                        print("\n\nSucesso ao deletar!")
                        print("ID: {} - Email: {} - Senha: {}".format(excluso.indice, excluso.email, excluso.senha))
                        msg = QMessageBox.information(None, "Resultado!",
                                                      "Cadastro deletado:"
                                                      "\n\nID: {}"
                                                      "\nEmail: {}"
                                                      "\nSenha: {}".format(excluso.indice, excluso.email, excluso.senha),
                                                      QMessageBox.Close)
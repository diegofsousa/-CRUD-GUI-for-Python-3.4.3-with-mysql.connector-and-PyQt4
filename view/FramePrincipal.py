import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from ProjetoCRUD.view.FrameFuncional import *

class JanelaInicial(QWidget):
    def __init__(self):
        super(JanelaInicial, self).__init__()

        versao = dao()
        versao = versao.versão()

        self.ultimaAçao = QLabel("Versão do conector: {}".format(versao))

        botaoListar = QPushButton("Listar")
        botaoCadastrar = QPushButton("Cadastrar")
        botaoConsultar = QPushButton("Consultar")
        botaoAtualizar = QPushButton("Atualizar")
        botaoDeletar = QPushButton("Deletar")
        botaoSair = QPushButton("Sair")

        hbox = QVBoxLayout()
        hbox.addWidget(self.ultimaAçao)
        hbox.addWidget(botaoListar)
        hbox.addWidget(botaoCadastrar)
        hbox.addWidget(botaoConsultar)
        hbox.addWidget(botaoAtualizar)
        hbox.addWidget(botaoDeletar)
        hbox.addWidget(botaoSair)

        self.connect(botaoListar, SIGNAL("clicked()"), self.lista)
        self.connect(botaoCadastrar, SIGNAL("clicked()"), self.cadastra)
        self.connect(botaoConsultar, SIGNAL("clicked()"), self.consulta)
        self.connect(botaoAtualizar, SIGNAL("clicked()"), self.atualiza)
        self.connect(botaoDeletar, SIGNAL("clicked()"), self.deleta)
        self.connect(botaoSair, SIGNAL("clicked()"), self.destroy)

        self.setGeometry(300, 300, 300, 200)
        self.setMinimumSize(400,300)
        self.setMaximumSize(500, 300)
        self.setLayout(hbox)
        self.setWindowTitle("ProjetoCRUD")
        self.show()

    def lista(self):
        print("Listando...")
        ex = Listando(self, self)
        ex.setModal(True)
        ex.show()

    def cadastra(self):
        print("Cadastrando...")
        ex = Cadastrando(self, self)
        ex.setModal(True)
        ex.show()

    def consulta(self):
        Consultando(self)
        print("Consultando...")

    def atualiza(self):
        print("Atualizando...")
        Atualizando(self)

    def deleta(self):
        print("Deletando...")
        Deletar(self)


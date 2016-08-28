class Usuarios:
    def __init__(self, indice, email, senha):
        self._indice = indice
        self._email = email
        self._senha = senha

    @property  # este é um get
    def indice(self):
        return self._indice
    @property
    def email(self):
        return self._email
    @property
    def senha(self):
        return self._senha

    @email.setter
    def email(self, email):
        self._email = email
    @senha.setter
    def senha(self, senha):
        self._senha = senha




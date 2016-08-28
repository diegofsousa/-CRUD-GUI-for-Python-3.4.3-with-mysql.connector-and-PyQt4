from ProjetoCRUD.view.FramePrincipal import JanelaInicial
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

def main():
    app = QApplication(sys.argv)
    ex = JanelaInicial()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
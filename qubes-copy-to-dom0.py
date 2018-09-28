from PyQt5 import QtWidgets
from ui.main import mainwin

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = mainwin()
    ui.show()
    sys.exit(app.exec_())

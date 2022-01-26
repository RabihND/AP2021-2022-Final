from PyQt5 import QtCore, QtGui, QtWidgets
from mastermind import MasterMind
from gameoverwindow import GameOverWindow
from mainwindow  import MainWindowUi

if __name__ == "__main__":
    import sys
    mastermind = MasterMind()
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MainWindowUi(mastermind)
    ui.setupUi(MainWindow, mastermind)
    MainWindow.show()
    sys.exit(app.exec_())

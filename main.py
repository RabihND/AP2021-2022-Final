#Import Part
#
from mastermind import MasterMind

class MainWindow:
    """The main window of the game designed by qt"""
    pass

class GameOverWindow:
    """The resulting window, which shows the player's loss(+) or victory(-)"""
    pass

if __name__ == "__main__":
    import sys
    mastermind = Mastermind()
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow(mastermind)
    ui.setupUi(MainWindow, mastermind)
    MainWindow.show()
    sys.exit(app.exec_())





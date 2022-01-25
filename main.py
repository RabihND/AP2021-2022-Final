#Import Part
from PyQt5 import QtCore, QtGui, QtWidgets
from mastermind import MasterMind


class MainWindow(object):
    """The main window of the game designed by qt"""
    def __init__(self, MastermindObj):
        self.selectedColors = []
        self.tries = 0
        self.mastermind = MastermindObj
        self.mastermind.get_random_solution()

    def setupUi(self, MainWindow, MastermindObj):
        self.__init__(MastermindObj)
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(450, 800)
        MainWindow.setFixedSize(450, 800)

        #Main Window Icon
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("pngegg.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)

        #Central widget
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        #Submit Button (design)
        self.submitButton = QtWidgets.QPushButton(self.centralwidget)
        self.submitButton.setGeometry(QtCore.QRect(75, 700, 300, 60))
        self.submitButton.setAcceptDrops(False)
        self.submitButton.setObjectName("submitButton")

        #Old Guess Table
        self.oldGuessesTable = QtWidgets.QTableWidget(self.centralwidget)
        self.oldGuessesTable.setEnabled(False)
        self.oldGuessesTable.setGeometry(QtCore.QRect(10, 10, 200, 500))
        self.oldGuessesTable.setMaximumSize(QtCore.QSize(16777215, 16777213))
        self.oldGuessesTable.setBaseSize(QtCore.QSize(4, 10))
        self.oldGuessesTable.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.oldGuessesTable.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.oldGuessesTable.setAutoScroll(False)
        self.oldGuessesTable.setWordWrap(False)
        self.oldGuessesTable.setCornerButtonEnabled(False)
        self.oldGuessesTable.setObjectName("oldGuessesTable")
        self.oldGuessesTable.setColumnCount(4)
        self.oldGuessesTable.setRowCount(10)
        self.oldGuessesTable.horizontalHeader().setVisible(False)
        self.oldGuessesTable.horizontalHeader().setDefaultSectionSize(50)
        self.oldGuessesTable.horizontalHeader().setMinimumSectionSize(0)
        self.oldGuessesTable.verticalHeader().setVisible(False)
        self.oldGuessesTable.verticalHeader().setCascadingSectionResizes(False)
        self.oldGuessesTable.verticalHeader().setDefaultSectionSize(50)
        self.oldGuessesTable.verticalHeader().setMinimumSectionSize(0)

class GameOverWindow:
    """The resulting window, which shows the player's loss(+) or victory(-)"""
    pass






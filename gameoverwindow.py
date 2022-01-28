from PyQt5 import QtCore, QtWidgets


class GameOverWindow(QtWidgets.QDialog):
    """The resulting window, which shows the player's loss(+) or victory(-)"""
    def __init__(self, text):
        super(GameOverWindow, self).__init__()
        self.text = text
        

    def setupUi(self, GameOverWindow):
        GameOverWindow.setObjectName("GAME OVER")
        GameOverWindow.resize(268, 142)
        GameOverWindow.setFixedSize(268, 142)
        self.buttonBox = QtWidgets.QDialogButtonBox(GameOverWindow)
        self.buttonBox.setGeometry(QtCore.QRect(-120, 110, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(GameOverWindow)
        self.label.setGeometry(QtCore.QRect(70, -10, 171, 111))
        self.label.setObjectName("label")

        self.retranslateUi(GameOverWindow)
        self.buttonBox.accepted.connect(GameOverWindow.accept)
        self.buttonBox.rejected.connect(GameOverWindow.reject)
        QtCore.QMetaObject.connectSlotsByName(GameOverWindow)

        self.display_text()

    def display_text(self):
            self.label.setText("You " + self.text + " the game. \nWant to try again?")
            self.label.setStyleSheet("font-family: Kristen ITC;\n"
                                                "font-size: 10pt;\n"
                                                "font-weight: normal;")

    def retranslateUi(self, gameoverDialog):
            _translate = QtCore.QCoreApplication.translate
            gameoverDialog.setWindowTitle( _translate("GAME OVER", "Game over"))
            self.label.setText(_translate("GAMEOVER", "You Won !!. \nWant to try again?"))
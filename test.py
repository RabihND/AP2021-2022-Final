
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_gameoverDialog(QtWidgets.QDialog):
    def __init__(self, text):
        super(Ui_gameoverDialog, self).__init__()
        self.text = text
        

    def setupUi(self, gameoverDialog):
        gameoverDialog.setObjectName("gameoverDialog")
        gameoverDialog.resize(268, 142)
        gameoverDialog.setFixedSize(268, 142)
        self.buttonBox = QtWidgets.QDialogButtonBox(gameoverDialog)
        self.buttonBox.setGeometry(QtCore.QRect(-120, 110, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(
            QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(gameoverDialog)
        self.label.setGeometry(QtCore.QRect(70, -10, 160, 100))
        self.label.setObjectName("label")


        self.retranslateUi(gameoverDialog)
        self.buttonBox.accepted.connect(gameoverDialog.accept)
        self.buttonBox.rejected.connect(gameoverDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(gameoverDialog)

        self.display_text()

    def display_text(self):
        self.label.setText("You " + self.text + " the game. \n"
                           "Want to try again?")
        self.label.setStyleSheet("font-family: Kristen ITC;\n"
                                       "font-size: 10pt;\n"
                                       "font-weight: normal;")

    def retranslateUi(self, gameoverDialog):
        _translate = QtCore.QCoreApplication.translate
        gameoverDialog.setWindowTitle(
            _translate("gameoverDialog", "Game over"))
        self.label.setText(_translate("gameoverDialog", "You won the game. \n"
                                      "Want to try again?"))

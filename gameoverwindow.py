from PyQt5 import QtCore, QtGui, QtWidgets


class GameOverWindow(QtWidgets.QDialog):
    def __init__(self, text):
        super(GameOverWindow, self).__init__()
        self.text = text
        

    def setupUi(self, GameOverWindow):
        GameOverWindow.setObjectName("gameoverDialog")
        GameOverWindow.resize(268, 142)
        GameOverWindow.setFixedSize(268, 142)
        self.buttonBox = QtWidgets.QDialogButtonBox(GameOverWindow)
        self.buttonBox.setGeometry(QtCore.QRect(-120, 110, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(
            QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(GameOverWindow)
        self.label.setGeometry(QtCore.QRect(70, -10, 171, 111))
        self.label.setObjectName("label")

        self.retranslateUi(GameOverWindow)
        self.buttonBox.accepted.connect(GameOverWindow.accept)
        self.buttonBox.rejected.connect(GameOverWindow.reject)
        QtCore.QMetaObject.connectSlotsByName(GameOverWindow)

        self.display_text()
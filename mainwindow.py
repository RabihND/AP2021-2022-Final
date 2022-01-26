#Import Part
from PyQt5 import QtCore, QtGui, QtWidgets
from mastermind import MasterMind
from gameoverwindow import GameOverWindow


class MainWindow(object):
    """The main window of the game designed by Qt"""
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
        self.submitButton.setGeometry(QtCore.QRect(75, 760, 300, 60))
        self.submitButton.setAcceptDrops(False)
        self.submitButton.setObjectName("submitButton")
        self.submitButton.setStyleSheet("font-family: Kristen ITC;\n"
                                       "font-size: 7pt;\n"
                                       "font-weight: bold;")

        #Old Guess Table
        self.oldGuessesTable = QtWidgets.QTableWidget(self.centralwidget)
        self.oldGuessesTable.setEnabled(False)
        self.oldGuessesTable.setGeometry(QtCore.QRect(10, 80, 200, 500))
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
        self.oldGuessesTable.setStyleSheet("	background-color: rgb(157, 191, 199);	\n"
                                           "	color: rgb(220, 220, 220);\n"
                                           "	border-radius: 10px;\n")

        # Color Table
        self.colorsTable = QtWidgets.QTableWidget(self.centralwidget)
        self.colorsTable.setGeometry(QtCore.QRect(75, 700, 300, 50))
        self.colorsTable.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.colorsTable.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.colorsTable.setRowCount(1)
        self.colorsTable.setColumnCount(6)
        self.colorsTable.setObjectName("colorsTable")
        #->Color 1: [0]
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setBackground(brush)
        item.setFlags(QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.colorsTable.setItem(0, 0, item)
        #->Color 2: [1]
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(153, 0, 204,127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setBackground(brush)
        item.setFlags(QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.colorsTable.setItem(0, 1, item)
        #->Color 3: [2]
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(255, 128, 0,180))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setBackground(brush)
        item.setFlags(QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.colorsTable.setItem(0, 2, item)
        #->Color 4: [3]
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(255, 26, 26,200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setBackground(brush)
        item.setFlags(QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.colorsTable.setItem(0, 3, item)
        #->Color 5: [4]
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 26, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setBackground(brush)
        item.setFlags(QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.colorsTable.setItem(0, 4, item)
        #->Color 6: [5]
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(0, 204, 0, 180))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setBackground(brush)
        item.setFlags(QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.colorsTable.setItem(0, 5, item)
        self.colorsTable.horizontalHeader().setVisible(False)
        self.colorsTable.horizontalHeader().setDefaultSectionSize(50)
        self.colorsTable.verticalHeader().setVisible(False)
        self.colorsTable.verticalHeader().setDefaultSectionSize(50)

        #Currently Guess Table
        self.thisGuessTable = QtWidgets.QTableWidget(self.centralwidget)
        self.thisGuessTable.setGeometry(QtCore.QRect(10, 600, 200, 50))
        self.thisGuessTable.setAcceptDrops(True)
        self.thisGuessTable.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.thisGuessTable.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.thisGuessTable.setRowCount(1)
        self.thisGuessTable.setColumnCount(4)
        self.thisGuessTable.setObjectName("thisGuessTable")
        self.set_thisguesstable()
        self.thisGuessTable.horizontalHeader().setVisible(False)
        self.thisGuessTable.horizontalHeader().setDefaultSectionSize(50)
        self.thisGuessTable.verticalHeader().setVisible(False)
        self.thisGuessTable.verticalHeader().setDefaultSectionSize(50)
        MainWindow.setCentralWidget(self.centralwidget)
        self.thisGuessTable.setStyleSheet("	background-color: rgb(255, 255, 255);	\n"
                                                             "	color: rgb(220, 220, 220);\n"
                                                            "	border-radius: 10px;\n")

        # Status Bar (For the AI Solver)
        # self.statusbar = QtWidgets.QStatusBar(MainWindow)
        # self.statusbar.setObjectName("statusbar")
        # MainWindow.setStatusBar(self.statusbar)
        # self.statusbar.setSizeGripEnabled(False)

        #Score Table
        self.scoreTable = QtWidgets.QTableWidget(self.centralwidget)
        self.scoreTable.setEnabled(False)
        self.scoreTable.setGeometry(QtCore.QRect(242, 80, 195, 500))
        self.scoreTable.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scoreTable.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scoreTable.setWordWrap(False)
        self.scoreTable.setCornerButtonEnabled(False)
        self.scoreTable.setRowCount(10)
        self.scoreTable.setColumnCount(4)
        self.scoreTable.setObjectName("scoreTable")
        self.scoreTable.horizontalHeader().setVisible(False)
        self.scoreTable.horizontalHeader().setDefaultSectionSize(10)
        self.scoreTable.verticalHeader().setVisible(False)
        self.scoreTable.verticalHeader().setDefaultSectionSize(50)
        self.scoreTable.setStyleSheet("	background-color: rgb(56, 100, 89);	\n"
                                                      "	color: rgb(220, 220, 220);\n"
                                                      "	border-radius: 10px;\n")

        #ResetButton
        self.resetButton = QtWidgets.QPushButton(self.centralwidget)
        self.resetButton.setGeometry(QtCore.QRect(242, 600, 200, 50))
        self.resetButton.setObjectName("resetButton")
        self.resetButton.clicked.connect(self.resetButtonClicked)
        self.resetButton.setStyleSheet("font-family: Kristen ITC;\n"
                                                        "font-size: 7pt;\n"
                                                        "font-weight: bold;")

        self.retranslateUi(MainWindow)
        self.colorsTable.cellClicked['int','int'].connect(self.clicked_color)

        #Submit Button
        self.submitButton.clicked.connect(self.clicked_submit)

        #Tries Label
        self.triesLeft = QtWidgets.QLabel(self.centralwidget)
        self.triesLeft.setGeometry(QtCore.QRect(133, 645, 300, 60))
        self.triesLeft.setText("Attempts Left = 10")
        self.triesLeft.setStyleSheet("color: white;\n"
                                                  "font-size: 12pt;\n"
                                                  "font-family: Kristen ITC;\n"
                                                  "text-align: center;")

        # ScoreTable Label
        self.scorelabel = QtWidgets.QLabel(self.centralwidget)
        self.scorelabel.setGeometry(QtCore.QRect(280, 30, 300, 60))
        self.scorelabel.setText("Score Table")
        self.scorelabel.setStyleSheet("color: white;\n"
                                                      "font-size: 12pt;\n"
                                                      "font-family: Kristen ITC;\n"
                                                      "text-align: center;\n")
    
    def resetButtonClicked(self):
        self.selectedColors = []
        self.set_thisguesstable()

    def set_thisguesstable(self):
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsDropEnabled)
        self.thisGuessTable.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsDropEnabled)
        self.thisGuessTable.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsDropEnabled)
        self.thisGuessTable.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsDropEnabled)
        self.thisGuessTable.setItem(0, 3, item)

    def clicked_color(self, row, col):
        if len(self.selectedColors) >= 4:
            return
        self.selectedColors.append(col)

        item = self.thisGuessTable.item(0, len(self.selectedColors)-1)
        color = self.colorsTable.item(row,col).background().color()
        brush = QtGui.QBrush(color)
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setBackground(brush)

    def clicked_submit(self):
        if len(self.selectedColors) != 4:
            return
        print(f"Trie {self.tries + 1} - {9 - self.tries} left")
        # print('─' * 10)  # U+2501, Box Drawings Heavy Horizontal
        print('_' * 10)  # Underscore
        print("Selected Colors:",self.selectedColors)
        self.triesLeft.setText(f"Attempts Left =  {9 - self.tries}")
        for col in range(4):
            color = self.thisGuessTable.item(0,col).background().color()
            brush = QtGui.QBrush(color)
            brush.setStyle(QtCore.Qt.SolidPattern)
            item = QtWidgets.QTableWidgetItem()
            item.setBackground(brush) 
            self.oldGuessesTable.setItem(self.tries, col, item)

        correct, misplaced = self.mastermind.check_guess(self.selectedColors)
        self.print_score(correct, misplaced)

        self.selectedColors = []
        self.tries += 1
        self.set_thisguesstable()

        if correct == 4:
            self.colorsTable.setEnabled(False)
            self.show_game_over("won")
        elif self.tries == 10:
            self.colorsTable.setEnabled(False)
            self.show_game_over("lost")
            # game lost

    def show_game_over(self, text):
        Dialog = QtWidgets.QDialog(self.centralwidget)
        ui = GameOverWindow(text)
        ui.setupUi(Dialog)
        #Dialog.show()
        choice = Dialog.exec_()

        if choice == QtWidgets.QDialog.Accepted:
            self.setupUi(MainWindow, mastermind)
            pass
        else:
            pass

    def print_score(self, correct, misplaced):
        for col in range(4):
            if correct:
                correct -= 1
                brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
                brush.setStyle(QtCore.Qt.SolidPattern)
                item = QtWidgets.QTableWidgetItem()
                item.setBackground(brush) 
                self.scoreTable.setItem(self.tries, col, item)
            elif misplaced:
                misplaced -=1
                brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
                brush.setStyle(QtCore.Qt.SolidPattern)
                item = QtWidgets.QTableWidgetItem()
                item.setBackground(brush) 
                self.scoreTable.setItem(self.tries, col, item)
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Mastermind"))
        self.submitButton.setText(_translate("MainWindow", "Submit"))
        __sortingEnabled = self.colorsTable.isSortingEnabled()
        self.colorsTable.setSortingEnabled(False)
        self.colorsTable.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.thisGuessTable.isSortingEnabled()
        self.thisGuessTable.setSortingEnabled(False)
        self.thisGuessTable.setSortingEnabled(__sortingEnabled)
        self.resetButton.setText(_translate("MainWindow", "Reset"))









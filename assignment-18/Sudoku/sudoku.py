from random import *
from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *

class Sudoko(QMainWindow):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load('form.ui',None)
        self.flag = 0
        self.f = 0
        self.game = [[None for i in range(9)]for j in range(9)]
        
        for i in range(9):
            for j in range(9):
                self.txtbox = QLineEdit()
                self.txtbox.setStyleSheet('font-size: 26px')
                self.game[i][j] = self.txtbox
                self.ui.gridLayout.addWidget(self.txtbox,i,j)
                self.game[i][j].setAlignment(Qt.AlignCenter)
                self.txtbox.textChanged.connect(self.CheckGame)
                
        self.ui.show()
        self.ui.newgame.clicked.connect(self.NewGame)   
        self.ui.checkgame.clicked.connect(self.CheckGame)
        self.ui.dark_mode_2.clicked.connect(self.DarkMode)


    def NewGame(self):
        for i in range(9):
            for j in range(9):
                self.game[i][j].setText('')

        rand = randint(1,6)

        try:
            file_path = f"data/s{rand}.txt"
            f = open(file_path , 'r')
            hyper_text = f.read()
            rows = hyper_text.split('\n')

            for i in range(9):
                numbers = rows[i].split(' ')
                for j in range(9):
                    if numbers[j] != '0' :
                        self.game[i][j].setText(numbers[j])
                        self.game[i][j].setReadOnly(True)
                        if self.flag == 0:
                            self.game[i][j].setStyleSheet('font-size: 26px ; color : black')
                        else:
                            self.game[i][j].setStyleSheet('font-size: 26px ; color : white')
                    else:
                        self.game[i][j].setReadOnly(False)
                        self.game[i][j].setStyleSheet('font-size: 26px ; color : blue')
        except:
            print('error')
            rand = randint(1,6)

    def CheckGame(self):

        self.fwin = False

        for row in range(9):
            for col in range(9):
                for i in range(9):
                    for j in range(9):
                        if self.game[row][i].text() == self.game[row][j].text() and i != j and self.game[row][i].text() != '' :
                            self.game[row][i].setStyleSheet('font-size: 26px ; background-color : pink')        
                            self.fwin == False             
                        elif self.game[i][col].text() == self.game[j][col].text() and i != j and self.game[i][col].text() != '':
                            self.game[i][col].setStyleSheet('font-size: 26px ; background-color : pink')     
                            self.fwin == False               
                                             
        for row in range(3):
            for col in range(3):
                for i in range(3):
                    for j in range(3):
                        if self.game[row][i].text() == self.game[row][j].text() and i != j and self.game[row][i].text() != '':
                            self.game[row][i].setStyleSheet('font-size: 26px ; background-color : pink')
                            self.fwin == False
                        elif self.game[i][col].text() == self.game[j][col].text() and i != j and self.game[i][col].text() != '':
                            self.game[i][col].setStyleSheet('font-size: 26px ; background-color : pink')
                            self.fwin == False
                        elif self.game[row][col].text() == self.game[i][j].text() and row!= i and col!= j and self.game[row][col].text() != '':
                            self.game[i][j].setStyleSheet('font-size: 26px ; background-color : pink')
                            self.fwin == False

        for row in range(3,6):
            for col in range(3,6):
                for i in range(3,6):
                    for j in range(3,6):
                        if self.game[row][i].text() == self.game[row][j].text() and i != j and self.game[row][i].text() != '':
                            self.game[row][i].setStyleSheet('font-size: 26px ; background-color : pink')
                            self.fwin == False
                        elif self.game[i][col].text() == self.game[j][col].text() and i != j and self.game[i][col].text() != '':
                            self.game[i][col].setStyleSheet('font-size: 26px ; background-color : pink')
                            self.fwin == False
                        elif self.game[row][col].text() == self.game[i][j].text() and row!= i and col!= j and self.game[row][col].text() != '':
                            self.game[i][j].setStyleSheet('font-size: 26px ; background-color : pink')
                            self.fwin == False
        
        for row in range(6,9):
            for col in range(6,9):
                for i in range(6,9):
                    for j in range(6,9):
                        if self.game[row][i].text() == self.game[row][j].text() and i != j and self.game[row][i].text() != '':
                            self.game[row][i].setStyleSheet('font-size: 26px ; background-color : pink')
                            self.fwin == False
                        elif self.game[i][col].text() == self.game[j][col].text() and i != j and self.game[i][col].text() != '':
                            self.game[i][col].setStyleSheet('font-size: 26px ; background-color : pink')
                            self.fwin == False
                        elif self.game[row][col].text() == self.game[i][j].text() and row!= i and col!= j and self.game[row][col].text() != '':
                            self.game[i][j].setStyleSheet('font-size: 26px ; background-color : pink')
                            self.fwin == False

        for row in range(3,6):
            for col in range(3):
                for i in range(3,6):
                    for j in range(3):
                        if self.game[row][col].text() == self.game[i][j].text() and row!= i and col!= j and self.game[row][col].text() != '':
                            self.game[i][j].setStyleSheet('font-size: 26px ; background-color : pink')    
                            self.fwin == False

        for row in range(6,9):
            for col in range(3):
                for i in range(6,9):
                    for j in range(3):
                        if self.game[row][col].text() == self.game[i][j].text() and row!= i and col!= j and self.game[row][col].text() != '':
                            self.game[i][j].setStyleSheet('font-size: 26px ; background-color : pink')
                            self.fwin == False 
        
        for row in range(3):
            for col in range(3,6):
                for i in range(3):
                    for j in range(3,6):
                        if self.game[row][col].text() == self.game[i][j].text() and row!= i and col!= j and self.game[row][col].text() != '':
                            self.game[i][j].setStyleSheet('font-size: 26px ; background-color : pink')
                            self.fwin == False
        
        for row in range(6,9):
            for col in range(3,6):
                for i in range(6,9):
                    for j in range(3,6):
                        if self.game[row][col].text() == self.game[i][j].text() and row!= i and col!= j and self.game[row][col].text() != '':
                            self.game[i][j].setStyleSheet('font-size: 26px ; background-color : pink')
                            self.fwin == False
        
        for row in range(3,6):
            for col in range(6,9):
                for i in range(3,6):
                    for j in range(6,9):
                        if self.game[row][col].text() == self.game[i][j].text() and row!= i and col!= j and self.game[row][col].text() != '':
                            self.game[i][j].setStyleSheet('font-size: 26px ; background-color : pink')
                            self.fwin == False
        
        for row in range(3):
            for col in range(6,9):
                for i in range(3):
                    for j in range(6,9):
                        if self.game[row][col].text() == self.game[i][j].text() and row!= i and col!= j and self.game[row][col].text() != '':
                            self.game[i][j].setStyleSheet('font-size: 26px ; background-color : pink')
                            self.fwin == False

        for i in range(9):
            for j in range(9):
                if self.game[i][j].text() != '':
                    self.fwin == True 

        if self.fwin == True:
            winingbox = QMessageBox()
            winingbox.setText('Congrats 😍')
            winingbox.exec()

    def DarkMode(self):
        if self.flag == 0 :
            self.ui.setStyleSheet('background-color : black')
            self.ui.checkgame.setStyleSheet('background-color : white')
            self.ui.newgame.setStyleSheet('background-color : white')
            self.ui.dark_mode_2.setStyleSheet('background-color : white')
            for i in range(9):
                    for j in range(9):
                        self.game[i][j].setStyleSheet('font-size: 26px ; color : white')
            self.flag = 1
        else :
            self.ui.setStyleSheet('background-color : white')
            for i in range(9):
                    for j in range(9):
                        self.game[i][j].setStyleSheet('font-size: 26px ; color : black')
            self.flag = 0

app = QApplication([])
window = Sudoko()

app.exec()
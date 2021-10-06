from random import *
from functools import partial
from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *

class TicTacToe(QMainWindow):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load('xo.ui',None)
        self.ui.show()
        self.ui.newgame.clicked.connect(self.new_game)
        self.ui.info.clicked.connect(self.game_info)
        self.ui.two_players.setChecked(True)
        self.sign = choice(['X', 'O'])
        self.xscore = 0
        self.oscore = 0
        self.flagx = 0
        self.flago = 0
               
        self.game = [[self.ui.btn1,self.ui.btn2,self.ui.btn3],
                    [self.ui.btn4,self.ui.btn5,self.ui.btn6],
                    [self.ui.btn7,self.ui.btn8,self.ui.btn9]]

        for i in range(3):
            for j in range(3):
                self.game[i][j].clicked.connect(partial(self.play,i,j))
    
    def play(self,i,j):

        if self.ui.two_players.isChecked() and self.game[i][j].text()== "":
            self.playersign(i,j)

        elif self.ui.single_player.isChecked() and self.game[i][j].text()== "": 
            self.playersign(i,j)
            self.pc_player()            
       
    def pc_player(self):
        while True:
            randi = randint(0, 2)
            randj = randint(0, 2)
            if self.game[randi][randj].text()=='':
                break 
        self.playersign(randi,randj)
     
    def new_game(self):
        self.flagx = 0
        self.flago = 0
        self.randcolor = choice(['pink','orange', 'lightblue'])
        self.refresh()

    def game_info(self):
        msgBox = QMessageBox()
        msgBox.setText('XO game\nmade by Mahdis\nversion 1.0')
        msgBox.exec()

    def refresh(self):
        for i in range(3):
                for j in range(3):
                    self.game[i][j].setText('')
                    self.game[i][j].setStyleSheet(f'background-color : {self.randcolor} ; border-radius: 12px')

    def playersign(self,x,y):
        self.game[x][y].setText(self.sign)
        if self.sign == 'X':
            self.sign = 'O'
            self.game[x][y].setStyleSheet('color : red')
        else:
            self.sign = 'X'
            self.game[x][y].setStyleSheet('color : blue') 

        self.check()
    def messgbox(self,x):
        msgBox = QMessageBox()
        msgBox.setText(x)
        msgBox.exec()               

    def check(self):
        self.randcolor = choice(['pink','orange', 'lightblue'])
        if  self.game[0][0].text() == 'X' and self.game[1][1].text() == 'X' and self.game[2][2].text() == 'X' or self.game[0][2].text() == 'X' and self.game[1][1].text() == 'X' and self.game[2][0].text() == 'X':
            self.messgbox('Player X wins')
            self.xscore+=1
            self.ui.xscore.setText(str(f"X : {self.xscore}"))
            self.refresh()

        elif self.game[0][2].text() == 'O' and self.game[1][1].text() == 'O' and self.game[2][0].text() == 'O' or self.game[0][0].text() == 'O' and self.game[1][1].text() == 'O' and self.game[2][2].text() == 'O' :
            self.messgbox('Player O wins')
            self.oscore+=1
            self.ui.oscore.setText(str(f"O : {self.oscore}"))
            self.refresh()

        elif ((self.game[0][0].text() == 'X' and self.game[1][0].text() == 'X' and self.game[2][0].text() == 'X') or (self.game[0][1].text() == 'X' and self.game[1][1].text() == 'X' and self.game[2][1].text() == 'X') or (self.game[0][2].text() == 'X' and self.game[1][2].text() == 'X' and self.game[2][2].text() == 'X') or (self.game[0][0].text() == 'X' and self.game[0][1].text() == 'X' and self.game[0][2].text() == 'X') or (self.game[1][0].text() == 'X' and self.game[1][1].text() == 'X' and self.game[1][2].text() == 'X') or (self.game[2][0].text() == 'X' and self.game[2][1].text() == 'X' and self.game[2][2].text() == 'X')) and self.flagx == 0:
            self.messgbox('Player X wins')
            self.xscore+=1
            self.ui.xscore.setText(str(f"X : {self.xscore}"))
            self.flagx = 1
            

        elif ((self.game[0][0].text() == 'O' and self.game[0][1].text() == 'O' and self.game[0][2].text() == 'O') or (self.game[1][0].text() == 'O' and self.game[1][1].text() == 'O' and self.game[1][2].text() == 'O') or (self.game[2][0].text() == 'O' and self.game[2][1].text() == 'O' and self.game[2][2].text() == 'O') or (self.game[0][0].text() == 'O' and self.game[1][0].text() == 'O' and self.game[2][0].text() == 'O') or (self.game[0][1].text() == 'O' and self.game[1][1].text() == 'O' and self.game[2][1].text() == 'O') or (self.game[0][2].text() == 'O' and self.game[1][2].text() == 'O' and self.game[2][2].text() == 'O')) and self.flago == 0:
            self.messgbox('Player O wins')
            self.oscore+=1
            self.ui.oscore.setText(str(f"O : {self.oscore}"))
            self.flago = 1
             
        if self.flagx == 1 and self.flago == 1:
            self.messgbox('Win-Win')
            self.refresh()
            self.flagx = 0
            self.flago = 0
        
        if self.game[0][0].text()!= '' and self.game[1][0].text()!= '' and self.game[2][0].text()!= '' and  self.game[1][1].text()!= '' and self.game[2][2].text()!= '' and self.game[0][1].text()!= '' and self.game[1][2].text()!= '' and self.game[2][1].text()!= '' and self.game[0][2].text()!= '':
            self.refresh()
            self.flagx = 0
            self.flago = 0
                   
app = QApplication([])
window = TicTacToe()

app.exec()
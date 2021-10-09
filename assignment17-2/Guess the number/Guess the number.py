from random import *
from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *

class NumberGuess(QMainWindow):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load('guessnum.ui',None)
        self.ui.show()
        self.ui.label_3.setStyleSheet("image : url(1.png);")
        self.ui.checkbtn.clicked.connect(self.player)
        self.ui.newgame.clicked.connect(self.newgame)
        self.pcnum = randint(0,1000)
        
    def player(self):
        self.randcolor = choice(['white' , 'pink' , 'silver'])

        self.usernum = int(self.ui.textEdit.text())
        self.ui.result1.setStyleSheet(f'color : {self.randcolor} ; font: 800 14pt "Rockwell Extra Bold";')

        if self.usernum == self.pcnum:
            self.ui.result1.setText(f"Hooray congratulations!\n The number was :{self.pcnum}") 

        if self.usernum > self.pcnum:
            self.ui.result1.setText("It's lower") 

        elif self.usernum < self.pcnum: 
            self.ui.result1.setText("It's upper")
        
    def newgame(self):
        self.pcnum = randint(0,1000)

app = QApplication([])
window = NumberGuess()

app.exec()
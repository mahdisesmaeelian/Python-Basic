import math
from sympy import cot
from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *
import sympy

class Calc(QMainWindow):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load("cal.ui", None)
        self.ui.show()

        self.ui.num1.clicked.connect(self.num_1)
        self.ui.num2.clicked.connect(self.num_2)
        self.ui.num3.clicked.connect(self.num_3)
        self.ui.num4.clicked.connect(self.num_4)
        self.ui.num5.clicked.connect(self.num_5)
        self.ui.num6.clicked.connect(self.num_6)
        self.ui.num7.clicked.connect(self.num_7)
        self.ui.num8.clicked.connect(self.num_8)
        self.ui.num9.clicked.connect(self.num_9)
        self.ui.num0.clicked.connect(self.num_0)
        self.ui.sumbtn.clicked.connect(self.numsum)
        self.ui.minbtn.clicked.connect(self.nummin)
        self.ui.eqbtn.clicked.connect(self.numeq)
        self.ui.mulbtn.clicked.connect(self.nummul)
        self.ui.divbtn.clicked.connect(self.numdiv)
        self.ui.dotbtn.clicked.connect(self.numdot)
        self.ui.revbtn.clicked.connect(self.numrev)
        self.ui.clearbtn.clicked.connect(self.numclear)
        self.ui.numtan.clicked.connect(self.numtan)
        self.ui.numsin.clicked.connect(self.numsin)
        self.ui.numcos.clicked.connect(self.numcos)
        self.ui.numrad.clicked.connect(self.numradical)
        self.ui.numfac.clicked.connect(self.numfactorial)
        self.ui.numcot.clicked.connect(self.numcot)

    def num_1(self):
        self.ui.textbox.setText(self.ui.textbox.text()+ '1')
    def num_2(self):
        self.ui.textbox.setText(self.ui.textbox.text()+ '2')
    def num_3(self):
        self.ui.textbox.setText(self.ui.textbox.text()+ '3')
    def num_4(self):
        self.ui.textbox.setText(self.ui.textbox.text()+ '4')
    def num_5(self):
        self.ui.textbox.setText(self.ui.textbox.text()+ '5')
    def num_6(self):
        self.ui.textbox.setText(self.ui.textbox.text()+ '6')
    def num_7(self):
        self.ui.textbox.setText(self.ui.textbox.text()+ '7')
    def num_8(self):
        self.ui.textbox.setText(self.ui.textbox.text()+ '8')
    def num_9(self):
        self.ui.textbox.setText(self.ui.textbox.text()+ '9')
    def num_0(self):
        self.ui.textbox.setText(self.ui.textbox.text()+ '0')
    def numdot(self):
        for i in self.ui.textbox.text():
            if '.' not in self.ui.textbox.text():
                self.ui.textbox.setText(self.ui.textbox.text()+ '.')
        

    def numsum(self):
        self.num1 = float(self.ui.textbox.text())
        self.ui.textbox.setText('')
        self.sign = '+'

    def nummin(self):
        self.num1 = float(self.ui.textbox.text())
        self.ui.textbox.setText('')
        self.sign = '-'
    
    def nummul(self):
        self.num1 = float(self.ui.textbox.text())
        self.ui.textbox.setText('')
        self.sign = '*'

    def numdiv(self):
        self.num1 = float(self.ui.textbox.text())
        self.ui.textbox.setText('')
        self.sign = '/'
    
    def numrev(self):
        self.num1 = float(self.ui.textbox.text())
        reversenum = self.num1 * -1
        self.ui.textbox.setText(str(reversenum))
        
    def numclear(self):
        self.ui.textbox.setText('')
    
    def numtan(self):
        self.num1 = float(self.ui.textbox.text())
        result=math.tan(math.radians(self.num1))
        self.ui.textbox.setText(str(result))

    def numcos(self):
        self.num1 = float(self.ui.textbox.text())
        result=math.cos(math.radians(self.num1))
        self.ui.textbox.setText(str(result))

    def numsin(self):
        self.num1 = float(self.ui.textbox.text())
        result=math.sin(math.radians(self.num1))
        self.ui.textbox.setText(str(result))

    def numcot(self):
        self.num1 = float(self.ui.textbox.text())
        result=cot(math.radians(self.num1))
        self.ui.textbox.setText(str(result))

    def numradical(self):
        self.num1 = float(self.ui.textbox.text())
        result=math.sqrt(self.num1)
        self.ui.textbox.setText(str(result))

    def numfactorial(self):
        self.num1 = float(self.ui.textbox.text())
        result=math.factorial(self.num1)
        self.ui.textbox.setText(str(result))

    def numeq(self):
        self.num2 = float(self.ui.textbox.text())

        if self.sign == '+':
            result = self.num1 + self.num2
        elif self.sign == '-':
            result = self.num1 - self.num2
        elif self.sign == '*':
            result = self.num1 * self.num2
        elif self.sign == '/':
            if self.num2 != 0:
                result = self.num1 / self.num2
            else:
                self.ui.textbox.setText("Can't devided by Zero")

        self.ui.textbox.setText(str(result))
    
app = QApplication([])
window = Calc()

app.exec()
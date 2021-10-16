from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *
from PySide6.QtGui import *

class Converting(QMainWindow):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load('UnitConvertor.ui',None)
        self.ui.show()
        
        self.listItems = ['Length','Weight','Temprature','Data']
        self.weightitems = ['grams','kilograms','tone','pound']
        self.lengthitems = ['milimeters','centimeters','meters','kilometers','inches']
        self.tempitems = ['celsius','farenheit','kelvin']
        self.dataitems = ['bits','bytes','kilobytes','megabytes','gigabytes','terabytes'] 

        self.ui.comboBox.addItems(self.listItems)
        self.Firstboxinfo()
        self.ui.convertbtn.clicked.connect(self.Converter)
        self.ui.comboBox.currentTextChanged.connect(self.onChange)
        
    def Firstboxinfo(self):
        self.ui.comboBox_2.setCurrentText(self.listItems[0])
        self.ui.comboBox_1.addItems(self.lengthitems)
        self.ui.comboBox_2.addItems(self.lengthitems)
        self.ui.comboBox_2.setCurrentText(self.lengthitems[1])
        
    def onChange(self):
        self.ui.comboBox_1.clear()
        self.ui.comboBox_2.clear()

        if self.ui.comboBox.currentText() == "Length":
            self.ui.comboBox_1.addItems(self.lengthitems)
            self.ui.comboBox_2.addItems(self.lengthitems)
            self.ui.comboBox_2.setCurrentText(self.lengthitems[1])

        elif self.ui.comboBox.currentText() == "Weight":
            self.ui.comboBox_1.addItems(self.weightitems)
            self.ui.comboBox_2.addItems(self.weightitems)
            self.ui.comboBox_2.setCurrentText(self.weightitems[1])
            
        elif self.ui.comboBox.currentText() == "Temprature":
            self.ui.comboBox_1.addItems(self.tempitems)
            self.ui.comboBox_2.addItems(self.tempitems)
            self.ui.comboBox_2.setCurrentText(self.tempitems[1])
            
        elif self.ui.comboBox.currentText() == "Data":
            self.ui.comboBox_1.addItems(self.dataitems)
            self.ui.comboBox_2.addItems(self.dataitems)
            self.ui.comboBox_2.setCurrentText(self.dataitems[1])
            
    def Converter(self):

        try:
            self.num1 = float(self.ui.lineEdit.text())
            self.combo1 = self.ui.comboBox_1.currentText()
            self.combo2 = self.ui.comboBox_2.currentText()

            if self.ui.comboBox.currentText() == "Length":
                self.Lengthconverter()
            elif self.ui.comboBox.currentText() == "Weight":
                self.Weightconverter()
            elif self.ui.comboBox.currentText() == "Temprature":
                self.Tempconverter()
            elif self.ui.comboBox.currentText() == "Data":
                self.Dataconverter()
        except:
            msgBox = QMessageBox()
            msgBox.setText('Wrong input!')
            msgBox.exec() 

    def Lengthconverter(self):
        
        if self.combo1 == "milimeters" :
            if self.combo2 == "milimeters":
                self.ui.lineEdit_2.setText(str(self.num1))
            elif self.combo2 == "centimeters":
                self.ui.lineEdit_2.setText(str((self.num1)/10))
            elif self.combo2 == 'meters':
                self.ui.lineEdit_2.setText(str((self.num1)/1000))
            elif self.combo2 == 'kilometers':
                self.ui.lineEdit_2.setText(str((self.num1)/1000000))
            elif self.combo2 == 'inches':
                self.ui.lineEdit_2.setText(str((self.num1)* 0.0393701))

        elif self.combo1 == "centimeters":
            if self.combo2 == "milimeters":
                self.ui.lineEdit_2.setText(str((self.num1)*10))
            elif self.combo2 == "centimeters":
                self.ui.lineEdit_2.setText(str(self.num1))
            elif self.combo2 == 'meters':
                self.ui.lineEdit_2.setText(str((self.num1)/100))
            elif self.combo2 == 'kilometers':
                self.ui.lineEdit_2.setText(str((self.num1)/100000))
            elif self.combo2 == 'inches':
                self.ui.lineEdit_2.setText(str((self.num1)/2.54))
        
        elif self.combo1 == "meters":
            if self.combo2 == "milimeters":
                self.ui.lineEdit_2.setText(str((self.num1)*1000))
            elif self.combo2 == "centimeters":
                self.ui.lineEdit_2.setText(str((self.num1)*100))
            elif self.combo2 == 'meters':
                self.ui.lineEdit_2.setText(str(self.num1))
            elif self.combo2 == 'kilometers':
                self.ui.lineEdit_2.setText(str((self.num1)/1000))
            elif self.combo2 == 'inches':
                self.ui.lineEdit_2.setText(str((self.num1)*39.3700787))
        
        elif self.combo1 == "kilometers":
            if self.combo2 == "milimeters":
                self.ui.lineEdit_2.setText(str((self.num1)*1000000))
            elif self.combo2 == "centimeters":
                self.ui.lineEdit_2.setText(str((self.num1)*100000))
            elif self.combo2 == 'meters':
                self.ui.lineEdit_2.setText(str((self.num1)*1000))
            elif self.combo2 == 'kilometers':
                self.ui.lineEdit_2.setText(str(self.num1))
            elif self.combo2 == 'inches':
                self.ui.lineEdit_2.setText(str((self.num1)*39370.0787))

        elif self.combo1 == "inches":
            if self.combo2 == "milimeters":
                self.ui.lineEdit_2.setText(str((self.num1)*25.4))
            elif self.combo2 == "centimeters":
                self.ui.lineEdit_2.setText(str((self.num1)*2.54))
            elif self.combo2 == 'meters':
                self.ui.lineEdit_2.setText(str((self.num1)*0.0254))
            elif self.combo2 == 'kilometers':
                self.ui.lineEdit_2.setText(str((self.num1)*0.0000254))
            elif self.combo2 == 'inches':
                self.ui.lineEdit_2.setText(str(self.num1))

    def Tempconverter(self):

        if self.combo1 == "celsius":
            if self.combo2 == "celsius":
                self.ui.lineEdit_2.setText(str(self.num1))
            elif self.combo2 == "farenheit":
                self.ui.lineEdit_2.setText(str((9 * self.num1) / 5 + 32))
            elif self.combo2 == 'kelvin':
                self.ui.lineEdit_2.setText(str(self.num1 +273))

        elif self.combo1 == "farenheit":
            if self.combo2 == "celsius":
                self.ui.lineEdit_2.setText(str(int(self.num1- 32) * 5 / 9))
            elif self.combo2 == "farenheit":
                self.ui.lineEdit_2.setText(str(self.num1))
            elif self.combo2 == 'kelvin':
                self.ui.lineEdit_2.setText(str(self.num1 +273))                
        
        elif self.combo1 == "kelvin":
            if self.combo2 == "celsius":
                self.ui.lineEdit_2.setText(str(self.num1-273))
            elif self.combo2 == "farenheit":
                self.ui.lineEdit_2.setText(str(1.8 * (self.num1-273) +32))
            elif self.combo2 == 'kelvin':
                self.ui.lineEdit_2.setText(str(self.num1))   

    def Weightconverter(self):

        if self.combo1 == "grams":
            if self.combo2 == "grams":
                self.ui.lineEdit_2.setText(str(self.num1))
            elif self.combo2 == "kilograms":
                self.ui.lineEdit_2.setText(str(self.num1*0.001))
            elif self.combo2 == 'tone':
                self.ui.lineEdit_2.setText(str(self.num1*0.0000011023))
            elif self.combo2 == 'pound':
                self.ui.lineEdit_2.setText(str(self.num1*0.00220462262))

        elif self.combo1 == "kilograms":
            if self.combo2 == "grams":
                self.ui.lineEdit_2.setText(str(self.num1*1000))
            elif self.combo2 == "kilograms":
                self.ui.lineEdit_2.setText(str(self.num1))
            elif self.combo2 == 'tone':
                self.ui.lineEdit_2.setText(str(self.num1*0.00110231131))
            elif self.combo2 == 'pound':
                self.ui.lineEdit_2.setText(str(self.num1* 2.20462262))
        
        elif self.combo1 == "tone":
            if self.combo2 == "grams":
                self.ui.lineEdit_2.setText(str(self.num1*907184.74))
            elif self.combo2 == "kilograms":
                self.ui.lineEdit_2.setText(str(self.num1*907.18474))
            elif self.combo2 == 'tone':
                self.ui.lineEdit_2.setText(str(self.num1))
            elif self.combo2 == 'pound':
                self.ui.lineEdit_2.setText(str(self.num1*2000))
            
        elif self.combo1 == "pound":
            if self.combo2 == "grams":
                self.ui.lineEdit_2.setText(str(self.num1*453.59237))
            elif self.combo2 == "kilograms":
                self.ui.lineEdit_2.setText(str(self.num1*0.45359237))
            elif self.combo2 == 'tone':
                self.ui.lineEdit_2.setText(str(self.num1*0.0005))
            elif self.combo2 == 'pound':
                self.ui.lineEdit_2.setText(str(self.num1))

    def Dataconverter(self):

        if self.combo1 == "bits":
            if self.combo2 == "bits":
                self.ui.lineEdit_2.setText(str(self.num1))
            elif self.combo2 == "bytes":
                self.ui.lineEdit_2.setText(str(self.num1*0.125))
            elif self.combo2 == 'kilobytes':
                self.ui.lineEdit_2.setText(str(self.num1*0.000125))
            elif self.combo2 == 'megabytes':
                self.ui.lineEdit_2.setText(str(self.num1*0.0000000125))
            elif self.combo2 == 'gigabytes':
                self.ui.lineEdit_2.setText(str(self.num1*0.0000000000125))
            elif self.combo2 == 'terabytes':
                self.ui.lineEdit_2.setText(str(self.num1*0.0000000000000125))
        
        elif self.combo1 == "bytes":
            if self.combo2 == "bits":
                self.ui.lineEdit_2.setText(str(self.num1*8))
            elif self.combo2 == "bytes":
                self.ui.lineEdit_2.setText(str(self.num1))
            elif self.combo2 == 'kilobytes':
                self.ui.lineEdit_2.setText(str((self.num1)*0.001))
            elif self.combo2 == 'megabytes':
                self.ui.lineEdit_2.setText(str(self.num1*0.000001))
            elif self.combo2 == 'gigabytes':
                self.ui.lineEdit_2.setText(str(self.num1*0.000000001))
            elif self.combo2 == 'terabytes':
                self.ui.lineEdit_2.setText(str(self.num1*0.000000000001))

        elif self.combo1 == "kilobytes":
            if self.combo2 == "bits":
                self.ui.lineEdit_2.setText(str((self.num1)*8000))
            elif self.combo2 == "bytes":
                self.ui.lineEdit_2.setText(str((self.num1)*1000))
            elif self.combo2 == 'kilobytes':
                self.ui.lineEdit_2.setText(str(self.num1))
            elif self.combo2 == 'megabytes':
                self.ui.lineEdit_2.setText(str((self.num1)*0.001))
            elif self.combo2 == 'gigabytes':
                self.ui.lineEdit_2.setText(str(self.num1*0.000001))
            elif self.combo2 == 'terabytes':
                self.ui.lineEdit_2.setText(str(self.num1*0.000000001))

        elif self.combo1 == "megabytes":
            if self.combo2 == "bits":
                self.ui.lineEdit_2.setText(str((self.num1)*8000000))
            elif self.combo2 == "bytes":
                self.ui.lineEdit_2.setText(str((self.num1)*1000000))
            elif self.combo2 == 'kilobytes':
                self.ui.lineEdit_2.setText(str((self.num1)*1000))
            elif self.combo2 == 'megabytes':
                self.ui.lineEdit_2.setText(str(self.num1))
            elif self.combo2 == 'gigabytes':
                self.ui.lineEdit_2.setText(str((self.num1)*0.001))
            elif self.combo2 == 'terabytes':
                self.ui.lineEdit_2.setText(str(self.num1*0.000001))

        elif self.combo1 == "gigabytes":
            if self.combo2 == "bits":
                self.ui.lineEdit_2.setText(str((self.num1)*8000000000))
            elif self.combo2 == "bytes":
                self.ui.lineEdit_2.setText(str((self.num1)*1000000000))
            elif self.combo2 == 'kilobytes':
                self.ui.lineEdit_2.setText(str((self.num1)*1000000))
            elif self.combo2 == 'megabytes':
                self.ui.lineEdit_2.setText(str(self.num1*1000))
            elif self.combo2 == 'gigabytes':
                self.ui.lineEdit_2.setText(str(self.num1))
            elif self.combo2 == 'terabytes':
                self.ui.lineEdit_2.setText(str((self.num1)*0.001))
        
        elif self.combo1 == "terabytes":
            if self.combo2 == "bits":
                self.ui.lineEdit_2.setText(str((self.num1)*8000000000000))
            elif self.combo2 == "bytes":
                self.ui.lineEdit_2.setText(str((self.num1)*1000000000000))
            elif self.combo2 == 'kilobytes':
                self.ui.lineEdit_2.setText(str((self.num1)*1000000000))
            elif self.combo2 == 'megabytes':
                self.ui.lineEdit_2.setText(str(self.num1*1000000))
            elif self.combo2 == 'gigabytes':
                self.ui.lineEdit_2.setText(str(self.num1*1000))
            elif self.combo2 == 'terabytes':
                self.ui.lineEdit_2.setText(str(self.num1))
             
app = QApplication([])
window = Converting()
app.exec()
from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *
from googletrans import Translator

class Translate(QMainWindow):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load('translator.ui',None)
        self.ui.show()
        self.translator = Translator()
        self.ui.en_to_pr.setChecked(True)
        self.ui.pushButton.clicked.connect(self.translate)
    
    def translate(self):

        if self.ui.en_to_pr.isChecked():
            self.translated = self.translator.translate(self.ui.lineEdit.text(), src='en', dest='persian')
            self.ui.lineEdit_2.setText(self.translated.text)
            print(self.translated.text)

        elif self.ui.pr_to_en.isChecked():
            self.translated = self.translator.translate(self.ui.lineEdit.text(), src='persian', dest='en')
            self.ui.lineEdit_2.setText(self.translated.text)
            print(self.translated.text)

app = QApplication([])
window = Translate()

app.exec()
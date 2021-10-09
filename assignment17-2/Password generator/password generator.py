import string
import random
from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *

class Password_generator(QMainWindow):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load('form.ui',None)
        self.ui.show()
        self.characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")
        self.ui.generate.clicked.connect(self.creat_pass)

    def creat_pass(self):

        length_of_pass= int(self.ui.length.text())
        random.shuffle(self.characters)
        
        pass_list = []
        for i in range(length_of_pass):
            pass_list.append(random.choice(self.characters))

        random.shuffle(pass_list)

        self.ui.passbox.setText("".join(pass_list))


app = QApplication([])
window = Password_generator()

app.exec()
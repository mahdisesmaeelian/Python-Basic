import sys
from functools import partial
from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *
from shiboken6.Shiboken import delete
import database

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load('form.ui',None)
        self.ui.show()
        self.ReadFromDB()
        self.ui.btn_add.clicked.connect(self.AddNewTask)    
        self.ui.menuUndone.triggered.connect(self.New_page)

        for i in range(len(self.checkboxlist)):
            self.checkboxlist[i].stateChanged.connect(partial(database.CheckforDone,self.Donelist[i],self.Title1[i]))             

    def New_page(self):
        print('yes')

    def ReadFromDB(self):
        self.result = database.GetAll()
        self.del_btn = []
        self.checkboxlist = []
        self.lablelist = []
        self.Title1 = []
        self.Donelist =[]

        for i in range(len(self.result)):
            self.new_checkbox = QCheckBox()
            if self.result[i][3] == 1:
                self.new_checkbox.setChecked(True)

            self.checkboxlist.append(self.new_checkbox)
            self.Donelist.append(self.result[i][3])

            self.new_label = QLabel() 
            self.new_label.setText(self.result[i][1])
            self.Title1.append(self.result[i][1])
            self.lablelist.append(self.new_label)

            self.delete_btn = QPushButton()
            self.delete_btn.setText('❌')
            self.del_btn.append(self.delete_btn)

            self.ui.gridLayout.addWidget(self.new_checkbox, i, 1)
            self.ui.gridLayout.addWidget(self.new_label, i, 0)
            self.ui.gridLayout.addWidget(self.delete_btn, i, 2)

        for i in range(len(self.del_btn)):
            self.del_btn[i].clicked.connect(partial(self.DeleteTask,self.del_btn[i],self.checkboxlist[i],self.lablelist[i],self.Title1[i]))

    def AddNewTask(self):
        title = self.ui.textboxtitle.text()
        description = self.ui.descriptiontxtbox.text()
        database.Add(title,description)
        self.ReadFromDB()
        self.ui.textboxtitle.setText('')
        self.ui.descriptiontxtbox.setText('')


    def DeleteTask(self,a,b,c,d):
        self.ui.gridLayout.removeWidget(a)
        self.ui.gridLayout.removeWidget(b)
        self.ui.gridLayout.removeWidget(c)
        a.deleteLater()
        b.deleteLater()
        c.deleteLater()
        database.Delete(d)

class Second_page():
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load('form1.ui',None)
        self.ui.show()


app = QApplication(sys.argv)
window = MainWindow()
app.exec()
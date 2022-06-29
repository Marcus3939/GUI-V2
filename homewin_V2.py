from PyQt5 import QtCore, QtGui, QtWidgets
from ques1_V2 import *

#Code below shows the whole UI of labels, boxes and buttons. Also there are the size of the window cancas and name of the objects
class Ui_homewin(object):
    def setupUi(self, homewin):
        homewin.setObjectName("homewin")
        homewin.resize(1071, 678)
        self.centralwidget = QtWidgets.QWidget(homewin)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(290, 130, 501, 261))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")

        self.enter_name = QtWidgets.QLabel(self.formLayoutWidget)
        self.enter_name.setObjectName("enter_name")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.enter_name)

        self.T1 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.T1.setObjectName("T1")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.T1)

        self.B1 = QtWidgets.QPushButton(self.formLayoutWidget)
        self.B1.setObjectName("B1")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.B1)

        self.T2 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.T2.setObjectName("T2")
        
# This code below only allows the user to type integers instead of strings.
        self.intInputValidation=QtGui.QIntValidator()
        self.T2.setValidator(self.intInputValidation)

        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.T2)
        self.enter_age = QtWidgets.QLabel(self.formLayoutWidget)
        self.enter_age.setObjectName("enter_age")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.enter_age)
        homewin.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(homewin)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1071, 26))
        self.menubar.setObjectName("menubar")
        homewin.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(homewin)
        self.statusbar.setObjectName("statusbar")
        homewin.setStatusBar(self.statusbar)

        self.retranslateUi(homewin)
        QtCore.QMetaObject.connectSlotsByName(homewin)

#Code below mainly consists of texts in labels and buttons
    def retranslateUi(self, homewin):
        _translate = QtCore.QCoreApplication.translate
        homewin.setWindowTitle(_translate("homewin", "Quiz Home"))
        #Shows the text within the label 
        self.enter_name.setText(_translate("homewin", "Enter Name: "))
        #This code below will show the Continue text in the button
        self.B1.setText(_translate("homewin", "Continue"))
        #This is the age text
        self.enter_age.setText(_translate("homewin", "Enter Age: "))
        #When the button is clicked, it will connect to opques which is defined below
        #self.B1.clicked.connect(homewin.close)
        self.B1.clicked.connect(self.opques)
        #This code closes the window after the user presses continue or go to another window



#This code below connects the continue button to the ques1.py (continues to next window/question)
    def opques(self):
#If the user's age input is more than to equal to 10 they can proceed to the next window. 
        if self.T2.text()!="":
            if int(self.T2.text())>=10 and int(self.T2.text())<=99:
                self.queswin = QtWidgets.QMainWindow()
                self.S1 = self.T1.text()       
                self.ui = Ui_ques1(self.S1)
                self.ui.setupUi(self.queswin)
                self.queswin.show()
                homewin.close()
                
        '''self.queswin = QtWidgets.QMainWindow()
        self.S1 = self.T1.text()       
        self.ui = Ui_ques1(self.S1)
        self.ui.setupUi(self.queswin)'''
        
        

#This code below opens up the UI design
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    homewin = QtWidgets.QMainWindow()
    ui = Ui_homewin()
    ui.setupUi(homewin)
    homewin.show()
    sys.exit(app.exec_())
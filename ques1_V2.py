from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
import sys
#importing question 2 so the connection from the button can sync when pressed
from ques2_V2 import *
from tkinter import *



        #this is the timer displayed in the quiz
class Ui_ques1(QtWidgets.QWidget):
        def __init__(self, name):
                super().__init__()
                self.name = name
                a = [900, 1800]
                self.count = a
                self.total = 0
        #This sets the object name to ques 1 which is the window so I resize it to the numberss below
        def setupUi(self, ques1):
                ques1.setObjectName("ques1")
                ques1.resize(1071, 678)
                self.centralwidget = QtWidgets.QWidget(ques1)
                self.centralwidget.setObjectName("centralwidget")
        #These are the layouts of the program suggesting each specific size and placement in the GUI
                self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
                self.verticalLayoutWidget.setGeometry(QtCore.QRect(300, 310, 471, 231))
                self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
                self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
                self.verticalLayout.setContentsMargins(0, 0, 0, 0)
                self.verticalLayout.setObjectName("verticalLayout")
        #This is creating the label which would be used for titles intended in the program, in my case it would be variables such as the name/remaining time and question
                self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
                self.label.setObjectName("label")
                self.verticalLayout.addWidget(self.label)
        #Radio buttons are the options the user can choose from to get either the correct or wrong answer there would be 2 in this first question but the rest of the questions would be 4 options
                self.R1 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
                self.R1.setObjectName("R1")
                self.verticalLayout.addWidget(self.R1)
                self.R2 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
                self.R2.setObjectName("R2")
                self.verticalLayout.addWidget(self.R2)
        #This B1 represents the continue button which allows users to move forward in the program
                self.B1 = QtWidgets.QPushButton(self.verticalLayoutWidget)
                self.B1.setObjectName("B1")
                self.verticalLayout.addWidget(self.B1)
        #These layouts are the containers for the labels and buttons
                self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
                self.horizontalLayoutWidget.setGeometry(QtCore.QRect(320, 70, 431, 111))
                self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
                self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
                self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
                self.horizontalLayout.setObjectName("horizontalLayout")
        #This label is for "Name: "
                self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
                self.label_3.setObjectName("label_3")
                self.horizontalLayout.addWidget(self.label_3)
        #T1 is for the name the user has put in which would carry out in all of the next questions, T2 would be the remaining time and label 4 is the "Remaining Time: "
                self.T1 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        #The size policy of a widget is an expression of its willingness to be resized in various ways, and affects how the widget is treated by the
        #  layout engine . Each widget returns a QSizePolicy that describes the horizontal and vertical resizing policy it prefers when being laid out -qt.io
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.T1.sizePolicy().hasHeightForWidth())
                self.T1.setSizePolicy(sizePolicy)
                self.T1.setObjectName("T1")
                self.horizontalLayout.addWidget(self.T1)
                self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget)
                self.label_4.setObjectName("label_4")
                self.horizontalLayout.addWidget(self.label_4)
                self.T2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
                self.T2.setObjectName("T2")
                self.horizontalLayout.addWidget(self.T2)
        #Center widget comes built-in with flutter, it aligns its child widget to the center of the available space on the screen. 
        # The size of this widget will be as big as possible if the widthFactor and heightFactor properties are set to null and the dimensions 
        # are constrained. - https://www.geeksforgeeks.org/center-widget-in-flutter/
                ques1.setCentralWidget(self.centralwidget)
                self.menubar = QtWidgets.QMenuBar(ques1)
                self.menubar.setGeometry(QtCore.QRect(0, 0, 1071, 26))
                self.menubar.setObjectName("menubar")
                ques1.setMenuBar(self.menubar)
                self.statusbar = QtWidgets.QStatusBar(ques1)
                self.statusbar.setObjectName("statusbar")
                ques1.setStatusBar(self.statusbar)
        #QTimer is the function of remaining time
                self.timer = QTimer(self)
                self.timer.timeout.connect(self.ShowTime)
                self.timer.start(1000)
                self.retranslateUi(ques1)
                QtCore.QMetaObject.connectSlotsByName(ques1)
        #This code below translate the text intended to be in the function
        def retranslateUi(self, ques1):
                _translate = QtCore.QCoreApplication.translate
                ques1.setWindowTitle(_translate("ques1", "Question 1"))
                self.label.setText(_translate("ques1", "Question 1: Climate change is causing flowers to change colours"))
                self.R1.setText(_translate("ques1", "True"))
                self.R2.setText(_translate("ques1", "False"))
                self.B1.setText(_translate("ques1", "Continue"))
                self.label_3.setText(_translate("ques1", "Name: "))
                self.label_4.setText(_translate("ques1", "Remaining Time: "))

                #This determines if the user has chosen an option or not and lets them proceed after picking an option
                self.B1.setEnabled(False)
                self.R1.clicked.connect(self.enable)
                self.R2.clicked.connect(self.enable)
                self.B1.clicked.connect(self.opques)
                self.B1.clicked.connect(ques1.close)
                #This is the time function

                
                
        def ShowTime(self):
                if self.count > 0:
                        self.count = self.count - 1
                        #total minutes
                        S1 = str(self.count//60)
                        #remaining seconds
                        S2 = str(self.count%60)
                        S3 = S1 + ":" + S2
                        self.T1.setText(str(self.name))
                        self.T2.setText(str(S3))
        #opques is open ques and is a variable function where it opens the next question
        def enable(self):
                self.B1.setEnabled(True)    


        #when one of the buttons, in this case R1 is pressed they will gain 10 points, the R2 will lose 0 points as the user got the wrong answer
        def opques(self):
                if self.R1.isChecked() == True:
                        self.total = self.total + 10
                        self.queswin = QtWidgets.QMainWindow()
                        self.ui = Ui_ques2(self.name,self.count,self.total)
                        self.ui.setupUi(self.queswin)
                        self.queswin.show()
                if self.R2.isChecked() == True:
                        self.total = self.total - 0
                        self.queswin = QtWidgets.QMainWindow()
                        self.ui = Ui_ques2(self.name,self.count,self.total)
                        self.ui.setupUi(self.queswin)
                        self.queswin.show()

                
        #This sets up the UI from QtDesigner 
        if __name__ == "__main__":
                import sys
                app = QtWidgets.QApplication(sys.argv)
                ques1 = QtWidgets.QMainWindow()
                ui = ques1.ui()
                ui.setupUi(ques1)
                ques1.show()
                sys.exit(app.exec_())
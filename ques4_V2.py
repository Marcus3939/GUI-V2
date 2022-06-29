from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
import sys
#importing question 2 so the connection from the button can sync when pressed
from ques5_V2 import *

class Ui_ques4(QtWidgets.QWidget):
    def __init__(self, name, count, total):
        super().__init__()
        self.name = name
        self.count = count
        self.total = total
    def setupUi(self, ques4):
        ques4.setObjectName("ques4")
        ques4.resize(1046, 678)
        self.centralwidget = QtWidgets.QWidget(ques4)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(290, 300, 471, 231))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.R1 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.R1.setObjectName("R1")
        self.verticalLayout.addWidget(self.R1)
        self.R2 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.R2.setObjectName("R2")
        self.verticalLayout.addWidget(self.R2)
        self.R3 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.R3.setObjectName("R3")
        self.verticalLayout.addWidget(self.R3)
        self.R4 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.R4.setObjectName("R4")
        self.verticalLayout.addWidget(self.R4)
        self.B1 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.B1.setObjectName("B1")
        self.verticalLayout.addWidget(self.B1)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(310, 70, 431, 111))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.T1 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
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
        ques4.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ques4)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1046, 26))
        self.menubar.setObjectName("menubar")
        ques4.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ques4)
        self.statusbar.setObjectName("statusbar")
        ques4.setStatusBar(self.statusbar)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.ShowTime)
        self.timer.start(1000)
        self.retranslateUi(ques4)
        QtCore.QMetaObject.connectSlotsByName(ques4)

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
        #this is to determine whether the user has gotten the question correct or not.
    def opques(self):
        if self.R1.isChecked() == True:
            self.total = self.total + 10
        if self.R2.isChecked() == True:
            self.total = self.total - 0
        if self.R3.isChecked() == True:
            self.total = self.total - 0
        if self.R4.isChecked() == True:
            self.total = self.total - 0
        
        self.queswin = QtWidgets.QMainWindow()
        self.ui = Ui_ques5(self.name,self.count,self.total)
        self.ui.setupUi(self.queswin)
        self.queswin.show()

    def retranslateUi(self, ques4):
        _translate = QtCore.QCoreApplication.translate
        ques4.setWindowTitle(_translate("ques4", "Question 4"))
        self.label.setText(_translate("ques4", "Question 4: Out of these statements which ones are TRUE?"))
        self.R1.setText(_translate("ques4", "Some metals are so reactive that they explode on contact with water."))
        self.R2.setText(_translate("ques4", "Eating long beans make you taller"))
        self.R3.setText(_translate("ques4", "Not finishing the food on your plate will give you bad luck"))
        self.R4.setText(_translate("ques4", "Police will come if you open the courtesy lights in a car"))
        self.B1.setText(_translate("ques4", "Continue"))
        self.label_3.setText(_translate("ques4", "Name: "))
        self.label_4.setText(_translate("ques4", "Remaining Time: "))
        self.B1.setEnabled(False)
        self.R1.clicked.connect(self.enable)
        self.R2.clicked.connect(self.enable)
        self.R3.clicked.connect(self.enable)
        self.R4.clicked.connect(self.enable)
        self.B1.clicked.connect(self.opques)
        self.B1.clicked.connect(ques4.close)

    def enable(self):
        self.B1.setEnabled(True)  


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ques4 = QtWidgets.QMainWindow()
    ui = Ui_ques4()
    ui.setupUi(ques4)
    ques4.show()
    sys.exit(app.exec_())

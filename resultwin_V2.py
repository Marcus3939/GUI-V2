from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
import sys
from ques1_V2 import *

class Ui_resultwin(QtWidgets.QWidget):
    def __init__(self, name, count, total):
        super().__init__()
        self.name = name
        self.count = count
        self.total = total
        self.S1 = str(self.count//60)
        #remaining seconds
        self.S2 = str(self.count%60)
        self.S3 = self.S1 + ":" + self.S2
    def setupUi(self, resultwin):
        resultwin.setObjectName("resultwin")
        resultwin.resize(1046, 678)
        self.centralwidget = QtWidgets.QWidget(resultwin)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(360, 240, 381, 171))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        
        self.lineEdit_3 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)
        resultwin.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(resultwin)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1046, 26))
        self.menubar.setObjectName("menubar")
        resultwin.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(resultwin)
        self.statusbar.setObjectName("statusbar")
        resultwin.setStatusBar(self.statusbar)
        
        self.retranslateUi(resultwin)
        QtCore.QMetaObject.connectSlotsByName(resultwin)


    def retranslateUi(self, resultwin):
        _translate = QtCore.QCoreApplication.translate
        resultwin.setWindowTitle(_translate("resultwin", "Result"))
        self.label.setText(_translate("resultwin", "Name: "))
        self.label_2.setText(_translate("resultwin", "Time Finised: "))
        self.label_3.setText(_translate("resultwin", "Total Score: "))
        self.lineEdit.setText(str(self.name))
        self.lineEdit_2.setText(str(self.count))
        self.lineEdit_3.setText(str(self.total))

        self.lineEdit.setEnabled(False)
        self.lineEdit_2.setText(str(self.S3))
        self.lineEdit_3.setText(str(self.total))
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_3.setEnabled(False)


    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    resultwin = QtWidgets.QMainWindow()
    ui = Ui_resultwin()
    ui.setupUi(resultwin)
    resultwin.show()
    sys.exit(app.exec_())

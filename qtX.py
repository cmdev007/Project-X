import os
from PyQt5 import QtCore, QtGui, QtWidgets

def mover(loc):
    state=os.system("mv {0} mountdir/".format(loc))
    return state

def encrypt():
    state=os.system("fusermount -u mountdir")
    return state

def decrypt():
    os.system("konsole -e cryfs basedir mountdir")   
    dir = os.listdir("mountdir") 
    return len(dir)

#decrypt()

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setEnabled(True)
        Dialog.resize(601, 593)
        font = QtGui.QFont()
        font.setFamily("URW Gothic")
        font.setBold(False)
        font.setWeight(50)
        Dialog.setFont(font)
        Dialog.setSizeGripEnabled(False)
        Dialog.setModal(False)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(240, 520, 104, 41))
        font = QtGui.QFont()
        font.setFamily("URW Gothic")
        font.setBold(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.passEncry)
        self.pushButton.clicked.connect(lambda:Dialog.close())
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 450, 104, 41))
        font = QtGui.QFont()
        font.setFamily("URW Gothic")
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.passMove)
        self.pushButton_2.clicked.connect(self.refreshList)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 410, 111, 22))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(170, 20, 251, 25))
        font = QtGui.QFont()
        font.setFamily("URW Gothic")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(150, 410, 401, 28))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(55, 90, 491, 291))
        self.textBrowser.setObjectName("textBrowser")
        text=os.popen("ls mountdir").read()
        self.textBrowser.setPlainText(text)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(50, 60, 101, 22))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Project-X~Vault"))
        self.pushButton.setText(_translate("Dialog", "Close Vault!"))
        self.pushButton_2.setText(_translate("Dialog", "Lock Files"))
        self.label.setText(_translate("Dialog", "Enter the path:"))
        self.label_2.setText(_translate("Dialog", "Welcome to Project-X"))
        self.label_3.setText(_translate("Dialog", "Locked Files:"))
    
    def refreshList(self):
        text=os.popen("ls mountdir").read()
        self.textBrowser.setPlainText(text)
    
    def passMove(self):
        mover(self.lineEdit.text())

    def passEncry(self):
        encrypt()

        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
    
encrypt()

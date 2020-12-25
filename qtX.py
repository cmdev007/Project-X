import os
import time
from PyQt5 import QtCore, QtGui, QtWidgets

def mover(loc):
    state=os.system("mv {0} mountdir/".format(loc))
    return state

def unmover(loc):
    state=os.system("mv mountdir/{0} unlockdir/".format(loc))
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
        Dialog.resize(601, 762)
        font = QtGui.QFont()
        font.setFamily("URW Gothic")
        font.setBold(False)
        font.setWeight(50)
        Dialog.setFont(font)
        Dialog.setSizeGripEnabled(False)
        Dialog.setModal(False)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(160, 720, 104, 41))
        font = QtGui.QFont()
        font.setFamily("URW Gothic")
        font.setBold(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.passEncry)
        self.pushButton.clicked.connect(lambda:Dialog.close())
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 530, 104, 41))
        font = QtGui.QFont()
        font.setFamily("URW Gothic")
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.passMove)
        self.pushButton_2.clicked.connect(self.refreshList)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 490, 111, 22))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(110, 20, 371, 31))
        font = QtGui.QFont()
        font.setFamily("Orbitron")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(150, 490, 401, 28))
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
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(150, 590, 401, 28))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(30, 590, 121, 22))
        self.label_4.setObjectName("label_4")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(240, 630, 104, 41))
        self.pushButton_3.clicked.connect(self.passUnmove)
        self.pushButton_3.clicked.connect(self.refreshList)
        font = QtGui.QFont()
        font.setFamily("URW Gothic")
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(210, 410, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Orbitron")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(170, 450, 241, 24))
        #self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(320, 720, 141, 41))
        font = QtGui.QFont()
        font.setFamily("URW Gothic")
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.changePass)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Project-X~Vault"))
        self.pushButton.setText(_translate("Dialog", "Lock Vault!"))
        self.pushButton_2.setText(_translate("Dialog", "Lock Files"))
        self.label.setText(_translate("Dialog", "Enter the path:"))
        self.label_2.setText(_translate("Dialog", "Project-X ~ Secure Vault"))
        self.label_3.setText(_translate("Dialog", "Locked Files:"))
        self.label_4.setText(_translate("Dialog", "Enter File Name:"))
        self.pushButton_3.setText(_translate("Dialog", "Unlock Files"))
        self.label_5.setText(_translate("Dialog", " "))
        self.pushButton_4.setText(_translate("Dialog", "Change Password"))
    
    def refreshList(self):
        text=os.popen("ls mountdir").read()
        self.textBrowser.setPlainText(text)
    
    def passMove(self):
        _translate = QtCore.QCoreApplication.translate
        b=mover(self.lineEdit.text())
        if b==0:
            self.label_5.setText(_translate("Dialog", "Encrypting Files..."))
            self.doAction()
            self.label_5.setText(_translate("Dialog", " "))
            self.lineEdit.clear()
        else:
            self.label_5.setText(_translate("Dialog", "No such file/directory!"))
        
    def passUnmove(self):
        _translate = QtCore.QCoreApplication.translate
        b=unmover(self.lineEdit_2.text())
        if b==0:
            self.label_5.setText(_translate("Dialog", "Decrypting Files..."))
            self.doAction()
            self.label_5.setText(_translate("Dialog", " "))
            self.lineEdit_2.clear()
        else:
            self.label_5.setText(_translate("Dialog", "No such file/directory!"))

    def passEncry(self):
        _translate = QtCore.QCoreApplication.translate
        self.label_5.setText(_translate("Dialog", "Locking Vault..."))
        self.doAction()
        self.label_5.setText(_translate("Dialog", " "))
        encrypt()
        
    def doAction(self):
        for i in range(101): 
            time.sleep(0.025) 
            self.progressBar.setValue(i) 
        self.progressBar.setValue(0) 
    
    def changePass(self):
        _translate = QtCore.QCoreApplication.translate
        a=os.system("mkdir temp")
        if a==0:
            b=os.system("mv mountdir/* temp/")
            if b==0:
                c=os.system("fusermount -u mountdir")
                if c==0:
                    d=os.system("rm -rf basedir mountdir")
                    if d==0:
                        decrypt()
                        os.system("mv temp/* mountdir/")
                        os.system("rm -rf temp")
                        self.label_5.setText(_translate("Dialog", "Changing Password..."))
                        self.doAction()
                        self.label_5.setText(_translate("Dialog", " "))
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
    
#encrypt()

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loading.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import time
import os

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
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(190, 20, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Orbitron")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(70, 490, 461, 24))
        #self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.graphicsView = QtWidgets.QGraphicsView(Dialog)
        self.graphicsView.setGeometry(QtCore.QRect(60, 90, 480, 300))
        self.graphicsView.setObjectName("graphicsView")
        scene = QtWidgets.QGraphicsScene()
        self.pixmap = QtWidgets.QGraphicsPixmapItem()
        scene.addItem(self.pixmap)
        img = QtGui.QPixmap('media/bootup.jpg')
        self.pixmap.setPixmap(img)
        self.graphicsView.setScene(scene)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(100, 430, 411, 41))
        font = QtGui.QFont()
        font.setFamily("Orbitron")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(250, 540, 104, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.doAction) 

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Project-X~Vault"))
        self.label_2.setText(_translate("Dialog", "Project-X~Vault"))
        
        self.pushButton.setText(_translate("Dialog", "Open Vault!"))

    def doAction(self):
        b=self.passDecry()
        if b==0:
            print("Please check your password!")
            self.label.setText(QtCore.QCoreApplication.translate("Dialog", "Incorrect password entered!"))
            self.doAction()
        else:
            print("Files unvaulted succesfully!")
            self.label.setText(QtCore.QCoreApplication.translate("Dialog", "Project-X is Decrypting Files..."))
            for i in range(101): 
                time.sleep(0.05) 
                self.progressBar.setValue(i) 
            Dialog.close()
        
    def passDecry(self):
        b=decrypt()
        return b

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

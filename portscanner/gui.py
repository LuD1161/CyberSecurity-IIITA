#!/usr/bin/python
# coding: utf-8

import sys
import json
from PyQt4 import QtGui
import os
from PyQt4 import QtCore, QtGui


class MyPopup(QtGui.QDialog):

    def __init__(self,parent = None):
        super(MyPopup, self).__init__()
        self.setGeometry(200, 100, 600, 400)
        self.setWindowTitle("Port Scanner")
        self.setStyleSheet("QDialog{border-image: url(bg.jpg)}")
        self.Button = QtGui.QPushButton(self)
        self.Button.clicked.connect(self.Run_Something)
        self.Button.setText("Scan Ports")
        self.Button.move(250,170)

    def Run_Something(self):
        self.progress = QtGui.QProgressDialog("Running","Cancel",0,0,self) 
        self.progress.setWindowTitle('Please wait...')
        self.progress.setWindowModality(QtCore.Qt.WindowModal)
        self.progress.canceled.connect(self.progress.close)
        self.progress.show()

        self.TT = Test_Thread()
        self.TT.finished.connect(self.TT_Finished)
        self.progress.canceled.connect(self.progress.close)
        self.progress.show()
        self.TT.start()

    def TT_Finished(self):
        self.progress.setLabelText("Analysis finished")
        self.progress.setRange(0,1)
        self.progress.setValue(1)
        self.progress.setCancelButtonText("Close")
        self.progress.canceled.connect(self.progress.close)
        self.oncomplete=complete()
        self.oncomplete.show()
        self.progress.close()
        self.close()
        


    def close_application(self):
        sys.exit()



class Test_Thread(QtCore.QThread):
    finished = QtCore.pyqtSignal()

    def __init__(self):
        QtCore.QThread.__init__(self)

    def run(self):
    	os.system("python ./scanner.py")

        self.finished.emit()
        self.terminate()  



class complete(QtGui.QWidget):

    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setGeometry(50, 50, 500, 300)
        layout = QtGui.QVBoxLayout(self)
        self.button = QtGui.QPushButton('Test')
        self.edit = QtGui.QTextEdit()
        self.setStyleSheet("QTextEdit{border-image: url(bg.jpg);}")
        self.edit.setReadOnly(True)
        self.edit.setStyleSheet("QTextEdit{color:#FFFFFF},")
        layout.addWidget(self.edit)
        self.show()
        self.handleTest()


    def handleTest(self):
    	with open('output.json') as x:
    		ports = json.load(x)
    		print('yo')


    	for i in range(len(ports)):
    		self.edit.append('')
    		self.edit.insertPlainText(ports[str(i+1)]['port'])
    		self.edit.insertPlainText('    '+ports[str(i+1)]['type of port'])
    		self.edit.insertPlainText('        '+ports[str(i+1)]['service'])
    		self.edit.insertPlainText('            '+ports[str(i+1)]['remarks'])
    		i = i+1


    def close_application(self):
        sys.exit()





if __name__=='__main__':
    app = QtGui.QApplication(sys.argv)
    GUI = MyPopup()
    GUI.show()
    sys.exit(app.exec_())
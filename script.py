from PyQt5 import QtWidgets
from mainwindow import Ui_MainWindow
import sys     
import serial
from runningThread import runningThread as RT

app = QtWidgets.QApplication([])

application = Ui_MainWindow()

application.show()

def onClick(self):
	if(self.running==False):
		self.pushButton.setText("Stop")
		self.running=True
		Port = application.lineEdit.text()
		BaudRate = int(application.lineEdit_2.text())
		if (len(RT.instances)==0):
			RT(application,serial.Serial(Port, BaudRate))
	else:
		self.pushButton.setText("Start") 
		self.running=False
		RT.clear()
		
application.pushButton.clicked.connect(lambda: onClick(application))

sys.exit(app.exec())
import subprocess
import threading
import time

def temp_schedule(ser_port,application,RefreshTime):
	stop_event=False
	while(stop_event==False):
		process1=subprocess.Popen(['sensors','amdgpu-pci-0c00'], stdout=subprocess.PIPE)
		process2=subprocess.Popen(['grep','junction'], stdin=process1.stdout,stdout=subprocess.PIPE)
		output = process2.communicate()[0]
		string = str(output[15:19])[2:6]
		ba = bytes(string, 'utf-8')
		ser_port.write(ba)
		time.sleep(RefreshTime/1000)
		if (application.running==False):
			stop_event=True

class runningThread():
	instances = []
	def __init__(self,application,ser_port):
		RefreshTime = int(application.lineEdit_3.text())
		self.thread=threading.Thread(target=temp_schedule, args=[ser_port,application,RefreshTime])
		runningThread.instances.append(self)
		self.thread.start()
	@staticmethod
	def clear():
		for i in runningThread.instances:
			i.thread.join()
		runningThread.instances.clear()
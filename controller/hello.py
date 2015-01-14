if __name__ == "__main__": SystemError("No Direct Access !");print "No Direct Access !"

import sys
import os

sys.path.append(os.path.abspath("system/core"))
print "path =",os.path.abspath("system/core")

from core_controller import Controller

class hello(Controller):
	def __init__(self):
		self.controller = Controller()
		#self.view = self.controller.view()

	def index(self):
		print "controller->hello->index"
		self.controller.view('test')

#hello = hello()
#hello.index()
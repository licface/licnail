if __name__ == "__main__": SystemError("No Direct Access !");print "No Direct Access !"

from core_controller import Controller

class hello(Controller):
	def __init__(self):
		self.controller = Controller()
		#self.view = self.controller.view()

	def index(self):
		print "controller->hello->index"
		self.controller.view('test')

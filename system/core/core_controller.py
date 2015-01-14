if __name__ == "__main__": SystemError("No Direct Access !");print "No Direct Access !"

from core_view import View

class Controller(View):
	def __init__(self, **data):
		self.data = data
		#View.__init__(data['data'], data['head'], data['body'], data['main'], data['footer'], data['title'])
	def view(self, filehtml):
		self.render(filehtml)

from classone import satu

class dua(satu):
	def __init__(self):
		self.satu = satu()

c = dua()
c.printme()

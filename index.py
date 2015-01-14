print "Content-Type: text/html\n"

import os
import imp
import config
from system.core.core_controller import Controller

#APP_NAME = "cgix"

#print "page name =", os.path.basename(__file__)
#imp.load_source(APP_NAME, os.path.dirname(__file__))

class index(Controller):
	def __init__(self):
		pass
	def index(self):
		if config.route.welcome == None or config.route.welcome == '':
			print "<h1><center>404 ERROR</center></h1>"
			return "<h1><center>404 ERROR</center></h1>"
		else:
			index_path = os.path.abspath('controller/' + str(config.route.welcome) + ".py")
			index_view = imp.load_source(config.route.welcome, index_path)
			index_class = getattr(index_view, config.route.welcome)
			index_sub_class = index_class()
			return index_sub_class.index()
	def __str__(self):
		return self.index()

c = index()
c.index()
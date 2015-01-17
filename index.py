print "Content-Type: text/html\n"

import os
import imp
import config
from system.core.core_controller import Controller

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

print "SCRIPT NAME =", os.environ['SCRIPT_NAME']
print "<br>"
print "PATH INFO =", os.environ['PATH_INFO']
print "<br>"
print "QUERY STRING =", os.environ['QUERY_STRING']
print "<br>"

c = index()
c.index()
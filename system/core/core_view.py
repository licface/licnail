if __name__ == "__main__": SystemError("No Direct Access !");print "No Direct Access !"

import os
import sys

class View(object):
	def __init__(self, data=None, head=None, body=None, main=None, footer=None, title=None):
		self.data = data
		self.head = head
		self.body = body
		self.main = main
		self.footer = footer
		self.title = title

	#def render(self, filehtml=None, data=None,head=None, body=None, main=None, footer=None):
	def render(self, filehtml=None, **data):
		print "View->render->filehtml =", filehtml
		html_render = ""
		if 'data' in data.keys():
			if data['data'] == None:
				data == self.data
			else:
				data = data['data']
		if 'head' in data.keys():
			if not data['head']	== None:
				html_render += data['head']
		if 'body' in data.keys():
			if not data['body'] == None:
				html_render += data['body']
		if 'main' in data.keys():
			if not data['main'] == None:
				html_render += data['main']
		if 'footer' in data.keys():
			if not data['footer'] == None:
				html_render += data['footer']
		if filehtml == None:
			return html_render
		else:
			view_path = os.path.abspath("view")
			#print "view_path =",view_path
			filename = os.path.join(view_path, filehtml) + ".html"
			if os.path.isfile(filename):
				f = open(filename).read()
				print f
				return f
			else:
				return "ERROR"
	def __str__(self, filehtml=None, **data):
		return self.render(filename, data)

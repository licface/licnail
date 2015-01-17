import os
print "Content-type: text/html\r\n\r\n";
print main_collapsed_path
print "\n"
print "<br/>"
print os.environ.get('main_collapsed_path')
"""
for param in os.environ.keys():
  print "<b>%s</b> = %s" % (param, os.environ[param])
  print "<br/>"

print 'CONTENT_TYPE    =',os.environ['CONTENT_TYPE']
print "<br/>"
print 'CONTENT_LENGTH  =',os.environ['CONTENT_LENGTH']
print "<br/>"
print 'HTTP_COOKIE     =',os.environ['HTTP_COOKIE']
print "<br/>"
print 'HTTP_USER_AGENT =',os.environ['HTTP_USER_AGENT']
print "<br/>"
print 'PATH_INFO       =',os.environ['PATH_INFO']
print "<br/>"
print 'QUERY_STRING    =',os.environ['QUERY_STRING']
print "<br/>"
print 'REMOTE_ADDR     =',os.environ['REMOTE_ADDR']
print "<br/>"
print 'REMOTE_HOST     =',os.environ['REMOTE_HOST']
print "<br/>"
print 'REQUEST_METHOD  =',os.environ['REQUEST_METHOD']
print "<br/>"
print 'SCRIPT_FILENAME =',os.environ['SCRIPT_FILENAME']
print "<br/>"
print 'SCRIPT_NAME     =',os.environ['SCRIPT_NAME']
print "<br/>"
print 'SERVER_NAME     =',os.environ['SERVER_NAME']
print "<br/>"
print 'SERVER_SOFTWARE =',os.environ['SERVER_SOFTWARE']
print "<br/>" """

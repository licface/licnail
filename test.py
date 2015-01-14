"""import os

print "Content-type: text/html\r\n\r\n";
print "<font size=+1>Environment</font><\br>";
for param in os.environ.keys():
  print "<b>%20s</b>: %s<\br>" % (param, os.environ[param])
  """
  
#print """Content-type:text/html\r\n\r\n
#<html>
#<head>
#<title>Hello Word - First CGI Program</title>
#</head>
#<body>
#<h2>Hello Word! This is my first CGI program</h2>
#</body>
#</html>
#"""
#import os
#os.system("notepad")

f = """
<html>
        <head>
                <title>TEST</title>
        </head>
        <body>
                <h1>TEST BY MR</h1>
        </body>
</html>
"""

print f
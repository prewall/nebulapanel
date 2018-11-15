#!/usr/bin/python3.6
"""
run on server
url=http://192.168.99.206/data/cgi-bin/test.py
"""
import cgi
form = cgi.FieldStorage()
print('Content-type: text/html')

html = """
<title>test.py</title>
<H1>Greetings</H1>
<HR>
<P>%s</P>
<HR>"""

if not 'user' in form:
	print(html % 'Who are you?')
else:
	print(html % ('Hello, %s' % form['user'].value))

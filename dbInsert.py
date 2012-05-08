#!/usr/local/bin/python
import cgi
print "Content-type: text/html"
print ""
form = cgi.FieldStorage()
print form["song_id"].value
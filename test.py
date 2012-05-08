#!/usr/bin/env python
import MySQLdb
import hashlib
import cgi
import os
import random
import md5
#folderName = 'qwuwiyr647e23e'+str(random.randint(1, 10))+'/'
hash = md5.new("Nobody inspects the spammish repetition").hexdigest()
def ensure_dir(f):
    d = os.path.dirname(f)
    print d
    if not os.path.exists(d):
        os.makedirs(d)


def response():
    print "Content-type: text/html"
    print ""
    form = cgi.FieldStorage()
    x = form["term"].value
    print x
    #ensure_dir('files3/sdasda/dsad/asd/jkgjsdfksdf')
    envro = os.environ.get('ENV','PROD')
    print envro
    if (envro == "PROD"):
    	print 'You are in PROD'
    print str(random.randint(1, 10)) + 'files'
   # print folderName
    print hash


#print md5.new("Nobody inspects the spammish repetition").hexdigest()    
response()

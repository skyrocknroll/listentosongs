#!/usr/bin/env python
import MySQLdb
import cgi
import os
import re

env = 'DEV'
#DB Details
if env == 'PROD':
    DB_Host = 'localhost'
    DB_UserName = 'psgkriya_rathi'
    DB_Password = 'rathi123!@#'
    DB_Name = 'psgkriya_rathimusic'
else:
    DB_Host = 'localhost'
    DB_UserName = 'root'
    DB_Password = ''
    DB_Name = 'psgkriya_rathimusic'


def getDBCursor():
    con = MySQLdb.Connect(DB_Host,DB_UserName,DB_Password,DB_Name)
    cursor = con.cursor()
    return cursor
def search(lang):
    cursor = getDBCursor()
    if lang == "Tamil":
        sql = "select Song_id , Song_Name, Local_URL from music where Local_URL IS NOT NULL ORDER BY rand() LIMIT 20"
    elif lang == "Hindi":
        sql = "select Song_id , Song_Name, Local_URL from hindi where Local_URL IS NOT NULL ORDER BY rand() LIMIT 20"
    elif lang == "Telugu":
        sql = "select Song_id , Song_Name, Local_URL from telugu where Local_URL IS NOT NULL ORDER BY rand() LIMIT 20"
    else:
        print '[{"Id":"0", "label":"No Results Found"}]'
    cursor.execute(sql)
#    result = cursor.fetchall()
    print "["
    numrows = int(cursor.rowcount)
#    print numrows
    for i in range(numrows):
        row = cursor.fetchone()
        print '{"Id":"'+str(row[0])+'", "title":"'+row[1]+'", "src":"'+row[2].strip()+'"}'
        if(i != numrows -1):
            print ","
    if numrows == 0:
        print '{"Id":"0", "label":"No Results Found"}'
    print "]"
        
       
#search('june')
    
def response():
    print "Content-type: text/plain"
    print ""
    form = cgi.FieldStorage()
    lang = form["lang"].value;
    search(lang)
response()
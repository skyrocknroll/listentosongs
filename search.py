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
    DB_Password = 'password'
    DB_Name = 'psgkriya_rathimusic'
else:
    DB_Host = 'localhost'
    DB_UserName = 'root'
    DB_Password = 'password'
    DB_Name = 'psgkriya_rathimusic'


def getDBCursor():
    con = MySQLdb.Connect(DB_Host,DB_UserName,DB_Password,DB_Name)
    cursor = con.cursor()
    return cursor

def search(query , lang):
    cursor = getDBCursor()
    if lang == "Tamil":
        sql = "select Song_id , Song_Name, Movie_Name,Local_URL from music where Song_Name LIKE '%"+query+"%' OR Movie_Name LIKE '%"+query+"%' LIMIT 300 "
    elif lang == "Hindi":
        sql = "select Song_id , Song_Name, Movie_Name,Local_URL from hindi where Song_Name LIKE '%"+query+"%' OR Movie_Name LIKE '%"+query+"%' LIMIT 300 "
    elif lang == "Telugu":
        sql = "select Song_id , Song_Name, Movie_Name,Local_URL from telugu where Song_Name LIKE '%"+query+"%' OR Movie_Name LIKE '%"+query+"%' LIMIT 300 "
    else:
        print '[{"Id":"0", "label":"No Results Found"}]'
    cursor.execute(sql)
#    result = cursor.fetchall()
    print "["
    numrows = int(cursor.rowcount)
#    print numrows
    for i in range(numrows):
        row = cursor.fetchone()
        if (row[3] == None):
            print '{"Id":"'+str(row[0])+'", "label":"'+row[1]+'-R->'+row[2]+'"}'
        else:
            print '{"Id":"'+str(row[0])+'", "label":"'+row[1]+'-L->'+row[2]+'"}'
        if(i != numrows -1):
            print ","
    if numrows == 0:
        print '{"Id":"0", "label":"No Results Found"}'
    print "]"
        
       
#search('june')
	
def response():
    print "Content-type: text/json"
    print ""
    form = cgi.FieldStorage()
    lang = form["lang"].value;
    match = re.search(r'[^a-zA-Z0-9 ]' , form["term"].value )
#    print match
    if match:
        print '[{"Id":"0", "label":"No Results Found"}]'
    else:
        search(form["term"].value,lang)
response()

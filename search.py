#!/usr/bin/env python
import MySQLdb
import cgi
import os

env = 'PROD'
#DB Details
if env == 'PROD':
    DB_Host = 'localhost'
    DB_UserName = 'xxxx'
    DB_Password = 'xxx!@#'
    DB_Name = 'xxx'
else:
    DB_Host = 'localhost'
    DB_UserName = 'root'
    DB_Password = ''
    DB_Name = 'xxxx'


def getDBCursor():
    con = MySQLdb.Connect(DB_Host,DB_UserName,DB_Password,DB_Name)
    cursor = con.cursor()
    return cursor

def search(query):
    cursor = getDBCursor()
    sql = "select Song_id , Song_Name, Movie_Name,Local_URL from music where Song_Name LIKE '%"+query+"%' OR Movie_Name LIKE '%"+query+"%' LIMIT 300 "
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
    search(form["term"].value)
response()

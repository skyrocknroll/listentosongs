#!/usr/bin/env python
import cgi
import urllib
import MySQLdb  
import re
import md5
import random
import os
import re
#variables
folderName = 'qwuwiyr647e23e'+str(random.randint(1, 10))+'/'

env = 'PROD'
#DB Details
if env == 'PROD':
    DB_Host = 'localhost'
    DB_UserName = 'xxxx'
    DB_Password = 'xxxx!@#'
    DB_Name = 'xxxxx'
elif(env == 'DEV'):
    DB_Host = 'localhost'
    DB_UserName = 'root'
    DB_Password = ''
    DB_Name = 'xxx'



def ensure_dir(f):
    d = os.path.dirname(f)
    if not os.path.exists(d):
        os.makedirs(d)
    

def getDBConnection():
    con = MySQLdb.Connect(DB_Host, DB_UserName,DB_Password,DB_Name)
    return con

def fetchAndSaveIt(songId) :
    con = getDBConnection()
    cursor = con.cursor()
    songId = str(songId)
    sql = "select Song_URL,Local_URL,Song_Name FROM music WHERE Song_Id="+str(songId)
    cursor.execute(sql)
    url = cursor.fetchone()
    con.close()
    title = url[2].strip()
    if url[1] == None:
        url = url[0].strip()
        x = url.split('/')
        y = x[(len(x)-1)]
#        y = re.sub('.mp3|.MP3|.mP3|.Mp3','.ogg',y)
        url = url.replace(' ','%20')
        fileName = md5.new(y).hexdigest()
        fileLoc = folderName+fileName
        ensure_dir(fileLoc)
        urllib.urlretrieve(url,fileLoc)
        try:
            con = getDBConnection()
            cursor = con.cursor()
            sql = "UPDATE music SET Local_URL ='"+fileLoc+"' WHERE Song_Id="+songId
            cursor.execute(sql)
            con.commit()
            con.close()
            print '{ "Id" : "'+songId +'", "source" : "remote" ,"status":"success" , "src":"'+fileLoc+'" , "title":"'+title+'" }'
        except:
            print '{ "Id" : "'+songId +'", "source" : "local" ,"status":"failure" , "src":"'+url[1].strip()+'" , "title":"'+title+'" }'
    else:
        print '{ "Id" : "'+songId +'", "source" : "local" ,"status":"success" , "src":"'+url[1].strip()+'" , "title":"'+title+'" }'


#fetchAndSaveIt(5665)

    
def response():
    print "Content-type: text/json"
    print ""
    form = cgi.FieldStorage()
    song_Id = str(form["song_id"].value)
    match = re.search(r'[^0-9]' , song_Id )
#    print match
    if match:
        print '{ "Id" : "'+song_Id+'", "source" : "local" ,"status":"failure" , "src":"" , "title":"" }'
    else:
        fetchAndSaveIt(song_Id)

response()

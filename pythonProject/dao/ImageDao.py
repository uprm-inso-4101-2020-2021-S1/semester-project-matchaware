import MySQLdb
from config import dbconfig


class ImageDao:
    # fix this url crap tonight
   ## def __init__(self):
   ##     connection_url = MySQLdb.connect(host='24.54.205.36', Image='RemoteMatcha', passwd='RemoteMatcha', db='BeyondHorizonsDB',port = 6606)
   ##     # connection_url = (host="localhost", Image='Argent', passwd='ArgentSable776', db='MatchaWareDB')
   ##     self.conn = connection_url

    def __init__(self):
        connection_url = MySQLdb.connect(host="localhost", user='root', passwd='root', db='BeyondHorizonsDB')
        self.conn = connection_url

    def getAllImages(self):
        cursor = self.conn.cursor()
        query = "select * from Images;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getImageById(self, ImageID):
        cursor = self.conn.cursor()
        query = "select * from Images Where ImageID = %s;"
        cursor.execute(query, (ImageID,))
        result = cursor.fetchone()
        return result

    def getImagebyID(self, ImageID):
        cursor = self.conn.cursor()
        query = "select * from Images where ImageID = %s;"
        cursor.execute(query, (ImageID,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert(self, imagename, image, imagestatus, postid):
        cursor = self.conn.cursor()
        query = "insert into Images(imagename, image, imagestatus, postid) values (%s, %s, %s, %s) ;"
        cursor.execute(query, (imagename, image, imagestatus, postid,))
        query = "SELECT LAST_INSERT_ID();"
        cursor.execute(query)
        Imageid = cursor.fetchall()[0]
        self.conn.commit()
        return Imageid

    def delete(self, ImageID):
        cursor = self.conn.cursor()
        query = "delete from Images where Imageid = %s;"
        cursor.execute(query, (ImageID,))
        self.conn.commit()
        return ImageID

    def update(self, ImageID, ImageName, Image, ImageStatus, PostID):
        cursor = self.conn.cursor()
        query = "update Images set ImageName = %s, Image = %s, ImageStatus = %s, PostID = %s where ImageID = %s;"
        cursor.execute(query, (ImageName, Image, ImageStatus, PostID, ImageID,))
        self.conn.commit()
        return ImageID

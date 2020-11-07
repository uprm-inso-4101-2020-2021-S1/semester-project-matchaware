import MySQLdb
from config import dbconfig


class CommentDao:
    # fix this url crap tonight
   ## def __init__(self):
   ##     connection_url = MySQLdb.connect(host='24.54.205.36', Comment='RemoteMatcha', passwd='RemoteMatcha', db='BeyondHorizonsDB',port = 6606)
   ##     # connection_url = (host="localhost", Comment='Argent', passwd='ArgentSable776', db='MatchaWareDB')
   ##     self.conn = connection_url

    def __init__(self):
        connection_url = MySQLdb.connect(host="localhost", user='root', passwd='root', db='BeyondHorizonsDB')
        self.conn = connection_url

    def getAllComments(self):
        cursor = self.conn.cursor()
        query = "select * from Comments;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCommentById(self, CommentID):
        cursor = self.conn.cursor()
        query = "select * from Comments Where commentid = %s;"
        cursor.execute(query, (CommentID,))
        result = cursor.fetchone()
        return result

    def insert(self, PostID, CommentText, UserID, CommentDate, CommentStatus):
        cursor = self.conn.cursor()
        query = "insert into Comments(PostID, CommentText, UserID, CommentDate, CommentStatus) values (%s, %s, %s, %s, %s) ;"
        cursor.execute(query, (PostID, CommentText, UserID, CommentDate, CommentStatus,))
        query = "SELECT LAST_INSERT_ID();"
        cursor.execute(query)
        Commentid = cursor.fetchall()[0]
        self.conn.commit()
        return Commentid

    def delete(self, CommentID):
        cursor = self.conn.cursor()
        query = "delete from Comments where Commentid = %s;"
        cursor.execute(query, (CommentID,))
        self.conn.commit()
        return CommentID

    def update(self, CommentID, PostID, CommentText, UserID, CommentDate, CommentStatus):
        cursor = self.conn.cursor()
        query = "update Comments set PostID = %s, CommentText = %s, UserID = %s, CommentDate = %s, CommentStatus = %s where CommentID = %s;"
        cursor.execute(query, (PostID, CommentText, UserID, CommentDate, CommentStatus, CommentID,))
        self.conn.commit()
        return CommentID

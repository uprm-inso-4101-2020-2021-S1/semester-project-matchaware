import MySQLdb
from config import dbconfig


class CommentDao:
    # fix this url crap tonight
   ## def __init__(self):
   ##     connection_url = MySQLdb.connect(host='24.54.205.36', Comment='RemoteMatcha', passwd='RemoteMatcha', db='BeyondHorizonsDB',port = 6606)
   ##     # connection_url = (host="localhost", Comment='Argent', passwd='ArgentSable776', db='MatchaWareDB')
   ##     self.conn = connection_url

    def __init__(self):
        connection_url = MySQLdb.connect(host='24.54.205.36', user='RemoteMatcha', passwd='RemoteMatcha',
                                         db='BeyondHorizonsDB', port=6606)
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

    def insert(self, CommentText, UserID, CommentDate, CommentStatus):
        cursor = self.conn.cursor()
        query = "insert into Comments( CommentText, UserID, CommentDate, CommentStatus) values (%s, %s, %s, %s, %s) ;"
        cursor.execute(query, ( CommentText, UserID, CommentDate, CommentStatus,))
        query = "SELECT LAST_INSERT_ID();"
        cursor.execute(query)
        Commentid = cursor.fetchall()[0]
        self.conn.commit()
        return Commentid

    def delete(self, CommentID):
        cursor = self.conn.cursor()
        query = "update Comments set status = 2 where commentid = %s;"
        cursor.execute(query, (CommentID,))
        self.conn.commit()
        return CommentID

    def update(self, CommentID, PostID, CommentText, UserID, CommentDate, Status):
        cursor = self.conn.cursor()
        query = "update Comments set  CommentText = %s, UserID = %s, CommentDate = %s, Status = %s where CommentID = %s;"
        cursor.execute(query, ( CommentText, UserID, CommentDate, Status, CommentID,))
        self.conn.commit()
        return CommentID

    def insertCommentOfComment(self, CommentID, CommentText, UserID, CommentDate, Status):
        cursor = self.conn.cursor()
        query = "insert into Comments( CommentText, UserID, CommentDate, Status) values(%s ,%s ,%s , %s);"
        cursor.execute(query, ( CommentText, UserID, CommentDate, Status, CommentID,))
        query = "SELECT LAST_INSERT_ID();"
        cursor.execute(query)
        Commentid = cursor.fetchall()[0]
        query = "insert into SubComments(commentid,rootcomment) values(%s,%s);"
        cursor.execute(query,(Commentid,CommentID,))
        self.conn.commit()
        return CommentID

    def getAllCommentsOfPost(self, PostID):
        cursor = self.conn.cursor()
        query = "Select CommentID, Commenttext,userid,commentdate, status from Comments inner join PostComments on Comments.commentid = PostComments.commentid where postid = %s;"

        cursor.execute(query, (PostID,))
        result = []
        for row in cursor:
            result.append(row)
        self.conn.commit()
        return result


    def getCommentsofComments(self, CommentID):
        cursor = self.conn.cursor()
        query = "Select CommentID, Commenttext,userid,commentdate, status from Comments inner join SubComments on Comments.commentid = SubComments.commentid where RootComment = %s;"

        cursor.execute(query, (CommentID,))
        result = []
        for row in cursor:
            result.append(row)
        self.conn.commit()
        return result

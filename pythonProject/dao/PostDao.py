import MySQLdb
from config import dbconfig


class PostDAO:
    # fix this url crap tonight
    def __init__(self):
        connection_url = MySQLdb.connect(host="localhost", user='root', passwd='root', db='BeyondHorizonsDB')
        self.conn = connection_url

    def getAllPosts(self):
        cursor = self.conn.cursor()
        query = "select * from Post;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getPostById(self, PostID):
        cursor = self.conn.cursor()
        query = "select * from Post Where postid = %s;"
        cursor.execute(query, (PostID,))
        result = cursor.fetchone()
        return result

    def insert(self, posttext, userid, postdate, status):
        cursor = self.conn.cursor()
        query = "insert into Post(posttext, userid, postdate, status) values (%s, %s, %s, %s);"
        cursor.execute(query, (posttext, userid, postdate, status,))
        query = "SELECT LAST_INSERT_ID();"
        cursor.execute(query)
        postid = cursor.fetchall()[0]
        self.conn.commit()
        return postid

    def delete(self, PostID):
        cursor = self.conn.cursor()
        query = "delete from Post where postid = %s;"
        cursor.execute(query, (PostID,))
        self.conn.commit()
        return PostID

    def update(self, postid, posttext, userid, date, status):
        cursor = self.conn.cursor()
        query = "update Post set posttext = %s, userid = %s, date = %s, status = %s where postid = %s;"
        cursor.execute(query, (posttext, userid, date, status, postid,))
        self.conn.commit()
        return postid

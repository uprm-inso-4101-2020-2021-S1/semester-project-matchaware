import MySQLdb
from config import dbconfig


class ProfilePicDAO:
    # fix this url crap tonight
   ## def __init__(self):
   ##     connection_url = MySQLdb.connect(host='24.54.205.36', ProfilePic='RemoteMatcha', passwd='RemoteMatcha', db='BeyondHorizonsDB',port = 6606)
   ##     # connection_url = (host="localhost", ProfilePic='Argent', passwd='ArgentSable776', db='MatchaWareDB')
   ##     self.conn = connection_url

    def __init__(self):
        connection_url = MySQLdb.connect(host="localhost", ProfilePic='root', passwd='root', db='BeyondHorizonsDB')
        self.conn = connection_url

    def getAllProfilePics(self):
        cursor = self.conn.cursor()
        query = "select * from ProfilePic;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getProfilePicById(self, PFPID):
        cursor = self.conn.cursor()
        query = "select * from ProfilePic Where PFPID = %s;"
        cursor.execute(query, (PFPID,))
        result = cursor.fetchone()
        return result

    def insert(self, pfp, userid, status):
        cursor = self.conn.cursor()
        query = "insert into ProfilePics(PFP, UserID, Status) values (%s, %s, %s) ;"
        cursor.execute(query, (pfp, userid, status))
        query = "SELECT LAST_INSERT_ID();"
        cursor.execute(query)
        pfpid = cursor.fetchall()[0]
        self.conn.commit()
        return pfpid

    def delete(self, ProfilePicID):
        cursor = self.conn.cursor()
        query = "delete from ProfilePics where ProfilePicid = %s;"
        cursor.execute(query, (ProfilePicID,))
        self.conn.commit()
        return ProfilePicID

    def update(self, PFPID, pfp, userid, status):
        cursor = self.conn.cursor()
        query = "update ProfilePic set pfp = %s, userid = %s, status = %s where PFPID = %s;"
        cursor.execute(query, (pfp, userid, status, PFPID,))
        self.conn.commit()
        return PFPID

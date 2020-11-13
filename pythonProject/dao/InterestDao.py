import MySQLdb
from config import dbconfig


class InterestDAO:
    # fix this url crap tonight
   ## def __init__(self):
   ##     connection_url = MySQLdb.connect(host='24.54.205.36', Interest='RemoteMatcha', passwd='RemoteMatcha', db='BeyondHorizonsDB',port = 6606)
   ##     # connection_url = (host="localhost", Interest='Argent', passwd='ArgentSable776', db='MatchaWareDB')
   ##     self.conn = connection_url

    def __init__(self):
        connection_url = MySQLdb.connect(host="localhost", Interest='root', passwd='root', db='BeyondHorizonsDB')
        self.conn = connection_url

    def getAllInterests(self):
        cursor = self.conn.cursor()
        query = "select * from Interest;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getInterestById(self, InterestID):
        cursor = self.conn.cursor()
        query = "select * from Interest Where InterestID = %s;"
        cursor.execute(query, (InterestID,))
        result = cursor.fetchone()
        return result

    def insert(self, interestname, userid):
        cursor = self.conn.cursor()
        query = "insert into Interest(InterestName, UserID) values (%s, %s) ;"
        cursor.execute(query, (interestname, userid))
        query = "SELECT LAST_INSERT_ID();"
        cursor.execute(query)
        InterestID = cursor.fetchall()[0]
        self.conn.commit()
        return InterestID

    def delete(self, InterestID):
        cursor = self.conn.cursor()
        query = "delete from Interest where Interestid = %s;"
        cursor.execute(query, (InterestID,))
        self.conn.commit()
        return InterestID

    def update(self, InterestID, interestname, userid):
        cursor = self.conn.cursor()
        query = "update Interest set interestname = %s, userid = %s where InterestID = %s;"
        cursor.execute(query, (interestname, userid, InterestID,))
        self.conn.commit()
        return InterestID

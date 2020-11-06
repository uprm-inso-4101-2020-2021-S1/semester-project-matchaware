import MySQLdb
from config import dbconfig


class MemberDAO:
    # fix this url crap tonight
    def __init__(self):
        connection_url = MySQLdb.connect(host="localhost", user='root', passwd='root', db='BeyondHorizonsDB')
        self.conn = connection_url

    def getAllMembers(self):
        cursor = self.conn.cursor()
        query = "select * from Member;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getMemberById(self, MemberID):
        cursor = self.conn.cursor()
        query = "select * from Member Where memberid = %s;"
        cursor.execute(query, (MemberID,))
        result = cursor.fetchone()
        return result

    def insert(self, projectid, userid, roletypenumber, status):
        cursor = self.conn.cursor()
        query = "insert into Member(projectid, userid, roletypenumber, status) values (%s, %s, %s, %s);"
        cursor.execute(query, (projectid, userid, roletypenumber, status,))
        query = "SELECT LAST_INSERT_ID();"
        cursor.execute(query)
        Memberid = cursor.fetchall()[0]
        self.conn.commit()
        return Memberid

    def delete(self, MemberID):
        cursor = self.conn.cursor()
        query = "delete from Member where memberid = %s;"
        cursor.execute(query, (MemberID,))
        self.conn.commit()
        return MemberID

    def update(self, memberid, projectid, userid, rolltypenumber, status):
        cursor = self.conn.cursor()
        query = "update Member set memberid = %s, projectid = %s, userid = %s, rolltypenumber = %s, status = %s where memberid = %s;"
        cursor.execute(query, (projectid, userid, rolltypenumber, status, memberid,))
        self.conn.commit()
        return memberid

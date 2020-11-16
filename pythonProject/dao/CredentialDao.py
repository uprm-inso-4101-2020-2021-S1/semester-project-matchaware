import MySQLdb
from config import dbconfig


class CredentialDAO:
    # fix this url crap tonight
    def __init__(self):
        connection_url = MySQLdb.connect(host='24.54.205.36', user='RemoteMatcha', passwd='RemoteMatcha',
                                         db='BeyondHorizonsDB', port=6606)
        ##connection_url = MySQLdb.connect(host="localhost", user='root', passwd='root', db='BeyondHorizonsDB')
        self.conn = connection_url

    def getAllCredentials(self):
        cursor = self.conn.cursor()
        query = "select * from Credentials;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCredentialById(self, CredentialID):
        cursor = self.conn.cursor()
        query = "select * from Credentials Where credentialid = %s;"
        cursor.execute(query, (CredentialID,))
        result = cursor.fetchone()
        return result

    def getCredentialByUsernameandPassword(self, Username, Password):
        cursor = self.conn.cursor()
        query = "select * from Credentials Where username = %s and password = %s;"
        cursor.execute(query, (Username, Password,))
        result = cursor.fetchone()
        return result

    def insert(self, username, password, userid, status):
        cursor = self.conn.cursor()
        query = "insert into Credentials(username, password, userid, status) values (%s, %s, %s, %s);"
        cursor.execute(query, (username, password, userid, status,))
        query = "SELECT LAST_INSERT_ID();"
        cursor.execute(query)
        credentialid = cursor.fetchall()[0]
        self.conn.commit()
        return credentialid

    def delete(self, CredentialID):
        cursor = self.conn.cursor()
        query = "delete from Credentials where credentialid = %s;"
        cursor.execute(query, (CredentialID,))
        self.conn.commit()
        return CredentialID

    def update(self, credentialid,username, password, userid, status):
        cursor = self.conn.cursor()
        query = "update Credentials set credentialid = %s, username = %s, password = %s, userid = %s, status = %s where Credentialid = %s;"
        cursor.execute(query, (credentialid, username, password, userid, status, credentialid,))
        self.conn.commit()
        return credentialid

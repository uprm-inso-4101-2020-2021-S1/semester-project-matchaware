import MySQLdb
from config import dbconfig


class CredentialDAO:
    # fix this url crap tonight
    def __init__(self):
        connection_url = MySQLdb.connect(host="localhost", user='root', passwd='root', db='BeyondHorizonsDB')
        self.conn = connection_url

    def getAllCredentials(self):
        cursor = self.conn.cursor()
        query = "select * from Credential;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCredentialById(self, CredentialID):
        cursor = self.conn.cursor()
        query = "select * from Credential Where credentialid = %s;"
        cursor.execute(query, (CredentialID,))
        result = cursor.fetchone()
        return result

    def insert(self, username, password, userid, status):
        cursor = self.conn.cursor()
        query = "insert into Credential(username, password, userid, status) values (%s, %s, %s, %s) returning credentialid;"
        cursor.execute(query, (username, password, userid, status,))
        credentialid = cursor.fetchone()[0]
        self.conn.commit()
        return credentialid

    def delete(self, CredentialID):
        cursor = self.conn.cursor()
        query = "delete from Credential where credentialid = %s;"
        cursor.execute(query, (CredentialID,))
        self.conn.commit()
        return CredentialID

    def update(self, credentialid,username, password, userid, status):
        cursor = self.conn.cursor()
        query = "update Credential set credentialid = %s, username = %s, password = %s, userid = %s, status = %s where Credentialid = %s;"
        cursor.execute(query, (credentialid, username, password, userid, status, credentialid,))
        self.conn.commit()
        return credentialid

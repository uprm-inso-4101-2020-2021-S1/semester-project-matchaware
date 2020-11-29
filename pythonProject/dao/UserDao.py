import MySQLdb
import self as self

from config import dbconfig


class UserDAO:
    # fix this url crap tonight
    def __init__(self):
        connection_url = MySQLdb.connect(host='24.54.205.36', user='RemoteMatcha', passwd='RemoteMatcha', db='BeyondHorizonsDB',port = 6606)
        self.conn = connection_url

    # def __init__(self):
    #     connection_url = MySQLdb.connect(host="localhost", user='root', passwd='root', db='BeyondHorizonsDB')
    #     self.conn = connection_url

    def getAllUsers(self):
        cursor = self.conn.cursor()
        query = "select * from Users;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUserById(self, UserID):
        cursor = self.conn.cursor()
        query = "select * from Users Where userid = %s;"
        cursor.execute(query, (UserID,))
        result = cursor.fetchone()
        return result

    def insert(self, accounttypenumber, firstname, lastname, phone, email, major):
        cursor = self.conn.cursor()
        query = "insert into Users( accounttypenumber, firstname, lastname, phone, email,major) values (%s, %s, %s, %s, %s, %s) ;"
        cursor.execute(query, (accounttypenumber, firstname, lastname, phone, email,major,))
        query = "SELECT LAST_INSERT_ID();"
        cursor.execute(query)
        userid = cursor.fetchall()[0]
        self.conn.commit()
        return userid

    def delete(self, UserID):
        cursor = self.conn.cursor()
        query = "delete from Users where userid = %s;"
        cursor.execute(query, (UserID,))
        self.conn.commit()
        return UserID

    def update(self, UserID, accounttypenumber, firstname, lastname, phone, email, gender, status):
        cursor = self.conn.cursor()
        query = "update Users set account  typenumber = %s, firstname = %s, lastname = %s, phone = %s, email = %s, gender = %s, status = %s where userid = %s;"
        cursor.execute(query, (accounttypenumber, firstname, lastname, phone, email, gender, status, UserID,))
        self.conn.commit()
        return UserID

import MySQLdb
from config import dbconfig


class StatisticsDao:
    def __init__(self):
        connection_url = MySQLdb.connect(host='24.54.205.36', user='RemoteMatcha', passwd='RemoteMatcha',
                                         db='BeyondHorizonsDB', port=6606)
        self.conn = connection_url

    def getTopfollowedUser(self,top):
        cursor = self.conn.cursor()
        query = "select * from Project;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTopfollowedOrg(self, top):
        cursor = self.conn.cursor()
        query = "select * from Project;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTopfollowedProject(self,top):
        cursor = self.conn.cursor()
        query = "select * from Project;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getTopviewedOrg(self,top):
        cursor = self.conn.cursor()
        query = "select * from Project;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTopviewedProject(self,top):
        cursor = self.conn.cursor()
        query = "select * from Project;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

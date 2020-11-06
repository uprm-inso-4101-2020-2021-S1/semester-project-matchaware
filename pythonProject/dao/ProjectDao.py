import MySQLdb
from config import dbconfig


class ProjectDAO:
    # fix this url crap tonight
    def __init__(self):
        connection_url = MySQLdb.connect(host="localhost", user='root', passwd='root', db='BeyondHorizonsDB')
        self.conn = connection_url

    def getAllProjects(self):
        cursor = self.conn.cursor()
        query = "select * from Project;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getProjectById(self, ProjectID):
        cursor = self.conn.cursor()
        query = "select * from Project Where projectid = %s;"
        cursor.execute(query, (ProjectID,))
        result = cursor.fetchone()
        return result

    def insert(self, projectname, projectdescription, imagelogo,userid, projecttypenumber, status):
        cursor = self.conn.cursor()
        query = "insert into Project( projectname, projectdescription, imagelogo, userid, projecttypenumber, status) values (%s, %s, %s, %s, %s, %s);"
        cursor.execute(query, (projectname, projectdescription, imagelogo, userid, projecttypenumber, status,))
        query = "SELECT LAST_INSERT_ID();"
        cursor.execute(query)
        projectid = cursor.fetchall()[0]
        self.conn.commit()
        return projectid

    def delete(self, ProjectID):
        cursor = self.conn.cursor()
        query = "delete from Project where projectid = %s;"
        cursor.execute(query, (ProjectID,))
        self.conn.commit()
        return ProjectID

    def update(self, projectid, projectname, projectdescription, imagelogo, userid, projecttypenumber, status):
        cursor = self.conn.cursor()
        query = "update Project set projectname = %s, projectdescription = %s, imagelogo = %s, and userid = %s, projecttypenumber = %s, status where projectid = %s;"
        cursor.execute(query, (projectname, projectdescription, imagelogo, userid, projecttypenumber, status, projectid,))
        self.conn.commit()
        return projectid

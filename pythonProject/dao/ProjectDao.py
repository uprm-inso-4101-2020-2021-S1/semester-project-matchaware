#import MySQLdb
import pymysql
from config import dbconfig


class ProjectDAO:
    # fix this url crap tonight
    def __init__(self):
        #connection_url = MySQLdb.connect(host='24.54.205.36', user='RemoteMatcha', passwd='RemoteMatcha',
         #                                db='BeyondHorizonsDB', port=6606)
        connection_url = pymysql.connect(host="localhost", user='Argent', passwd='ArgentSable776',
                                         db='BeyondHorizonsDB')
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

    def insert(self, projecttitle, projectDescription, projectViewCounter, creationDate,lastUpdate,ProjectType,status):
        cursor = self.conn.cursor()
        query = "insert into Project(projecttitle, projectDescription, projectViewCounter, creationDate,lastUpdate,ProjectType,status) values (%s, %s, %s, %s, %s, %s,%s);"
        cursor.execute(query, (projecttitle, projectDescription, projectViewCounter, creationDate,lastUpdate,ProjectType,status,))
        query = "SELECT LAST_INSERT_ID();"
        cursor.execute(query)
        projectid = cursor.fetchall()[0]
        self.conn.commit()
        return projectid

    def delete(self, ProjectID):
        cursor = self.conn.cursor()
        query = "update Project set status = 2 where projectid = %s;"
        cursor.execute(query, (ProjectID,))
        self.conn.commit()
        return ProjectID

    def update(self,projectid, Projecttitle,projectdescription,projectviewcounter,creationdate,lastupdate, projecttypenumber, status):
        cursor = self.conn.cursor()
        query = "update Project set projecttitle = %s, projectdescription = %s, projectviewCounter =%s,creationdate = %s, lastupdate=%s ,projecttype =%s,status=%s where projectid = %s;"
        cursor.execute(query, (Projecttitle,projectdescription,projectviewcounter,creationdate,lastupdate, projecttypenumber, status,))
        self.conn.commit()
        return projectid

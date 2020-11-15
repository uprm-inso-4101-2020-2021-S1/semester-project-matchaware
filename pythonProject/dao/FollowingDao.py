import MySQLdb
from config import dbconfig


class FollowingDAO:
    # fix this url crap tonight
   ## def __init__(self):
   ##     connection_url = MySQLdb.connect(host='24.54.205.36', user='RemoteMatcha', passwd='RemoteMatcha', db='BeyondHorizonsDB',port = 6606)
   ##     # connection_url = (host="localhost", user='Argent', passwd='ArgentSable776', db='MatchaWareDB')
   ##     self.conn = connection_url

    def __init__(self):
        connection_url = MySQLdb.connect(host="localhost", user='root', passwd='root', db='BeyondHorizonsDB')
        self.conn = connection_url

    def getAllFollowed(self):
        cursor = self.conn.cursor()
        query = "Select UserID, FollowedUserID, OrganizationID, ProjectID From FollowingUsers natural join " \
                "FollowingOrganizations natural join FollowingProject; "
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getFollowedByUserID(self, UserID):
        cursor = self.conn.cursor()
        query = "Select UserID, FollowedUserID, OrganizationID, ProjectID From FollowingUsers natural join " \
                "FollowingOrganizations natural join FollowingProject Where UserID = %s; "
        cursor.execute(query, (UserID,))
        result = cursor.fetchone()
        return result

    def insertOrg(self,  OrganizationID, UserID):
        cursor = self.conn.cursor()
        query = "insert into FollowingOrganization(OrganizationID, UserID) values (%s, %s) ;"
        cursor.execute(query, (OrganizationID, UserID))
        query = "SELECT LAST_INSERT_ID();"
        cursor.execute(query)
        followingorganizationid = cursor.fetchall()[0]
        self.conn.commit()
        return followingorganizationid

    def insertProject(self,  ProjectID, UserID):
        cursor = self.conn.cursor()
        query = "insert into FollowingProject(ProjectID, UserID) values (%s, %s) ;"
        cursor.execute(query, (ProjectID, UserID))
        query = "SELECT LAST_INSERT_ID();"
        cursor.execute(query)
        followingprojectid = cursor.fetchall()[0]
        self.conn.commit()
        return followingprojectid

    def insertUsers(self,  FollowedUserID, UserID):
        cursor = self.conn.cursor()
        query = "insert into FollowingUsers(FollowedUserID, UserID) values (%s, %s) ;"
        cursor.execute(query, (FollowedUserID, UserID))
        query = "SELECT LAST_INSERT_ID();"
        cursor.execute(query)
        followingusersid = cursor.fetchall()[0]
        self.conn.commit()
        return followingusersid
###Not implemented
    def delete(self, UserID):
        cursor = self.conn.cursor()
        query = "delete from Users where userid = %s;"
        cursor.execute(query, (UserID,))
        self.conn.commit()
        return UserID

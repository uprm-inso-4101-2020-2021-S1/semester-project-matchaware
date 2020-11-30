#import MySQLdb
import pymysql


class OrganizationDao:
    # fix this url crap tonight
    def __init__(self):
        #connection_url = MySQLdb.connect(host='24.54.205.36', user='RemoteMatcha', passwd='RemoteMatcha',
        #                                 db='BeyondHorizonsDB', port=6606)

        connection_url = pymysql.connect(host="localhost", user='Argent', passwd='ArgentSable776',
                                         db='BeyondHorizonsDB')
        self.conn = connection_url


    def inserOrganization(self,OrganizationName,OrganizationDescription , OrganizationViewCounter ,CreationDate,LastUpdate,Status):
        cursor = self.conn.cursor()
        query = "insert into Organization( OrganizationName,OrganizationDescription , OrganizationViewCounter ,CreationDate,LastUpdate,Status) values ( %s, %s, %s,%s,%s,%s);"
        cursor.execute(query, (OrganizationName,OrganizationDescription , OrganizationViewCounter ,CreationDate,LastUpdate,Status))
        query = "SELECT LAST_INSERT_ID();"
        cursor.execute(query)
        Organizationid = cursor.fetchall()[0]
        self.conn.commit()
        return Organizationid


    def updateOrganization(self,OrganizationID,OrganizationName,OrganizationDescription , OrganizationViewCounter ,CreationDate,LastUpdate,Status):
        cursor = self.conn.cursor()
        query = "update Organization set  OrganizationID = %s,OrganizationName= %s,OrganizationDescription= %s , OrganizationViewCounter = %s,CreationDate= %s,LastUpdate= %s,Status= %s where organizationid = %s;"
        cursor.execute(query, (OrganizationID,OrganizationName,OrganizationDescription , OrganizationViewCounter ,CreationDate,LastUpdate,Status))
        self.conn.commit()
        return OrganizationID

    def deleteOrganization(self,OrganizationID):
        cursor = self.conn.cursor()
        query = "update Organization set Status= 2 where Organizationid = %s;"
        cursor.execute(query,(OrganizationID))
        self.conn.commit()
        return OrganizationID

    def insertOrganizationMember(self,memberid,organizationid,JoinDate,Status):
        cursor = self.conn.cursor()
        query = "insert into OrganizationMember (memberid,organizaionid, joindate, status) values(%s,%s,%s.%s);"
        cursor.execute(query, (memberid,organizationid,JoinDate,Status))
        query = "SELECT LAST_INSERT_ID();"
        cursor.execute(query)
        Organizationid = cursor.fetchall()[0]
        self.conn.commit()
        return Organizationid

    def getOrganization(self, OrganizationID):
        cursor = self.conn.cursor()
        query = "Select * from  Organization  where Organizationid = %s;"
        cursor.execute(query, (OrganizationID))
        Results = cursor.fetchall()
        self.conn.commit()
        return Results


    def updateOrganizationMember(self, memberid, organizationid, JoinDate, Status):
        cursor = self.conn.cursor()
        query = "UPDATE OrganizationMember SET memberid = %s, organizationid= %s, JoinDate= %s, Status= %s WHERE organizationmemberid= %s;"
        cursor.execute(query, (memberid, organizationid, JoinDate, Status))
        self.conn.commit()
        return memberid

    def deleteorganizationmember(self, organizationmemberid):
        cursor = self.conn.cursor()
        query = "UPDATE OrganizationMembers SET status=2 WHERE organizationmemberid= %s;"
        cursor.execute(query, (organizationmemberid,))
        self.conn.commit()
        return organizationmemberid

    def getallMembersorganization(self, organizationid):
        cursor = self.conn.cursor()
        query = "select * from Members inner join OrganizationMember on memberid where organizationid = %s;"
        cursor.execute(query, (organizationid,))
        self.conn.commit()
        return organizationid

    def getallOrganizations(self):
        cursor = self.conn.cursor()
        query = "select * from Organization where status=1;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        self.conn.commit()
        return result

    def insertOrganizationProject(self, OrganizationID, ProjectID):
        cursor = self.conn.cursor()
        query = "insert into OrgProjects (organizationid,projectid) values(%s,%s);"
        cursor.execute(query, (OrganizationID, ProjectID))
        query = "SELECT LAST_INSERT_ID();"
        cursor.execute(query)
        Orgprojectid = cursor.fetchall()[0]
        self.conn.commit()
        return  Orgprojectid

    def updateOrganizationProject(self,orgprojectid, OrganizationID, ProjectID, status):
        cursor = self.conn.cursor()
        query = "UPDATE OrgProjects SET OrganizationID = %s, ProjectID = %s,status =%s WHERE orgprojectid= %s;"
        cursor.execute(query, (OrganizationID, ProjectID, status, orgprojectid))
        self.conn.commit()
        return orgprojectid

    def deleteOrganizationProject(self, OrgProjectID, ProjectID):
        cursor = self.conn.cursor()
        query = "UPDATE OrgProjects SET status =2 WHERE orgprojectid= %s;"
        cursor.execute(query, (OrgProjectID))
        self.conn.commit()
        return OrgProjectID

from flask import jsonify
from dao import OrganizationDao
from dao import MemberDao
from dao import ProjectDao

class OrganizationHandler:
    #testing

    def inserOrganization(self,json):
        dao = OrganizationDao.OrganizationDao()
        OrganizationName = json['OrganizationName']
        OrganizationDescription = json['OrganizationDescription']
        OrganizationViewCounter = json['OrganizationViewCounter']
        CreationDate = json['CreationDate']
        LastUpdate = json['lastUpdate']
        Status = json['Status']

        if OrganizationName and OrganizationDescription and OrganizationViewCounter and CreationDate and LastUpdate and Status:
            organizationid = dao.inserOrganization(OrganizationName,OrganizationDescription , OrganizationViewCounter ,CreationDate,LastUpdate,Status)
            if(organizationid):
                return jsonify(OrganizationID = organizationid) ,201
            else:
                return jsonify(ERROR = "Unable to insert into DB") ,400
        else:
            return jsonify(ERROR = "Invalid arguments") ,400



    def updateOrganization(self,json):
        dao = OrganizationDao.OrganizationDao()
        OrganizationID = json['OrganizationID']
        OrganizationName = json['OrganizationName']
        OrganizationDescription = json['OrganizationDescription']
        OrganizationViewCounter = json['OrganizationViewCounter']
        CreationDate = json['CreationDate']
        LastUpdate = json['lastUpdate']
        Status = json['Status']
        if OrganizationID and OrganizationName and OrganizationDescription and OrganizationViewCounter and CreationDate and LastUpdate and Status:
            organizationid = dao.updateOrganization(OrganizationID,OrganizationName,OrganizationDescription , OrganizationViewCounter ,CreationDate,LastUpdate,Status)
            if(organizationid):
                return jsonify(Updated = "Organiaation Updated") ,201
            else:
                return jsonify(ERROR = "Unable to update into DB") ,400
        else:
            return jsonify(ERROR = "Invalid arguments") ,400


    def deleteOrganization(self, organizationid):
        dao = OrganizationDao.OrganizationDao()

        if organizationid:
            status = dao.deleteOrganization(organizationid)
            if status:
                return jsonify(Status = status) , 201
            else:
                return jsonify(ERROR="Unable to delete "), 400
        else:
            return jsonify(ERROR="Invalid arguments"), 400

    def addOrganizationMember(self,organizationid, json):
        dao = OrganizationDao.OrganizationDao()
        daom = MemberDao.MemberDAO()
        UserID = json['UserID']
        RoleTypeNumber = json['RoleTypeNumber']
        Status = json['Status']
        JoinDate = json['JoinDate']
        if not dao.getOrganization(organizationid):
            return jsonify(ERROR='Invalid Organization'),400

        if UserID and RoleTypeNumber and Status and JoinDate:
            memberid = daom.insert(UserID,RoleTypeNumber,Status)
            if memberid:
                Organizationmemberid = dao.insertOrganizationMember(memberid,organizationid,JoinDate,Status)
                if organizationid:
                    return jsonify(OrganizationMemberID = Organizationmemberid) ,201
                else:

                    return jsonify(ERROR='Unable to insert new organization member'), 400
            else:
                return jsonify(ERROR='Unable to inser new member'),400
        else:
            return jsonify(ERROR = 'Invalid arguments'),400


    def updateOrganizationMember(self,organizationid, json):
        dao = OrganizationDao.OrganizationDao()
        daom = MemberDao.MemberDAO()
        UserID = json['UserID']
        RoleTypeNumber = json['RoleTypeNumber']
        Status = json['Status']
        JoinDate = json['JoinDate']
        if not dao.getOrganization(organizationid):
            return jsonify(ERROR='Invalid Organization'), 400

        if UserID and RoleTypeNumber and Status and JoinDate:
            memberid = daom.update(UserID, RoleTypeNumber, Status)
            if memberid:
                Organizationmemberid = dao.updateOrganizationMember(memberid, organizationid, JoinDate, Status)
                if organizationid:
                    return jsonify(OrganizationMemberID=Organizationmemberid), 201
                else:

                    return jsonify(ERROR='Unable to update new organization member'), 400
            else:
                return jsonify(ERROR='Unable to update new member'), 400
        else:
            return jsonify(ERROR='Invalid arguments'), 400



    def deleteOrganizationMember(self,organizationmemberid):
        dao = OrganizationDao.OrganizationDao()
        daom = MemberDao.MemberDAO()
        if(organizationmemberid):
            memberid =dao.deleteorganizationmember(organizationmemberid)
            status = daom.delete(memberid)
            if status:
                return jsonify(Status=status), 201
            else:
                return jsonify(ERROR="Unable to delete "), 400
        else:
            return jsonify(ERROR="Invalid arguments"), 400

    def addOrganizationProject(self,json):
        dao = OrganizationDao.OrganizationDao()
        pdao = ProjectDao.ProjectDAO()
        OrganizationID = json['OrganizationID']
        ProjectTitle = json['ProjectTitle']
        ProjectDescription = json['ProjectDescription']
        ProjectViewCounter  = json['ProjectViewCounter']
        CreationDate = json['CreationDate']
        LastUpdate = json['LastUpdate']
        ProjectType = json['ProjectType']
        Status = json['Status']
        if dao.getOrganization(OrganizationID):
            if OrganizationID and ProjectTitle and ProjectDescription and ProjectViewCounter and CreationDate and LastUpdate and ProjectType and Status:
                ProjectID = pdao.insert(ProjectTitle , ProjectDescription ,ProjectViewCounter ,CreationDate and LastUpdate , ProjectType ,Status)
                if ProjectID:
                    orgprojectid = dao.insertOrganizationProject(OrganizationID,ProjectID)
                    if orgprojectid:
                        return jsonify(ProjectID = ProjectID), 200
                    else:
                        return jsonify(ERROR="Invalid arguments "),400
                else:
                    return jsonify(ERROR="coulnt insert into project"),400
            else:
                return jsonify(ERROR="Invalid Arguments"),400
        else:
            return jsonify(ERROR="Invalid organizationID"),400


    def updateOrganizationProject(self,json):
        dao = OrganizationDao.OrganizationDao()
        pdao = ProjectDao.ProjectDAO()
        OrganizationID = json['OrganizationID']
        ProjectTitle = json['ProjectTitle']
        ProjectDescription = json['ProjectDescription']
        ProjectViewCounter = json['ProjectViewCounter']
        CreationDate = json['CreationDate']
        LastUpdate = json['LastUpdate']
        ProjectType = json['ProjectType']
        Status = json['Status']
        if dao.getOrganization(OrganizationID):
            if OrganizationID and ProjectTitle and ProjectDescription and ProjectViewCounter and CreationDate and LastUpdate and ProjectType and Status:
                ProjectID = pdao.update(ProjectTitle, ProjectDescription, ProjectViewCounter, CreationDate and LastUpdate, ProjectType, Status)
                if ProjectID:
                    orgprojectid = dao.updateOrganizationProject(OrganizationID, ProjectID , Status)
                    if orgprojectid:
                        return jsonify(ProjectID=ProjectID), 200
                    else:
                        return jsonify(ERROR="Invalid arguments "), 400
                else:
                    return jsonify(ERROR="coulnt update into project"), 400
            else:
                return jsonify(ERROR="Invalid Arguments"), 400
        else:
            return jsonify(ERROR="Invalid organizationID"), 400

    def deleteorganizationProject(self,json):
        dao = OrganizationDao.OrganizationDao()
        pdao = ProjectDao.ProjectDAO()
        OrganizationID = json['OrganizationID']
        ProjectID = json['ProjectID']
        LastUpdate = json['LastUpdate']
        Status = json['Status']
        if dao.getOrganization(OrganizationID):
            if OrganizationID and LastUpdate and Status and ProjectID:
                output = pdao.delete(ProjectID) #lastupdate
                if output:
                    orgprojectid = dao.deleteOrganizationProject(OrganizationID, ProjectID)

                    if orgprojectid:
                        return jsonify(ProjectID=ProjectID), 200
                    else:
                        return jsonify(ERROR="Invalid arguments "), 400
                else:
                    return jsonify(ERROR="coulnt update into project"), 400
            else:
                return jsonify(ERROR="Invalid Arguments"), 400
        else:
            return jsonify(ERROR="Invalid organizationID"), 404

    def getAllMembersOrganization(self, organizationid):
        dao = OrganizationDao.OrganizationDao()
        if organizationid:
            if not dao.getOrganization(organizationid):
                return jsonify(ERROR='Invalid organization'),400
            data = dao.getallMembersorganization(organizationid)
            result =[]
            for row in data:
                result.append(self.build_diccionary_Member(row))
            return jsonify(result), 200 
        else:
            return jsonify(ERROR= "Invalid arguments"),400

    def getOrganization(self,organizationid):
        dao = OrganizationDao.OrganizationDao()
        if organizationid:
            data = dao.getOrganization(organizationid)
            return jsonify(self.build_diccionary_organization(data)),200
        else:
            return jsonify(ERROR= "Invalid OrganizationID"),400
    def getAllOrganizations(self):
        dao = OrganizationDao.OrganizationDao()
        data = dao.getallOrganizations()
        result = []
        for row in data:
            result.append(self.build_diccionary_organization(row))

        return jsonify(Organization = result), 201

    def build_diccionary_organization(self, row):
        result = {}
        result['OrganizationID']=row[0]
        result['OrganizationName'] = row[1]
        result['OrganizationDescription'] = row[2]
        result['OrganizationViewCounter'] = row[3]
        result['CreationDate'] = row[4]
        result['LastUpdate'] = row[5]
        result['Status'] = row[6]
        return result

    def build_diccionary_Member(self, row):
        result = {}
        result['MemberID'] = row[0]
        result['UserID'] = row[1]
        result['RoleTypeNumber'] = row[2]
        result['Status'] = row[3]
        return result



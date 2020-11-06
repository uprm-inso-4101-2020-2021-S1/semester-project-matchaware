from flask import jsonify
from dao import ProjectDao


class ProjectHandler:
    def build_project_dict(self, row):
        result = {}
        result['ProjectID'] = row[0]
        result['ProjectName'] = row[1]
        result['ProjectDescription'] = row[2]
        result['ImageLogo'] = row[3]
        result['UserID'] = row[4]
        result['ProjectTypeNumber'] = row[5]
        result['Status'] = row[6]
        return result

    def build_project_attributes(self, ProjectID, ProjectName, ProjectDescription, ImageLogo, UserID, ProjectType, Status):
        result = {}
        result['ProjectID'] = ProjectID
        result['ProjectName'] = ProjectName
        result['ProjectDescription'] = ProjectDescription
        result['ImageLogo'] = ImageLogo
        result['UserID'] = UserID
        result['ProjectTypeNumber'] = ProjectType
        result['Status'] = Status
        return result

    def getAllProjects(self):
        dao = ProjectDao.ProjectDAO()
        Project_list = dao.getAllProjects()
        result_list = []
        for row in Project_list:
            result = self.build_project_dict(row)
            result_list.append(result)
        return jsonify(Project=result_list)

    def getProjectById(self, ProjectID):
        dao = ProjectDao.ProjectDAO()
        row = dao.getProjectById(ProjectID)
        if not row:
            return jsonify(Error="Project Not Found"), 404
        else:
            Project = self.build_project_dict(row)
            return jsonify(Project=Project)

    def insertProjectJson(self, json):
        projectname = json['ProjectName']
        projectdescription = json['ProjectDescription']
        imagelogo = json['ImageLogo']
        userid = json['UserID']
        projecttypenumber = json['ProjectTypeNumber']
        status = json['Status']
        if projectname and projectdescription and imagelogo and userid and projecttypenumber and status:
            dao = ProjectDao.ProjectDAO()
            projectid = dao.insert(projectname, projectdescription, imagelogo, userid, projecttypenumber, status)
            result = self.build_project_attributes(projectid, projectname, projectdescription, imagelogo, userid,
                                                   projecttypenumber, status)
            return jsonify(Project=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

    def deleteProject(self, projectid):
        dao = ProjectDao.ProjectDAO
        if not dao.getProjectById(projectid):
            return jsonify(Error="Project not found."), 404
        else:
            dao.delete(projectid)
            return jsonify(DeleteStatus="OK"), 200

    def updateProjectJson(self, projectid, json):
        dao = ProjectDao.ProjectDAO()
        if not dao.getProjectById(projectid):
            return jsonify(Error="Project not found."), 404
        else:
            projectname = json['ProjectName']
            projectdescription = json['ProjectDescription']
            imagelogo = json['ImageLogo']
            userid = json['UserID']
            projecttypenumber = json['ProjectTypeNumber']
            status = json['Status']
            if projectname and projectdescription and imagelogo and userid and projecttypenumber and status:
                dao.update(projectname, projectdescription, imagelogo,userid ,projecttypenumber, status)
                result = self.build_project_attributes(projectid, projectname, projectdescription, imagelogo,userid,
                                                       projecttypenumber, status)
                return jsonify(Project=result), 200

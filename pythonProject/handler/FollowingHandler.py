from flask import jsonify
from dao import FollowingDao


class FollowingHandler:
    def build_following_dict(self, row):
        result = {}
        result['UserID'] = row[0]
        result['FollowedUserID'] = row[1]
        result['OrganizationID'] = row[2]
        result['ProjectID'] = row[3]
        return result

    def build_following_attributes(self, UserID, FollowedUserID, OrganizationID, ProjectID):
        result = {}
        result['UserID'] = UserID
        result['FollowedUserID'] = FollowedUserID
        result['OrganizationID'] = OrganizationID
        result['ProjectID'] = ProjectID
        return result

    ###################################################################
    def build_followingusers_dict(self, row):
        result = {}
        result['FollowingUsersID'] = row[0]
        result['FollowedUserID'] = row[1]
        result['UserID'] = row[2]
        return result

    def build_followingusers_attributes(self, FollowingUsersID, FollowedUserID, UserID):
        result = {}
        result['FollowingUsersID'] = FollowingUsersID
        result['FollowedUserID'] = FollowedUserID
        result['UserID'] = UserID
        return result

    ############################################################################
    def build_followingorgs_dict(self, row):
        result = {}
        result['FollowingOrganizationID'] = row[0]
        result['OrganizationID'] = row[1]
        result['UserID'] = row[2]
        return result

    def build_followingorgs_attributes(self, FollowingOrganizationID, OrganizationID, UserID):
        result = {}
        result['FollowingOrganizationID'] = FollowingOrganizationID
        result['ProjectID'] = OrganizationID
        result['UserID'] = UserID
        return result

    #####################################################################
    def build_followingprojects_dict(self, row):
        result = {}
        result['FollowingProjectID'] = row[0]
        result['ProjectID'] = row[1]
        result['UserID'] = row[2]
        return result

    def build_followingprojects_attributes(self, FollowingProjectID, ProjectID, UserID):
        result = {}
        result['FollowingProjectID'] = FollowingProjectID
        result['ProjectID'] = ProjectID
        result['UserID'] = UserID
        return result

    def getAllFollowed(self):
        dao = FollowingDao.FollowingDAO()
        Following_list = dao.getAllFollowed()
        result_list = []
        for row in Following_list:
            result = self.build_following_dict(row)
            result_list.append(result)
        return jsonify(Following=result_list)

    def getFollowedByUserId(self, UserID):
        dao = FollowingDao.FollowingDAO()
        row = dao.getFollowedByUserID(UserID)
        if not row:
            return jsonify(Error="Following Not Found"), 404
        else:
            Following = self.build_following_dict(row)
            return jsonify(Following=Following)

    def insertOrgFollowJson(self, json):
        OrganizationID = json['OrganizationID']
        UserID = json['UserID']
        if OrganizationID and UserID:
            dao = FollowingDao.FollowingDAO()
            FollowingOrganizationID = dao.insertOrg(OrganizationID, UserID)
            result = self.build_followingorgs_attributes(FollowingOrganizationID, OrganizationID, UserID)
            return jsonify(Following=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

    def insertProjectFollowJson(self, json):
        ProjectID = json['ProjectID']
        UserID = json['UserID']
        if ProjectID and UserID:
            dao = FollowingDao.FollowingDAO()
            FollowingProjectID = dao.insertProject(ProjectID, UserID)
            result = self.build_followingprojects_attributes(FollowingProjectID, ProjectID, UserID)
            return jsonify(Following=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

    def insertUserFollowJson(self, json):
        FollowedUserID = json['FollowedUserID']
        UserID = json['UserID']
        if FollowedUserID and UserID:
            dao = FollowingDao.FollowingDAO()
            FollowingUsersID = dao.insertUsers(FollowedUserID, UserID)
            result = self.build_followingusers_attributes(FollowingUsersID, FollowedUserID, UserID)
            return jsonify(Following=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400
###Not implemented.
    def deleteFollowed(self, UserID):
        dao = FollowingDao.FollowingDAO()
        if not dao.getFollowedByUserID(UserID):
            return jsonify(Error="Following not found."), 404
        else:
            dao.delete(UserID)
            return jsonify(DeleteStatus="OK"), 200

from flask import jsonify
from dao import ProfilePicDao


class ProfilePicsHandler:
    def build_profilepics_dict(self, row):
        result = {}
        result['PFPID'] = row[0]
        result['PFP'] = row[1]
        result['UserID'] = row[2]
        result['Status'] = row[3]
        return result

    def build_profilepics_attributes(self, PFPID, PFP, UserID, Status):
        result = {}
        result['PFPIDD'] = PFPID
        result['PFP'] = PFP
        result['UserID'] = UserID
        result['Status'] = Status
        return result

    def getAllProfilePics(self):
        dao = ProfilePicDao.ProfilePicDAO()
        ProfilePics_list = dao.getAllProfilePics()
        result_list = []
        for row in ProfilePics_list:
            result = self.build_profilepics_dict(row)
            result_list.append(result)
        return jsonify(ProfilePics=result_list)

    def getProfilePicById(self, ProfilePicID):
        dao = ProfilePicDao.ProfilePicDAO()
        row = dao.getProfilePicById(ProfilePicID)
        if not row:
            return jsonify(Error = "ProfilePic Not Found"), 404
        else:
            ProfilePics = self.build_profilepics_dict(row)
            return jsonify(ProfilePics=ProfilePics)

    def insertProfilePicJson(self, json):
            pfp = json['PFP']
            userid = json['UserID']
            status = json['Status']
            if pfp and userid and status:
                dao = ProfilePicDao.ProfilePicDAO()
                pfpid = dao.insert(pfp, userid, status)
                result = self.build_ProfilePics_attributes(pfpid, pfp, userid, status)
                return jsonify(ProfilePics=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def deleteProfilePic(self, ProfilePicid):
        dao = ProfilePicDao.ProfilePicDAO()
        if not dao.getProfilePicById(ProfilePicid):
            return jsonify(Error = "ProfilePic not found."), 404
        else:
            dao.delete(ProfilePicid)
            return jsonify(DeleteStatus = "OK"), 200

    def updateProfilePicJson(self, pfpid, json):
        dao = ProfilePicDao.ProfilePicDAO()
        if not dao.getProfilePicById(pfpid):
            return jsonify(Error="Admin not found."), 404
        else:
            pfp = json['PFP']
            userid = json['UserID']
            status = json['Status']
            if pfp and userid and status:
                dao.update(pfpid, pfp, userid, status)
                result = self.build_profilepics_attributes(pfpid, pfp, userid, status)
                return jsonify(ProfilePics=result), 200

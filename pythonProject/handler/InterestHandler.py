from flask import jsonify
from dao import InterestDao


class InterestsHandler:
    def build_interests_dict(self, row):
        result = {}
        result['InterestID'] = row[0]
        result['InterestName'] = row[1]
        result['UserID'] = row[2]
        return result

    def build_interests_attributes(self, InterestID, InterestName, UserID):
        result = {}
        result['InterestIDD'] = InterestID
        result['InterestName'] = InterestName
        result['UserID'] = UserID
        return result

    def getAllInterests(self):
        dao = InterestDao.InterestDAO()
        Interests_list = dao.getAllInterests()
        result_list = []
        for row in Interests_list:
            result = self.build_interests_dict(row)
            result_list.append(result)
        return jsonify(Interests=result_list)

    def getInterestById(self, InterestID):
        dao = InterestDao.InterestDAO()
        row = dao.getInterestById(InterestID)
        if not row:
            return jsonify(Error = "Interest Not Found"), 404
        else:
            Interests = self.build_interests_dict(row)
            return jsonify(Interests=Interests)

    def insertInterestJson(self, json):
            interestname = json['InterestName']
            userid = json['UserID']
            if interestname and userid:
                dao = InterestDao.InterestDAO()
                InterestID = dao.insert(interestname, userid)
                result = self.build_interests_attributes(InterestID, interestname, userid)
                return jsonify(Interests=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def deleteInterest(self, Interestid):
        dao = InterestDao.InterestDAO()
        if not dao.getInterestById(Interestid):
            return jsonify(Error = "Interest not found."), 404
        else:
            dao.delete(Interestid)
            return jsonify(DeleteStatus = "OK"), 200

    def updateInterestJson(self, InterestID, json):
        dao = InterestDao.InterestDAO()
        if not dao.getInterestById(InterestID):
            return jsonify(Error="Admin not found."), 404
        else:
            interestname = json['InterestName']
            userid = json['UserID']
            if interestname and userid:
                dao.update(InterestID, interestname, userid)
                result = self.build_interests_attributes(InterestID, interestname, userid)
                return jsonify(Interests=result), 200

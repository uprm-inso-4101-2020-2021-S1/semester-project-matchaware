from flask import jsonify
from dao import StatisticDao

class StatisticsHandler:
#testing
    def getTopfollowedUser(self, top):
        dao = StatisticDao.StatisticsDao()
        if top >0:
            data = dao.getTopfollowedUser(top)
            result = []
            for row in data:
                result.append(self.Dict_users(row))
            return  jsonify(result),200
        else:
            return jsonify(ERROR = "Invalid top number"),400

    def getTopfollowedOrg(self, top):
        dao = StatisticDao.StatisticsDao()
        if top > 0:
            data = dao.getTopfollowedOrg(top)
            result = []
            for row in data:
                result.append(self.Dict_organizaion(row))
            return jsonify(result), 200
        else:
            return jsonify(ERROR="Invalid top number")  ,400

    def getTopfollowedProject(self, top):
        dao = StatisticDao.StatisticsDao()
        if top > 0:
            data = dao.getTopfollowedProject(top)
            result = []
            for row in data:
                result.append(self.Dict_project(row))
            return jsonify(result), 200
        else:
            return jsonify(ERROR="Invalid top number") , 400

    def getTopviewedOrg(self, top):
        dao = StatisticDao.StatisticsDao()
        if top > 0:
            data = dao.getTopviewedOrg(top)
            result = []
            for row in data:
                result.append(self.Dict_organizaion(row))
            return jsonify(result), 200
        else:
            return jsonify(ERROR="Invalid top number"),400

    def getTopviewedProject(self, top):
        dao = StatisticDao.StatisticsDao()
        if top > 0:
            data = dao.getTopviewedProject(top)
            result = []
            for row in data:
                result.append(self.Dict_project(row))
            return jsonify(result), 200
        else:
            return jsonify(ERROR="Invalid top number"),400

    def Dict_users(self, row):
        result = {}
        result ['UserID'] = row[0]
        result['AccountTypeNumber'] = row[1]
        result['FirstName'] = row[2]
        result['LastName'] = row[3]
        result['Phone'] = row[4]
        result['Email'] = row[5]
        result['MajorNumber'] = row[6]
        result['AboutMe'] = row[7]
        result['YearOfEnrollment'] = row[8]
        result['CreationDate'] = row[9]
        result['LastLogin'] = row[10]
        result['Status'] = row[11]
        return result

    def Dict_organizaion(self, row):
        result = {}
        result['OrganizationID'] = row[0]
        result['OrganizationName'] = row[1]
        result['OrganizationDescription'] = row[2]
        result['OrganizationViewCounter'] = row[3]
        result['CreationDate'] = row[4]
        result['LastUpdate'] = row[5]
        result['Status'] = row[6]
        return result

    def Dict_project(self, row):
        result ={}
        result ['ProjectID']=row[0]
        result['ProjectTitle'] = row[1]
        result['ProjectDescription'] = row[2]
        result['ProejectViewCounter'] = row[3]
        result['CreationDate'] = row[4]
        result['LastUpdate'] = row[5]
        result['ProjectType'] = row[6]
        result['Status'] = row[7]
        return result

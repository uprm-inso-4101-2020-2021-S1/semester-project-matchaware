from flask import jsonify
from dao import CredentialDao


class CredentialHandler:
    def build_credential_dict(self, row):
        result = {}
        result['CredentialID'] = row[0]
        result['UserName'] = row[1]
        result["Password"] = row[2]
        result['UserID'] = row[3]
        result['Status'] = row[4]
        return result

    def build_credential_attributes(self, CredentialID, UserName, Password, UserID, Status):
        result = {}
        result['CredentialID'] = CredentialID
        result['UserName'] = UserName
        result["Password"] = Password
        result['UserID'] = UserID
        result['Status'] = Status
        return result

    def getAllCredentials(self):
        dao = CredentialDao.CredentialDAO()
        Credential_list = dao.getAllCredentials()
        result_list = []
        for row in Credential_list:
            result = self.build_credential_dict(row)
            result_list.append(result)
        return jsonify(Credential=result_list)

    def getCredentialById(self, CredentialID):
        dao = CredentialDao.CredentialDAO()
        row = dao.getCredentialById(CredentialID)
        if not row:
            return jsonify(Error="Credential Not Found"), 404
        else:
            Credential = self.build_credential_dict(row)
            return jsonify(Credential=Credential)

    def getCredentialByUsernameandPassword(self, Username, Password):
        dao = CredentialDao.CredentialDAO()
        row = dao.getCredentialByUsernameandPassword(Username, Password)
        if not row:
            return jsonify(Error="Credential Not Found"), 404
        else:
            Credential = self.build_credential_dict(row)
            return jsonify(Credential=Credential)

    def insertCredentialJson(self, json):
        username = json['UserName']
        password = json['Password']
        userid = json['UserID']
        status = json['Status']
        if username and password and userid and status:
            dao = CredentialDao.CredentialDAO()
            credentialid = dao.insert(username, password, userid, status)
            result = self.build_credential_attributes(credentialid, username, password, userid, status)
            return jsonify(Credential=result), 201
        else:
            return jsonify(Error="Unexpected attributes in Credential request"), 400

    def insertCredentialTestJson(self, json):
        username = json['UserName']
        password = json['Password']
        if username and password:
            userid = 1
            status = 1
            dao = CredentialDao.CredentialDAO()
            credentialid = dao.insert(username, password, userid, status)
            result = self.build_credential_attributes(credentialid, username, password, userid, status)
            return jsonify(Credential=result), 201
        else:
            return jsonify(Error="Unexpected attributes in Credential request"), 400

    def deleteCredential(self, Credentialid):
        dao = CredentialDao.CredentialDAO
        if not dao.getCredentialById(Credentialid):
            return jsonify(Error="Credential not found."), 404
        else:
            dao.delete(Credentialid)
            return jsonify(DeleteStatus="OK"), 200

    def updateCredentialJson(self, Credentialid, json):
        dao = CredentialDao.CredentialDAO()
        if not dao.getCredentialById(Credentialid):
            return jsonify(Error="Credential not found."), 404
        else:
            username = json['UserName']
            password = json['Password']
            userid = json['UserID']
            status = json['Status']
            if username and password and userid and status:
                dao.update(username, password, userid, status)
                result = self.build_credential_attributes(Credentialid, username, password, userid, status)
                return jsonify(Credential=result), 200

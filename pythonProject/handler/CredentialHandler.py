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

    def insertCredential(self, form):
        print("form: ", form)
        if len(form) != 4:
            return jsonify(Error="Malformed Credential request"), 400
        else:
            username = form['UserName']
            password = form['Password']
            userid = form['UserID']
            status = form['Status']
            if username and password and userid and status:
                dao = CredentialDao.CredentialDAO()
                credentialid = dao.insert(username, password, userid, status)
                result = self.build_credential_attributes(credentialid, username, password, userid, status)
                return jsonify(Credential=result), 201
            else:
                return jsonify(Error="Unexpected attributes in Credential request"), 400

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

    def deleteCredential(self, Credentialid):
        dao = CredentialDao.CredentialDAO
        if not dao.getCredentialById(Credentialid):
            return jsonify(Error="Credential not found."), 404
        else:
            dao.delete(Credentialid)
            return jsonify(DeleteStatus="OK"), 200

    def updateCredential(self, Credentialid, form):
        dao = CredentialDao.CredentialDAO()
        if not dao.getCredentialById(Credentialid):
            return jsonify(Error="Credential not found."), 404
        else:
            if len(form) != 4:
                return jsonify(Error="Malformed update request"), 400
            else:
                username = form['UserName']
                password = form['Password']
                userid = form['UserID']
                status = form['Status']
                if username and password and userid and status:
                    dao.update(username, password, userid, status)
                    result = self.build_credential_attributes(Credentialid, username, password, userid, status)
                    return jsonify(Credential=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400

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

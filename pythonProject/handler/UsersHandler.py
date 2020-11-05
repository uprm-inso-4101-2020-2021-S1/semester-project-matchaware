from flask import jsonify
from dao import UserDao


class UsersHandler:
    def build_users_dict(self, row):
        result = {}
        result['UserID'] = row[0]
        result['AccountTypeNumber'] = row[1]
        result['FirstName'] = row[2]
        result['LastName'] = row[3]
        result['Phone'] = row[4]
        result['Email'] = row[5]
        result['Major'] = row[6]
        result['Status'] = row[7]
        return result

    def build_users_attributes(self, UserID, AccountTypeNumber,  FirstName, LastName, Phone, Email, umajor):
        result = {}
        result['UserID'] = UserID
        result['AccountTypeNumber'] = AccountTypeNumber
        result['FirstName'] = FirstName
        result['LastName'] = LastName
        result['Phone'] = Phone
        result['Email'] = Email
        result['major'] = umajor
        return result

    def getAllUsers(self):
        dao = UserDao.UserDAO()
        users_list = dao.getAllUsers()
        result_list = []
        for row in users_list:
            result = self.build_users_dict(row)
            result_list.append(result)
        return jsonify(Users=result_list)

    def getUserById(self, UserID):
        dao = UserDao.UserDAO()
        row = dao.getUserById(UserID)
        if not row:
            return jsonify(Error = "User Not Found"), 404
        else:
            users = self.build_users_dict(row)
            return jsonify(Users = users)


    # def insertUser(self, form):
    #     print("form: ", form)
    #     if len(form) != 6:
    #         return jsonify(Error = "Malformed post request"), 400
    #     else:
    #         accounttypenumber = form['AccountTypeNumber']
    #         firstname = form['FirstName']
    #         lastname = form['LastName']
    #         phone = form['Phone']
    #         email = form['Email']
    #         umajor = form['umajor']
    #
    #         if accounttypenumber and firstname and lastname and phone and email and umajor:
    #             dao = UserDao.UserDAO()
    #             userid = dao.insert(accounttypenumber, firstname, lastname, phone, email, umajor)
    #             result = self.build_users_attributes(userid, accounttypenumber, firstname, lastname, phone, email, umajor)
    #             return jsonify(Users=result), 201
    #         else:
    #             return jsonify(Error="Unexpected attributes in post request"), 400

    def insertUserJson(self, form):
        if len(form) != 6:
            return jsonify(Error="Malformed post request"), 400
        else:
            accounttypenumber = form['AccountTypeNumber']
            firstname = form['FirstName']
            lastname = form['LastName']
            phone = form['Phone']
            email = form['Email']
            umajor = form['Major']

            if accounttypenumber and firstname and lastname and phone and email and umajor:
                dao = UserDao.UserDAO()
                userid = dao.insert(accounttypenumber, firstname, lastname, phone, email, umajor)
                result = self.build_users_attributes(userid, accounttypenumber, firstname, lastname, phone, email,
                                                     umajor)
                return jsonify(Users=result), 201

    def deleteUser(self, userid):
        dao = UserDao.UserDAO()
        if not dao.getUserById(userid):
            return jsonify(Error = "User not found."), 404
        else:
            dao.delete(userid)
            return jsonify(DeleteStatus = "OK"), 200

    def updateUser(self, userid, form):
        dao = UserDao.UserDAO()
        if not dao.getUserById(userid):
            return jsonify(Error = "User not found."), 404
        else:
            if len(form) != 7:
                return jsonify(Error="Malformed update request"), 400
            else:
                accounttypenumber = form['AccountTypeNumber']
                firstname = form['FirstName']
                lastname = form['LastName']
                phone = form['Phone']
                email = form['Email']
                gender = form['Gender']
                status = form['Status']
                if accounttypenumber and firstname and lastname and phone and email and gender and status:
                    dao.update(accounttypenumber, firstname, lastname, phone, email, gender, status,)
                    result = self.build_users_attributes(userid, accounttypenumber, firstname, lastname, phone, email, gender, status)
                    return jsonify(Users=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400

    def updateUserJson(self, userid, json):
        dao = UserDao.UserDAO()
        if not dao.getUserById(userid):
            return jsonify(Error="Admin not found."), 404
        else:
            accounttypenumber = json['AccountTypeNumber']
            firstname = json['FirstName']
            lastname = json['LastName']
            phone = json['Phone']
            email = json['Email']
            gender = json['Gender']
            status = json['Status']
            if accounttypenumber and firstname and lastname and phone and email and gender and status:
                dao.update(accounttypenumber, firstname, lastname, phone, email, gender, status)
                result = self.build_users_attributes(userid, accounttypenumber, firstname, lastname, phone, email, gender, status)
                return jsonify(Users=result), 200
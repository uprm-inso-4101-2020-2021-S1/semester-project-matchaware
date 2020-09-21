from flask import jsonify
from dao.UserDao import UserDao
class UserHandler:
    def user_dic(self, row):
        result = {}
        result['userid'] = row[0]
        result['name'] = row[1]
        return result

    def insertUserJson(self, form):
        dao = UserDao()
        values = dao.insertUser()

        result = []
        for row in values:
            result.append(self.user_dic(row))
        return jsonify(User=result)
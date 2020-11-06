from flask import jsonify
from dao import MemberDao



class MemberHandler:
    def build_member_dict(self, row):
        result = {}
        result['MemberID'] = row[0]
        result['ProjectID'] = row[1]
        result["UserID"] = row[2]
        result['RoleTypeNumber'] = row[3]
        result['Status'] = row[4]
        return result

    def build_member_attributes(self, MemberID, ProjectID, UserID, RoleNumber, Status):
        result = {}
        result['MemberID'] = MemberID
        result['ProjectID'] = ProjectID
        result["UserID"] = UserID
        result['RoleTypeNumber'] = RoleNumber
        result['Status'] = Status
        return result

    def getAllMembers(self):
        dao = MemberDao.MemberDAO()
        Member_list = dao.getAllMembers()
        result_list = []
        for row in Member_list:
            result = self.build_member_dict(row)
            result_list.append(result)
        return jsonify(Member=result_list)

    def getMemberById(self, memberID):
        dao = MemberDao.MemberDAO()
        row = dao.getMemberById(memberID)
        if not row:
            return jsonify(Error = "Member Not Found"), 404
        else:
            Member = self.build_member_dict(row)
            return jsonify(Member = Member)

    def insertMemberJson(self, json):
        projectid = json['ProjectID']
        userid = json['UserID']
        rolenumber = json['RoleTypeNumber']
        status = json['Status']
        if projectid and userid and rolenumber and status:
            dao = MemberDao.MemberDAO()
            memberid = dao.insert(projectid, userid, rolenumber, status)
            result = self.build_member_attributes(memberid, projectid, userid, rolenumber, status)
            return jsonify(Member=result), 201
        else:
            return jsonify(Error="Unexpected attributes in Member request"), 400

    def deleteMember(self, memberid):
        dao = MemberDao.MemberDAO
        if not dao.getMemberById(memberid):
            return jsonify(Error = "Member not found."), 404
        else:
            dao.delete(memberid)
            return jsonify(DeleteStatus = "OK"), 200

    def updateMemberJson(self, Memberid, json):
        dao = MemberDao.MemberDAO()
        if not dao.getMemberById(Memberid):
            return jsonify(Error="Member not found."), 404
        else:
            projectid = json['ProjectID']
            userid = json['UserID']
            rollnumber = json['RollTypeNumber']
            status = json['Status']
            if projectid and userid and rollnumber and status:
                dao.update(projectid, userid, rollnumber, status)
                result = self.build_member_attributes(projectid, projectid, userid, rollnumber, status)
                return jsonify(Member=result), 200
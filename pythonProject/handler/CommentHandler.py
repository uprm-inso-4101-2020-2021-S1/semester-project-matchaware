from flask import jsonify
from dao import CommentDao


class CommentsHandler:
    def build_comments_dict(self, row):
        result = {}
        result['CommentID'] = row[0]
        result['PostID'] = row[1]
        result['CommentText'] = row[2]
        result['UserID'] = row[3]
        result['CommentDate'] = row[4]
        result['CommentStatus'] = row[5]
        return result

    def build_comments_attributes(self, CommentID, PostID, CommentText, UserID, CommentDate, CommentStatus):
        result = {}
        result['CommentID'] = CommentID
        result['PostID'] = PostID
        result['CommentText'] = CommentText
        result['UserID'] = UserID
        result['CommentDate'] = CommentDate
        result['CommentStatus'] = CommentStatus
        return result

    def getAllComments(self):
        dao = CommentDao.CommentDao()
        Comments_list = dao.getAllComments()
        result_list = []
        for row in Comments_list:
            result = self.build_comments_dict(row)
            result_list.append(result)
        return jsonify(Comments=result_list)

    def getCommentById(self, CommentID):
        dao = CommentDao.CommentDao()
        row = dao.getCommentById(CommentID)
        if not row:
            return jsonify(Error="Comment Not Found"), 404
        else:
            Comments = self.build_comments_dict(row)
            return jsonify(Comments=Comments)

    def insertCommentJson(self, json):
        PostID = json['PostID']
        CommentText = json['CommentText']
        UserID = json['UserID']
        CommentDate = json['CommentDate']
        CommentStatus = json['CommentStatus']
        if PostID and CommentText and UserID and CommentDate and CommentStatus:
            dao = CommentDao.CommentDao()
            CommentID = dao.insert(PostID, CommentText, UserID, CommentDate, CommentStatus)
            result = self.build_comments_attributes(CommentID,
                                                    PostID, CommentText, UserID, CommentDate, CommentStatus)
            return jsonify(Comments=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400


    def deleteComment(self, Commentid):
        dao = CommentDao.CommentDao()
        if not dao.getCommentById(Commentid):
            return jsonify(Error="Comment not found."), 404
        else:
            dao.delete(Commentid)
            return jsonify(DeleteStatus="OK"), 200

    def updateCommentJson(self, CommentID, json):
        dao = CommentDao.CommentDao()
        if not dao.getCommentById(CommentID):
            return jsonify(Error="Admin not found."), 404
        else:
            PostID = json['PostID']
            CommentText = json['CommentText']
            UserID = json['UserID']
            CommentDate = json['CommentDate']
            CommentStatus = json['CommentStatus']
            if PostID and CommentText and UserID and CommentDate and CommentStatus:
                dao.update(CommentID, PostID, CommentText, UserID, CommentDate, CommentStatus)
                result = self.build_comments_attributes(CommentID, PostID, CommentText, UserID, CommentDate, CommentStatus)
                return jsonify(Comments=result), 200

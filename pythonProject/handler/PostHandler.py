from flask import jsonify
from dao import PostDao



class PostHandler:
    def build_post_dict(self, row):
        result = {}
        result['PostID'] = row[0]
        result['PostText'] = row[1]
        result["UserID"] = row[2]
        result['PostDate'] = row[3]
        result['Status'] = row[4]
        return result

    def build_post_attributes(self, PostID, PostText, UserID, PostDate, Status):
        result = {}
        result['PostID'] = PostID
        result['PostText'] = PostText
        result["UserID"] = UserID
        result['PostDate'] = PostDate
        result['Status'] = Status
        return result

    def getAllPosts(self):
        dao = PostDao.PostDAO()
        Post_list = dao.getAllPosts()
        result_list = []
        for row in Post_list:
            result = self.build_post_dict(row)
            result_list.append(result)
        return jsonify(Post=result_list)

    def getPostById(self, PostID):
        dao = PostDao.PostDAO()
        row = dao.getPostById(PostID)
        if not row:
            return jsonify(Error = "Post Not Found"), 404
        else:
            Post = self.build_post_dict(row)
            return jsonify(Post = Post)

    def insertPostJson(self, json):
        posttext = json['PostText']
        userid = json['UserID']
        postdate = json['PostDate']
        status = json['Status']
        if posttext and userid and postdate and status:
            dao = PostDao.PostDAO()
            postid = dao.insert(posttext, userid, postdate, status)
            result = self.build_post_attributes(postid, posttext, userid, postdate, status)
            return jsonify(Post=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

    def deletePost(self, postid):
        dao = PostDao.PostDAO
        if not dao.getPostById(postid):
            return jsonify(Error = "Post not found."), 404
        else:
            dao.delete(postid)
            return jsonify(DeleteStatus = "OK"), 200

    def updatePostJson(self, postid, json):
        dao = PostDao.PostDAO()
        if not dao.getPostById(postid):
            return jsonify(Error="Post not found."), 404
        else:
            posttext = json['PostText']
            userid = json['UserID']
            date = json['Date']
            status = json['Status']
            if posttext and userid and date and status:
                dao.update(posttext, userid, date, status)
                result = self.build_post_attributes(postid, posttext, userid, date, status)
                return jsonify(Post=result), 200
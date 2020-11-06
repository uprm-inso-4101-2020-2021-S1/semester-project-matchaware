from flask import jsonify
from dao import ImageDao


class ImagesHandler:
    def build_images_dict(self, row):
        result = {}
        result['ImageID'] = row[0]
        result['ImageName'] = row[1]
        result['Image'] = row[2]
        result['ImageStatus'] = row[3]
        result['PostID'] = row[4]
        return result

    def build_images_attributes(self, ImageID, ImageName, Image, ImageStatus, PostID):
        result = {}
        result['ImageID'] = ImageID
        result['ImageName'] = ImageName
        result['Image'] = Image
        result['ImageStatus'] = ImageStatus
        result['PostID'] = PostID
        return result

    def getAllImages(self):
        dao = ImageDao.ImageDao()
        Images_list = dao.getAllImages()
        result_list = []
        for row in Images_list:
            result = self.build_images_dict(row)
            result_list.append(result)
        return jsonify(Images=result_list)

    def getImageById(self, ImageID):
        dao = ImageDao.ImageDao()
        row = dao.getImageById(ImageID)
        if not row:
            return jsonify(Error="Image Not Found"), 404
        else:
            Images = self.build_images_dict(row)
            return jsonify(Images=Images)

    def insertImageJson(self, json):
        ImageName = json['ImageName']
        Image = json['Image']
        ImageStatus = json['ImageStatus']
        PostID = json['PostID']
        if ImageName and Image and ImageStatus and PostID:
            dao = ImageDao.ImageDao()
            imageid = dao.insert(ImageName, Image, ImageStatus, PostID)
            result = self.build_images_attributes(imageid, ImageName, Image, ImageStatus, PostID)
            return jsonify(Images=result), 201

    def deleteImage(self, Imageid):
        dao = ImageDao.ImageDao()
        if not dao.getImageById(Imageid):
            return jsonify(Error="Image not found."), 404
        else:
            dao.delete(Imageid)
            return jsonify(DeleteStatus="OK"), 200

    def updateImageJson(self, ImageID, json):
        dao = ImageDao.ImageDao()
        if not dao.getImageById(ImageID):
            return jsonify(Error="Image not found."), 404
        else:
            ImageName = json['ImageName']
            Image = json['Image']
            ImageStatus = json['ImageStatus']
            PostID = json['PostID']
            if ImageName and Image and ImageStatus and PostID:
                dao.update(ImageName, Image, ImageStatus, PostID)
                result = self.build_images_attributes(ImageID, ImageName, Image, ImageStatus, PostID)
                return jsonify(Image=result), 200

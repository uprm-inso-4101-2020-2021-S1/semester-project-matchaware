from flask import jsonify
from dao import MessagesDao


class MessagesHandler:
#testing
    def build_message_dict(self, row):
        result = {}
        result['MessageID'] = row[0]
        result['ReceiverID'] = row[1]
        result["SenderID"] = row[2]
        result['MessageText'] = row[3]
        result['MessageDate'] = row[4]
        return result

    def build_message_attributes(self, MessageID, ReceiverID, SenderID, MessageText, DateTime, Status):
        result = {}
        result['MessageID'] = MessageID
        result['ReceiverID'] = ReceiverID
        result["SenderID"] = SenderID
        result['MessageText'] = MessageText
        result['MessageDate'] = DateTime
        result['Status'] = Status
        return result

    def getAllMessagess(self):
        dao = MessagesDao.MessageDao()
        Messages_list = dao.getAllMessages()
        result_list = []
        for row in Messages_list:
            result = self.build_message_dict(row)
            result_list.append(result)
        return jsonify(Messages=result_list)

    def insertMessageJson(self, json):
            ReceiverID = json['ReceiverID']
            SenderID = json['SenderID']
            MessageText = json['MessageText']
            MessageDate = json['MessageDate']
            Status = json['Status']

            if ReceiverID and SenderID and MessageText and MessageDate and Status:
                dao = MessagesDao.MessageDao()
                messageid = dao.insertMessage(ReceiverID, SenderID, MessageText, MessageDate,Status,)

                return jsonify(messageid=messageid), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def getMessagesBetweenUsers(self,json):
        ReceiverID = json['ReceiverID']
        SenderID = json['SenderID']

        if (ReceiverID and SenderID):
            dao = MessagesDao.MessageDao()
            data = dao.getMessageBetweenUsers(ReceiverID,SenderID)
            results = []
            for row in data:
                results.append(self.build_message_dict(row))

            return jsonify(Results=results), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

    def deleteAllMessagesbetweenUsers(self,json ):
        ReceiverID = json['ReceiverID']
        SenderID = json['SenderID']

        if (ReceiverID and SenderID):
            dao = MessagesDao.MessageDao()
            status = dao.deleteAllMessageBetweenUsers(ReceiverID, SenderID)


            return jsonify(Status= status), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

    def deleteAMessagesbetweenUsers(self, json):
        ReceiverID = json['ReceiverID']
        SenderID = json['SenderID']
        MessageID = json['MessageID']

        if (ReceiverID and SenderID and MessageID):
            dao = MessagesDao.MessageDao()
            status = dao.deleteAMessageBetweenUsers(ReceiverID, SenderID,MessageID)

            return jsonify(Status=status), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

    def searchMesagesBetweenUsersKeyword(self,json):
        ReceiverID = json['ReceiverID']
        SenderID = json['SenderID']
        Keyword = json['Keyword']

        if (ReceiverID and SenderID and Keyword):
            dao = MessagesDao.MessageDao()
            data = dao.searchInMessages(ReceiverID, SenderID, Keyword)
            results = []
            for row in data:
                results.append(self.build_message_dict(row))

            return jsonify(Results=results), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400
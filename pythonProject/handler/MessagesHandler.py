from flask import jsonify
from dao import MessagesDao


class MessagesHandler:

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



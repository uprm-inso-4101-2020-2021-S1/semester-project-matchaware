from flask import jsonify
from dao import MessagesDao


class MessagesHandler:

    def build_message_dict(self, row):
        result = {}
        result['MessageID'] = row[0]
        result['ReceiverID'] = row[1]
        result["SenderID"] = row[2]
        result['MessageText'] = row[3]
        result['DateTime'] = row[4]
        return result

    def build_message_attributes(self, MessageID, ReceiverID, SenderID, MessageText, DateTime):
        result = {}
        result['MessageID'] = MessageID
        result['ReceiverID'] = ReceiverID
        result["SenderID"] = SenderID
        result['MessageText'] = MessageText
        result['DateTime'] = DateTime
        return result

    def getAllMessagess(self):
        dao = MessagesDao.MessageDao()
        Messages_list = dao.getAllMessages()
        result_list = []
        for row in Messages_list:
            result = self.build_message_dict(row)
            result_list.append(result)
        return jsonify(Messages=result_list)

    def insertMessageJson(self, form):
        if form and len(form) == 4:
            ReceiverID = form['ReceiverID']
            SenderID = form['SenderID']
            MessageText = form['MessageText']
            DateTime = form['DateTime']

            if ReceiverID and SenderID and MessageText and DateTime:
                dao = MessagesDao.MessageDao()
                messageid = dao.insertMessage(ReceiverID, SenderID, MessageText,DateTime,)

                return jsonify(messageid=messageid), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400



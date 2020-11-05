
from flask import jsonify
from dao.MessagesDao import MessagesDao

class MessagesHandler:

    def insertMessageJson(self, form) :
        if form and len(form)==4:
            receptor = form['receptor']
            emisor = form['emisor']
            messagetext = form['messagetext']
            date = form['date']

            if receptor and emisor and messagetext and date:
                dao = MessagesDao()
                messageid = dao.insertMessage(receptor,emisor,messagetext,date)

                return jsonify(messageid=messageid), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400



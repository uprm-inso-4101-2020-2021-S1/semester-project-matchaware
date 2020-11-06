import MySQLdb


class MessageDao:
    # fix this url crap tonight
    def __init__(self):
        connection_url = MySQLdb.connect(host="localhost", user='root', passwd='root', db='BeyondHorizonsDB')
        self.conn = connection_url

    def getAllMessages(self):
        cursor = self.conn.cursor()
        query = "select * from Messages;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insertMessage(self, ReceiverID, SenderID, MessageText, DateTime, Status):
        cursor = self.conn.cursor()
        query = "INSERT INTO Messages(receiverid, senderid, messagetext, messagedate, status) values(%s,%s,%s,%s, %s) ;"
        cursor.execute(query, (ReceiverID, SenderID, MessageText, DateTime, Status))
        query = "SELECT LAST_INSERT_ID();"
        cursor.execute(query)
        messageid = cursor.fetchall()[0]
        self.conn.commit()
        return messageid

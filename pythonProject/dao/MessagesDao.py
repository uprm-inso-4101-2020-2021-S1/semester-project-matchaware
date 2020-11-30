#import MySQLdb
import pymysql


class MessageDao:
    # fix this url crap tonight
    def __init__(self):
        #connection_url = MySQLdb.connect(host='24.54.205.36', user='RemoteMatcha', passwd='RemoteMatcha',
        #                                 db='BeyondHorizonsDB', port=6606)

        connection_url = pymysql.connect(host="localhost", user='Argent', passwd='ArgentSable776',
                                         db='BeyondHorizonsDB')
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

    def getMessageBetweenUsers(self, ReceiverID,SenderID):
        cursor = self.conn.cursor()
        query = "select * from Messages where receiberid = %s and Senderid = %s and status  = 1 ;"
        cursor.execute(query, (ReceiverID,SenderID))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def deleteAllMessageBetweenUsers(self, ReceiverID, SenderID): #assuming status 2 = deleted and 1 is active
        cursor = self.conn.cursor()
        query = "UPDATE Messages SET status = 2 where receiberid = %s and Senderid = %s and status  = 1 ;"
        cursor.execute(query, (ReceiverID, SenderID))
        result = 2
        return result

    def deleteAMessageBetweenUsers(self,ReceiverID, SenderID,MessageID):
        cursor = self.conn.cursor()
        query = "UPDATE Messages SET status = 2 where receiberid = %s and Senderid = %s and messageid=%s and status=1;"
        cursor.execute(query, (ReceiverID, SenderID, MessageID))
        result = 2
        return result

    def searchInMessages(self,ReceiverID, SenderID, keyword):
        cursor = self.conn.cursor()
        query = "select * from Messages where receiberid = %s and Senderid = %s  and messageText LIKE %%s% and status  = 1 ;"
        cursor.execute(query, (ReceiverID, SenderID,keyword))
        result = []
        for row in cursor:
            result.append(row)
        return result

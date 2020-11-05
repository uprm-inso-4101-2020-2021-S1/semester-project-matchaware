import MySQLdb



class MessagesDao:
    # fix this url crap tonight
    def __init__(self):
        connection_url = MySQLdb.connect(host="localhost", user='root', passwd='root', db='BeyondHorizonsDB')
        self.conn = connection_url

    def insertMessage(self, receptor, emisor, messagetext,date):
        cursor = self.conn.cursor()
        query = "INSERT INTO message(receptorid,emisorid, messagetext,  mdate) values(%s,%s,%s,%s) ;"
        cursor.execute(query,(receptor,emisor,messagetext,date))
        query = "SELECT LAST_INSERT_ID();"
        cursor.execute(query)
        messageid = cursor.fetchall()[0]
        self.conn.commit()
        return messageid
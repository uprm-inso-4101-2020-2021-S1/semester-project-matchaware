import MySQLdb

class UserDAO:
    #fix this url crap tonight
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s host=127.0.0.1" % (pg_config['dbname'], pg_config['user'], pg_config['passwd'])
        self.conn = MySQLdb.connect(connection_url)

    def getAllUsers(self):
        cursor = self.conn.cursor()
        query = "select * from Users;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUserById(self, UserID):
        cursor = self.conn.cursor()
        query = "select * from Users Where userid = %s;"
        cursor.execute(query, (UserID,))
        result = cursor.fetchone()
        return result

    def getUserbyEmail(self, Email):
        cursor = self.conn.cursor()
        query = "select * from Users where email = %s;"
        cursor.execute(query, (Email,))
        result = []
        for row in cursor:
            result.append(row)
        return result



    def insert(self, accounttypenumber, firstname, lastname, phone, email, gender, status):
        cursor = self.conn.cursor()
        query = "insert into Users( accounttypenumber, firstname, lastname, phone, email, gender, status) values (%s, %s, %s, %s, %s, %s, %s) returning userid;"
        cursor.execute(query, (accounttypenumber, firstname, lastname, phone, email, gender, status,))
        userid = cursor.fetchone()[0]
        self.conn.commit()
        return userid

    def delete(self, UserID):
        cursor = self.conn.cursor()
        query = "delete from Users where userid = %s;"
        cursor.execute(query, (UserID,))
        self.conn.commit()
        return UserID

    def update(self, UserID, accounttypenumber, firstname, lastname, phone, email, gender, status):
        cursor = self.conn.cursor()
        query = "update users set username = %s, password = %s, email = %s, cardid = %s, ulocation = %s, firstname = %s, lastname = %s, dateofbirth = %s, gender = %s where userid = %s;"
        cursor.execute(query, (accounttypenumber, firstname, lastname, phone, email, gender, status, UserID,))
        self.conn.commit()
        return UserID
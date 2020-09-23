
import MySQLdb

class UserDao:

    def getUser(self):
        miConexion = MySQLdb.connect(host ="localhost", user = 'IngShiroe_user', passwd='root', db='testdb')

        cur = miConexion.cursor();
        cur.execute("Select * from test")
        results = cur.fetchall()

        miConexion.close()
        return results
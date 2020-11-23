import pymysql

class mysql(object):

    def __init__(self, host, user, passwd, db):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.db = db

    def connection(self):
        myConnection = pymysql.connect(
            host = self.host, user = self.user,
            passwd = self.passwd, db = self.db)
        return myConnection

    def close(self, myConnection):
        myConnection.close()
    
    def mysql_query(self,myConnection, field, table):
        values = []
        mysql = myConnection.cursor()
        sql = "select {} from {}".format(field, table)
        mysql.execute(sql)
        queries = mysql.fetchall()
        for value in queries:
            value = value[0]
            values.append(value)
        return values

    def mysql_write_comm(self,myConnection, idcomment, idsite, username, nd_comment, times):
        mysql = myConnection.cursor()
        sql = "insert into comment (idcomment, idsite, username, nd_comment, times) values ('{}', {}, '{}', '{}', '{}')"\
        .format(idcomment, idsite, username, nd_comment, times)
        mysql.execute(sql)
        myConnection.commit()

    def mysql_get_id(self,myConnection, id, table, field, value):
        mysql = myConnection.cursor()
        sql = "select {} from {} where {}='{}'".format(id, table, field, value)
        mysql.execute(sql)
        value = mysql.fetchall()
        id_value = value[0][0]
        return id_value

    def mysql_write_site(self,myConnection, url, tieude):
        mysql = myConnection.cursor()
        sql = "insert into site (links, tieude) values ('{}', '{}')"\
        .format(url, tieude)
        mysql.execute(sql)
        myConnection.commit()
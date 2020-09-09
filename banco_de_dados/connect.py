import MySQLdb

host = "localhost"
user = "root"
password = ""
db = "escola_curso"
port = 3306

connection = MySQLdb.connect(host, user, password, db, port)

c = connection.cursor(MySQLdb.cursors.DictCursor)


def isRealNumber(target):
    
    flag = True
    
    try:
        int(target)
    except:
        try:
            float(target)
        except:
            flag = False
    
    return flag

def select(fields, tables, where=None, group=None, order=None):

    global c
    query = "SELECT " + fields + " FROM " + tables
    if(where):
        query += " WHERE "+ where
    if(group):
        query += " GROUP BY "+ where
    if(order):
        query += " ORDER BY "+ where

    #print(query)
    c.execute(query)
    return(c.fetchall())

def insert(values, table, fields=None):
    
    global c, connection

    query = "INSERT INTO " + table + " "
    if(fields):
        query += "(" + fields + ") "
    query += "VALUES " + ",".join([ "(" + v + ")" for v in values]) 

    #print(query)
    c.execute(query)
    connection.commit()

def update(sets, table, where=None):
    
    global c, connection

    query = "UPDATE " + table + " SET "
    query += ", ".join([field + " = " + (("" + value) if isRealNumber(value) else ("'" + value +"'"))  for field, value in sets.items()])
    if(where):
        query += " WHERE " + where

    #print(query)
    c.execute(query)
    connection.commit()


def delete(table, where=None):

    global c, connection

    query = "DELETE FROM " + table
    if(where):
        query += " WHERE "+where

    #print(query)
    c.execute(query)
    connection.commit()


# print(select("*", "alunos"))
# insert(["DEFAULT, 'Igor', '1993-05-07', 'Rua A, 21', 'Paulo Afonso', 'Bahia', '91827364534' "] , "alunos")
# update({"nome":"João Martins", "cidade": 'Curitiba'}, "alunos", "id_aluno = 2")
delete("alunos", "id_aluno = 6")


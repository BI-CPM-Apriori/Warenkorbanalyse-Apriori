import pyodbc

def openConn():
    server_name = 'NB-DK-DELL\SQLEXPRESS' 
    db_name = 'AdventureWorks2019' 
    connection_str =  'Driver={SQL Server};' + 'Server=' + server_name + ";Database=" + db_name + ";Trusted_Connection=yes;"

    try:
        conn = pyodbc.connect(connection_str)
    except:
        print("conn failed")

    return conn

def closeConn(conn):
    conn.close()
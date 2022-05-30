import pyodbc

def openConn():

    # lokales Servername ('[Rechnername]\SQLEXPRESS') für MS SQL Server Express
    rechner_name = 'NB-DK-DELL'
    server_name = rechner_name + '\SQLEXPRESS' 
    db_name = 'AdventureWorks2019' 
    connection_str =  'Driver={SQL Server};' + 'Server=' + str(server_name) + ";Database=" + str(db_name) + ";Trusted_Connection=yes;"

    try:
        conn = pyodbc.connect(connection_str)
    except:
        print("conn failed")

    return conn

def closeConn(conn):
    conn.close()
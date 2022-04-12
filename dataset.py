import dbConnection
import read

def createDataset(x):
    dataset = []
    innerList = []

    conn = dbConnection.openConn()
    cursor = conn.cursor()

    if x == "1":
        sql = read.getProducts()
    elif x == "2":
        sql = read.getCategories()

    cursor.execute(sql) 
    row = cursor.fetchone()
    lastID = row[0]
    while row: 
        if lastID == row[0]:
            innerList.append(row[1])
        else:
            dataset.append(innerList)
            innerList = []
            innerList.append(row[1])

        lastID = row[0]
        row = cursor.fetchone()

    return dataset
    dbConnection.closeConn(conn)
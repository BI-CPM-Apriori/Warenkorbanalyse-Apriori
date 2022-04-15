from Database import dbConnection, read

def createDataset(param):
    dataset = []
    innerList = []

    conn = dbConnection.openConn()
    cursor = conn.cursor()

    if param == "1":
        sql = read.getProductsAll()
    elif param == "2":
        sql = read.getProductsByCountry("9")
    elif param == "3":
        sql = read.getCategoriesAll()


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
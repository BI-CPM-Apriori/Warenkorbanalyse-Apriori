from Database import dbConnection, read

def createDataset(filter, country, saison):
    dataset = []
    innerList = []

    conn = dbConnection.openConn()
    cursor = conn.cursor()
    if filter == "product":
        if country == "All" and saison == "All":
            sql = read.getProductsAll()
        elif country == "All":
            sql = read.getProductsBySaison(saison)
        elif saison == "All":
            sql = read.getProductsByCountry(country)
        else:
            sql = read.getProductsByCountryAndSaison(country, saison)
    else:
        if country == "All" and saison == "All":
            sql = read.getCategoriesAll()
        elif country == "All":
            sql = read.getCategoriesBySaison(saison)
        elif saison == "All":
            sql = read.getCategoriesByCountry(country)
        else:
            sql = read.getCategoriesByCountryAndSaison(country, saison)
            


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
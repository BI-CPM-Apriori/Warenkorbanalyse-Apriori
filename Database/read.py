def getProductName(productID):
    sql = "SELECT [AdventureWorks2019].[Production].[Product].[Name] FROM [AdventureWorks2019].[Production].[Product] WHERE [AdventureWorks2019].[Production].[Product].[ProductID] = " + str(productID) + ";"

    return sql

def getProductPhoto(productID):
    sql = "SELECT [AdventureWorks2019].[Production].[ProductPhoto].[LargePhoto] FROM [AdventureWorks2019].[Production].[Product], [AdventureWorks2019].[Production].[ProductPhoto], [AdventureWorks2019].[Production].[ProductProductPhoto] WHERE [AdventureWorks2019].[Production].[Product].[ProductID] = [AdventureWorks2019].[Production].[ProductProductPhoto].ProductID AND [AdventureWorks2019].[Production].[ProductPhoto].[ProductPhotoID] = [AdventureWorks2019].[Production].[ProductProductPhoto].[ProductPhotoID] AND [AdventureWorks2019].[Production].[Product].[ProductID] = " + str(productID) + ";"

    return sql

def getProductsAll():
    sql = "SELECT [AdventureWorks2019].[Sales].[SalesOrderDetail].[SalesOrderID], [AdventureWorks2019].[Sales].[SalesOrderDetail].[ProductID] FROM [AdventureWorks2019].[Sales].[SalesOrderDetail] ORDER BY [SalesOrderID] ASC;"

    return sql

def getProductsByCountry(country):
    sql = "SELECT [AdventureWorks2019].[Sales].[SalesOrderDetail].[SalesOrderID], [AdventureWorks2019].[Sales].[SalesOrderDetail].[ProductID] FROM [AdventureWorks2019].[Sales].[SalesOrderHeader], [AdventureWorks2019].[Sales].[SalesOrderDetail] WHERE [AdventureWorks2019].[Sales].[SalesOrderDetail].[SalesOrderID] = [AdventureWorks2019].[Sales].[SalesOrderHeader].[SalesOrderID]  AND [AdventureWorks2019].[Sales].[SalesOrderHeader].[TerritoryID] IN(" + getCountryID(country) + ") ORDER BY [SalesOrderID] ASC;"

    return sql

def getProductsBySaison(saison):

    sql = "SELECT [AdventureWorks2019].[Sales].[SalesOrderDetail].[SalesOrderID], [AdventureWorks2019].[Sales].[SalesOrderDetail].[ProductID] FROM [AdventureWorks2019].[Sales].[SalesOrderDetail] WHERE " + getQuartal(saison) + " ORDER BY [SalesOrderID] ASC;"

    return sql

def getProductsByCountryAndSaison(country, saison):

    sql = "SELECT [AdventureWorks2019].[Sales].[SalesOrderDetail].[SalesOrderID], [AdventureWorks2019].[Sales].[SalesOrderDetail].[ProductID] FROM [AdventureWorks2019].[Sales].[SalesOrderHeader], [AdventureWorks2019].[Sales].[SalesOrderDetail] WHERE [AdventureWorks2019].[Sales].[SalesOrderDetail].[SalesOrderID] = [AdventureWorks2019].[Sales].[SalesOrderHeader].[SalesOrderID]  AND [AdventureWorks2019].[Sales].[SalesOrderHeader].[TerritoryID] IN(" + getCountryID(country) + ") AND ("+ getQuartal(saison) +") ORDER BY [SalesOrderID] ASC;"

    return sql

def getCategoriesAll():
    sql = "SELECT DISTINCT [AdventureWorks2019].[Sales].[SalesOrderDetail].[SalesOrderID], [AdventureWorks2019].[Production].[ProductCategory].[ProductCategoryID]  FROM [AdventureWorks2019].[Sales].[SalesOrderDetail], [AdventureWorks2019].[Production].[Product], [AdventureWorks2019].[Production].[ProductSubcategory], [AdventureWorks2019].[Production].[ProductCategory] WHERE [AdventureWorks2019].[Sales].[SalesOrderDetail].[ProductID] = [AdventureWorks2019].[Production].[Product].[ProductID]  AND [AdventureWorks2019].[Production].[Product].[ProductSubcategoryID] = [AdventureWorks2019].[Production].[ProductSubcategory].[ProductSubcategoryID] AND [AdventureWorks2019].[Production].[ProductCategory].[ProductCategoryID] = [AdventureWorks2019].[Production].[ProductSubcategory].[ProductCategoryID] ORDER BY [AdventureWorks2019].[Sales].[SalesOrderDetail].[SalesOrderID] ASC;"

    return sql

def getCategoriesByCountry(country):
    sql = "SELECT DISTINCT [AdventureWorks2019].[Sales].[SalesOrderDetail].[SalesOrderID], [AdventureWorks2019].[Production].[ProductSubcategory].[Name] FROM [AdventureWorks2019].[Sales].[SalesOrderHeader], [AdventureWorks2019].[Sales].[SalesOrderDetail], [AdventureWorks2019].[Production].[Product], [AdventureWorks2019].[Production].[ProductSubcategory] WHERE [AdventureWorks2019].[Sales].[SalesOrderDetail].[SalesOrderID] = [AdventureWorks2019].[Sales].[SalesOrderHeader].[SalesOrderID] AND [AdventureWorks2019].[Sales].[SalesOrderDetail].[ProductID] = [AdventureWorks2019].[Production].[Product].[ProductID] AND [AdventureWorks2019].[Production].[Product].[ProductSubcategoryID] = [AdventureWorks2019].[Production].[ProductSubcategory].[ProductSubcategoryID] AND [AdventureWorks2019].[Sales].[SalesOrderHeader].[TerritoryID] IN(" + getCountryID(country) + ") ORDER BY [AdventureWorks2019].[Sales].[SalesOrderDetail].[SalesOrderID] ASC;"

    return sql

def getCategoriesBySaison(saison):
    sql = ""

    return sql

def getCategoriesByCountryAndSaison(country,saison):
    sql = ""

    return sql

def getCountryID(country):

    if country == "All":
        countryID = "1,2,3,4,5,6,7,8,9,10"
    elif country == "North America":
        countryID = "1,2,3,4,5,6"
    elif country == "Europe":
        countryID = "7,8,10"
    else:
        countryID = "9"

    return countryID

def getQuartal(saison):

    if saison == "Q1":
        quartal = "[AdventureWorks2019].[Sales].[SalesOrderDetail].[ModifiedDate] BETWEEN '01.01.2011 00:00:00.000' AND '31.03.2011 00:00:00.000' OR [AdventureWorks2019].[Sales].[SalesOrderDetail].[ModifiedDate] BETWEEN '01.01.2012 00:00:00.000' AND '31.03.2012 00:00:00.000' OR [AdventureWorks2019].[Sales].[SalesOrderDetail].[ModifiedDate] BETWEEN '01.01.2013 00:00:00.000' AND '31.03.2013 00:00:00.000' OR [AdventureWorks2019].[Sales].[SalesOrderDetail].[ModifiedDate] BETWEEN '01.01.2014 00:00:00.000' AND '31.03.2014 00:00:00.000'"
    elif saison == "Q2":
        quartal = "[AdventureWorks2019].[Sales].[SalesOrderDetail].[ModifiedDate] BETWEEN '01.04.2011 00:00:00.000' AND '30.06.2011 00:00:00.000' OR [AdventureWorks2019].[Sales].[SalesOrderDetail].[ModifiedDate] BETWEEN '01.04.2012 00:00:00.000' AND '30.06.2012 00:00:00.000' OR [AdventureWorks2019].[Sales].[SalesOrderDetail].[ModifiedDate] BETWEEN '01.04.2013 00:00:00.000' AND '30.06.2013 00:00:00.000' OR [AdventureWorks2019].[Sales].[SalesOrderDetail].[ModifiedDate] BETWEEN '01.04.2014 00:00:00.000' AND '30.06.2014 00:00:00.000'"
    elif saison == "Q3":
        quartal = "[AdventureWorks2019].[Sales].[SalesOrderDetail].[ModifiedDate] BETWEEN '01.07.2011 00:00:00.000' AND '30.09.2011 00:00:00.000' OR [AdventureWorks2019].[Sales].[SalesOrderDetail].[ModifiedDate] BETWEEN '01.07.2012 00:00:00.000' AND '30.09.2012 00:00:00.000' OR [AdventureWorks2019].[Sales].[SalesOrderDetail].[ModifiedDate] BETWEEN '01.07.2013 00:00:00.000' AND '30.09.2013 00:00:00.000' OR [AdventureWorks2019].[Sales].[SalesOrderDetail].[ModifiedDate] BETWEEN '01.07.2014 00:00:00.000' AND '30.09.2014 00:00:00.000'"
    else:
        quartal = "[AdventureWorks2019].[Sales].[SalesOrderDetail].[ModifiedDate] BETWEEN '01.10.2011 00:00:00.000' AND '31.12.2011 00:00:00.000' OR [AdventureWorks2019].[Sales].[SalesOrderDetail].[ModifiedDate] BETWEEN '01.10.2012 00:00:00.000' AND '31.12.2012 00:00:00.000' OR [AdventureWorks2019].[Sales].[SalesOrderDetail].[ModifiedDate] BETWEEN '01.10.2013 00:00:00.000' AND '31.12.2013 00:00:00.000' OR [AdventureWorks2019].[Sales].[SalesOrderDetail].[ModifiedDate] BETWEEN '01.10.2014 00:00:00.000' AND '31.12.2014 00:00:00.000'"

    return quartal

def getProductPhoto(product):
    sql = "SELECT [AdventureWorks2019].[Production].[ProductPhoto].[ThumbNailPhoto] FROM [AdventureWorks2019].[Production].[Product], [AdventureWorks2019].[Production].[ProductPhoto], [AdventureWorks2019].[Production].[ProductProductPhoto] WHERE [AdventureWorks2019].[Production].[Product].[ProductID] = [AdventureWorks2019].[Production].[ProductProductPhoto].ProductID AND [AdventureWorks2019].[Production].[ProductPhoto].[ProductPhotoID] = [AdventureWorks2019].[Production].[ProductProductPhoto].[ProductPhotoID] AND [AdventureWorks2019].[Production].[Product].[Name] = '" + str(product) + "';"

def getProductsAll():
    sql = "SELECT [AdventureWorks2019].[Sales].[SalesOrderDetail].[SalesOrderID], [AdventureWorks2019].[Production].[Product].[Name] FROM [AdventureWorks2019].[Sales].[SalesOrderDetail], [AdventureWorks2019].[Production].[Product] WHERE [AdventureWorks2019].[Sales].[SalesOrderDetail].[ProductID] = [AdventureWorks2019].[Production].[Product].[ProductID] ORDER BY [SalesOrderID] ASC;"

    return sql

def getProductsByCountry(country):
    sql = "SELECT [AdventureWorks2019].[Sales].[SalesOrderDetail].[SalesOrderID], [AdventureWorks2019].[Production].[Product].[Name] FROM [AdventureWorks2019].[Sales].[SalesOrderHeader], [AdventureWorks2019].[Sales].[SalesOrderDetail], [AdventureWorks2019].[Production].[Product] WHERE [AdventureWorks2019].[Sales].[SalesOrderDetail].[SalesOrderID] = [AdventureWorks2019].[Sales].[SalesOrderHeader].[SalesOrderID] AND [AdventureWorks2019].[Sales].[SalesOrderDetail].[ProductID] = [AdventureWorks2019].[Production].[Product].[ProductID] AND [AdventureWorks2019].[Sales].[SalesOrderHeader].[TerritoryID] = " + str(country) + " ORDER BY [SalesOrderID] ASC;"

    return sql

def getCategoriesAll():
    sql = "SELECT DISTINCT [AdventureWorks2019].[Sales].[SalesOrderDetail].[SalesOrderID], [AdventureWorks2019].[Production].[ProductSubcategory].[Name] FROM [AdventureWorks2019].[Sales].[SalesOrderDetail], [AdventureWorks2019].[Production].[Product], [AdventureWorks2019].[Production].[ProductSubcategory] WHERE [AdventureWorks2019].[Sales].[SalesOrderDetail].[ProductID] = [AdventureWorks2019].[Production].[Product].[ProductID] AND [AdventureWorks2019].[Production].[Product].[ProductSubcategoryID] = [AdventureWorks2019].[Production].[ProductSubcategory].[ProductSubcategoryID] ORDER BY [AdventureWorks2019].[Sales].[SalesOrderDetail].[SalesOrderID] ASC;"

    return sql

def getCategoriesByCountry(country):
    sql = "SELECT DISTINCT [AdventureWorks2019].[Sales].[SalesOrderDetail].[SalesOrderID], [AdventureWorks2019].[Production].[ProductSubcategory].[Name] FROM [AdventureWorks2019].[Sales].[SalesOrderHeader], [AdventureWorks2019].[Sales].[SalesOrderDetail], [AdventureWorks2019].[Production].[Product], [AdventureWorks2019].[Production].[ProductSubcategory] WHERE [AdventureWorks2019].[Sales].[SalesOrderDetail].[SalesOrderID] = [AdventureWorks2019].[Sales].[SalesOrderHeader].[SalesOrderID] AND [AdventureWorks2019].[Sales].[SalesOrderDetail].[ProductID] = [AdventureWorks2019].[Production].[Product].[ProductID] AND [AdventureWorks2019].[Production].[Product].[ProductSubcategoryID] = [AdventureWorks2019].[Production].[ProductSubcategory].[ProductSubcategoryID] AND [AdventureWorks2019].[Sales].[SalesOrderHeader].[TerritoryID] = " + str(country) + " ORDER BY [AdventureWorks2019].[Sales].[SalesOrderDetail].[SalesOrderID] ASC;"

    return sql
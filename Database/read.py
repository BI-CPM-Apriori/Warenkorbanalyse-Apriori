def getProductName(productID):
    sql = "SELECT [AdventureWorks2019].[Production].[Product].[Name] FROM [AdventureWorks2019].[Production].[Product] WHERE [AdventureWorks2019].[Production].[Product].[ProductID] = " + str(productID) + ";"

    return sql

def getCategoryName(categoryID):
    sql = "SELECT [AdventureWorks2019].[Production].[ProductCategory].[Name] FROM [AdventureWorks2019].[Production].[ProductCategory] WHERE [AdventureWorks2019].[Production].[ProductCategory].[ProductCategoryID] =  " + str(categoryID) + ";"

    return sql

def getSubcategoryName(subcategoryID):
    sql = "SELECT [AdventureWorks2019].[Production].[ProductSubcategory].[Name] FROM [AdventureWorks2019].[Production].[ProductSubcategory] WHERE [AdventureWorks2019].[Production].[ProductSubcategory].[ProductSubcategoryID] =  " + str(subcategoryID) + ";"

    return sql

def getProductPhoto(productID):
    sql = "SELECT [AdventureWorks2019].[Production].[ProductPhoto].[LargePhoto] FROM [AdventureWorks2019].[Production].[Product], [AdventureWorks2019].[Production].[ProductPhoto], [AdventureWorks2019].[Production].[ProductProductPhoto] WHERE [AdventureWorks2019].[Production].[Product].[ProductID] = [AdventureWorks2019].[Production].[ProductProductPhoto].ProductID AND [AdventureWorks2019].[Production].[ProductPhoto].[ProductPhotoID] = [AdventureWorks2019].[Production].[ProductProductPhoto].[ProductPhotoID] AND [AdventureWorks2019].[Production].[Product].[ProductID] = " + str(productID) + ";"

    return sql

def getCategoryPhoto(categoryID):

    if categoryID == 1:
        path = "images/categories/bikes.png"
    elif categoryID == 2:
        path = "images/categories/components.png"
    elif categoryID == 3:
        path = "images/categories/clothing.png"
    else:
        path = "images/categories/accessories.png"

    return path

def getSubcategoryPhoto(categoryID):

    if categoryID == 1:
        path = "images/subcategories/mountain_bikes.png"
    elif categoryID == 2:
        path = "images/subcategories/road_bikes.png"
    elif categoryID == 3:
        path = "images/subcategories/touring_bikes.png"
    elif categoryID == 4:
        path = "images/subcategories/handlebars.png"
    elif categoryID == 5:
        path = "images/subcategories/bottom_brackets.png"
    elif categoryID == 6:
        path = "images/subcategories/brakes.png"
    elif categoryID == 7:
        path = "images/subcategories/chains.png"
    elif categoryID == 8:
        path = "images/subcategories/cranksets.png"
    elif categoryID == 9:
        path = "images/subcategories/derailleurs.png"
    elif categoryID == 10:
        path = "images/subcategories/forks.png"
    elif categoryID == 11:
        path = "images/subcategories/headsets.png"
    elif categoryID == 12:
        path = "images/subcategories/mountain_frames.png"
    elif categoryID == 13:
        path = "images/subcategories/pedals.png"
    elif categoryID == 14:
        path = "images/subcategories/road_frames.png"
    elif categoryID == 15:
        path = "images/subcategories/saddles.png"
    elif categoryID == 16:
        path = "images/subcategories/touring_frames.png"
    elif categoryID == 17:
        path = "images/subcategories/wheels.png"
    elif categoryID == 18:
        path = "images/subcategories/bib_shorts.png"
    elif categoryID == 19:
        path = "images/subcategories/caps.png"
    elif categoryID == 20:
        path = "images/subcategories/gloves.png"
    elif categoryID == 21:
        path = "images/subcategories/jerseys.png"
    elif categoryID == 22:
        path = "images/subcategories/shorts.png"
    elif categoryID == 23:
        path = "images/subcategories/socks.png"
    elif categoryID == 24:
        path = "images/subcategories/tights.png"
    elif categoryID == 25:
        path = "images/subcategories/vests.png"
    elif categoryID == 26:
        path = "images/subcategories/bike_racks.png"
    elif categoryID == 27:
        path = "images/subcategories/bike_stands.png"
    elif categoryID == 28:
        path = "images/subcategories/bottles_cages.png"
    elif categoryID == 29:
        path = "images/subcategories/cleaners.png"
    elif categoryID == 30:
        path = "images/subcategories/fenders.png"
    elif categoryID == 31:
        path = "images/subcategories/helmets.png"
    elif categoryID == 32:
        path = "images/subcategories/hydration_packs.png"
    elif categoryID == 33:
        path = "images/subcategories/lights.png"
    elif categoryID == 34:
        path = "images/subcategories/locks.png"
    elif categoryID == 35:
        path = "images/subcategories/panniers.png"
    elif categoryID == 36:
        path = "images/subcategories/pumps.png"
    elif categoryID == 37:
        path = "images/subcategories/tires_tubes.png"
    else:
        path = ""

    return path

def getProductsAll():
    sql = "SELECT [AdventureWorks2019].[Sales].[SalesOrderDetail].[SalesOrderID], [AdventureWorks2019].[Sales].[SalesOrderDetail].[ProductID] FROM [AdventureWorks2019].[Sales].[SalesOrderDetail] ORDER BY [SalesOrderID] ASC;"

    return sql

def getProductsByCountry(country):
    sql = "SELECT [AdventureWorks2019].[Sales].[SalesOrderDetail].[SalesOrderID], [AdventureWorks2019].[Sales].[SalesOrderDetail].[ProductID] FROM [AdventureWorks2019].[Sales].[SalesOrderHeader], [AdventureWorks2019].[Sales].[SalesOrderDetail] WHERE [AdventureWorks2019].[Sales].[SalesOrderDetail].[SalesOrderID] = [AdventureWorks2019].[Sales].[SalesOrderHeader].[SalesOrderID] AND [AdventureWorks2019].[Sales].[SalesOrderHeader].[TerritoryID] IN(" + getCountryID(country) + ") ORDER BY [SalesOrderID] ASC;"

    return sql

def getProductsBySaison(saison):

    sql = "SELECT [AdventureWorks2019].[Sales].[SalesOrderDetail].[SalesOrderID], [AdventureWorks2019].[Sales].[SalesOrderDetail].[ProductID] FROM [AdventureWorks2019].[Sales].[SalesOrderDetail] WHERE " + getQuartal(saison) + " ORDER BY [SalesOrderID] ASC;"

    return sql

def getProductsByCountryAndSaison(country, saison):

    sql = "SELECT [AdventureWorks2019].[Sales].[SalesOrderDetail].[SalesOrderID], [AdventureWorks2019].[Sales].[SalesOrderDetail].[ProductID] FROM [AdventureWorks2019].[Sales].[SalesOrderHeader], [AdventureWorks2019].[Sales].[SalesOrderDetail] WHERE [AdventureWorks2019].[Sales].[SalesOrderDetail].[SalesOrderID] = [AdventureWorks2019].[Sales].[SalesOrderHeader].[SalesOrderID] AND [AdventureWorks2019].[Sales].[SalesOrderHeader].[TerritoryID] IN(" + getCountryID(country) + ") AND ("+ getQuartal(saison) +") ORDER BY [SalesOrderID] ASC;"

    return sql

def getCategoriesAll():
    sql = "SELECT DISTINCT [AdventureWorks2019].[Sales].[SalesOrderDetail].[SalesOrderID], [AdventureWorks2019].[Production].[ProductCategory].[ProductCategoryID]  FROM [AdventureWorks2019].[Sales].[SalesOrderDetail], [AdventureWorks2019].[Production].[Product], [AdventureWorks2019].[Production].[ProductSubcategory], [AdventureWorks2019].[Production].[ProductCategory] WHERE [AdventureWorks2019].[Sales].[SalesOrderDetail].[ProductID] = [AdventureWorks2019].[Production].[Product].[ProductID]  AND [AdventureWorks2019].[Production].[Product].[ProductSubcategoryID] = [AdventureWorks2019].[Production].[ProductSubcategory].[ProductSubcategoryID] AND [AdventureWorks2019].[Production].[ProductCategory].[ProductCategoryID] = [AdventureWorks2019].[Production].[ProductSubcategory].[ProductCategoryID] ORDER BY [AdventureWorks2019].[Sales].[SalesOrderDetail].[SalesOrderID] ASC;"

    return sql

def getCategoriesByCountry(country):
    sql = "SELECT DISTINCT [AdventureWorks2019].[Sales].[SalesOrderDetail].[SalesOrderID], [AdventureWorks2019].[Production].[ProductCategory].[ProductCategoryID] FROM [AdventureWorks2019].[Sales].[SalesOrderHeader], [AdventureWorks2019].[Sales].[SalesOrderDetail], [AdventureWorks2019].[Production].[Product], [AdventureWorks2019].[Production].[ProductSubcategory], [AdventureWorks2019].[Production].[ProductCategory] WHERE [AdventureWorks2019].[Sales].[SalesOrderHeader].[SalesOrderID] = [AdventureWorks2019].[Sales].[SalesOrderDetail].[SalesOrderID] AND [AdventureWorks2019].[Sales].[SalesOrderDetail].[ProductID] = [AdventureWorks2019].[Production].[Product].[ProductID] AND [AdventureWorks2019].[Production].[Product].[ProductSubcategoryID] = [AdventureWorks2019].[Production].[ProductSubcategory].[ProductSubcategoryID] AND [AdventureWorks2019].[Production].[ProductCategory].[ProductCategoryID] = [AdventureWorks2019].[Production].[ProductSubcategory].[ProductCategoryID] AND [AdventureWorks2019].[Sales].[SalesOrderHeader].[TerritoryID] IN(" + getCountryID(country) + ") ORDER BY [AdventureWorks2019].[Sales].[SalesOrderDetail].[SalesOrderID] ASC;"

    return sql

def getCategoriesBySaison(saison):
    sql = "SELECT DISTINCT [AdventureWorks2019].[Sales].[SalesOrderDetail].[SalesOrderID], [AdventureWorks2019].[Production].[ProductCategory].[ProductCategoryID] FROM [AdventureWorks2019].[Sales].[SalesOrderDetail], [AdventureWorks2019].[Production].[Product], [AdventureWorks2019].[Production].[ProductSubcategory], [AdventureWorks2019].[Production].[ProductCategory] WHERE [AdventureWorks2019].[Sales].[SalesOrderDetail].[ProductID] = [AdventureWorks2019].[Production].[Product].[ProductID] AND [AdventureWorks2019].[Production].[Product].[ProductSubcategoryID] = [AdventureWorks2019].[Production].[ProductSubcategory].[ProductSubcategoryID] AND [AdventureWorks2019].[Production].[ProductCategory].[ProductCategoryID] = [AdventureWorks2019].[Production].[ProductSubcategory].[ProductCategoryID] AND (" + getQuartal(saison) + ") ORDER BY [AdventureWorks2019].[Sales].[SalesOrderDetail].[SalesOrderID] ASC;"

    return sql

def getCategoriesByCountryAndSaison(country,saison):
    sql = "SELECT DISTINCT [AdventureWorks2019].[Sales].[SalesOrderDetail].[SalesOrderID], [AdventureWorks2019].[Production].[ProductCategory].[ProductCategoryID] FROM [AdventureWorks2019].[Sales].[SalesOrderHeader], [AdventureWorks2019].[Sales].[SalesOrderDetail], [AdventureWorks2019].[Production].[Product], [AdventureWorks2019].[Production].[ProductSubcategory], [AdventureWorks2019].[Production].[ProductCategory] WHERE [AdventureWorks2019].[Sales].[SalesOrderHeader].[SalesOrderID] = [AdventureWorks2019].[Sales].[SalesOrderDetail].[SalesOrderID] AND [AdventureWorks2019].[Sales].[SalesOrderDetail].[ProductID] = [AdventureWorks2019].[Production].[Product].[ProductID] AND [AdventureWorks2019].[Production].[Product].[ProductSubcategoryID] = [AdventureWorks2019].[Production].[ProductSubcategory].[ProductSubcategoryID] AND [AdventureWorks2019].[Production].[ProductCategory].[ProductCategoryID] = [AdventureWorks2019].[Production].[ProductSubcategory].[ProductCategoryID] AND [AdventureWorks2019].[Sales].[SalesOrderHeader].[TerritoryID] IN(" + getCountryID(country) + ") AND (" + getQuartal(saison) + ") ORDER BY [AdventureWorks2019].[Sales].[SalesOrderDetail].[SalesOrderID] ASC;"

    return sql

def getSubcategoriesAll():
    sql = "SELECT DISTINCT [AdventureWorks2019].[Sales].[SalesOrderDetail].[SalesOrderID], [AdventureWorks2019].[Production].[ProductSubCategory].[ProductSubcategoryID] FROM [AdventureWorks2019].[Sales].[SalesOrderDetail], [AdventureWorks2019].[Production].[Product], [AdventureWorks2019].[Production].[ProductSubcategory] WHERE [AdventureWorks2019].[Sales].[SalesOrderDetail].[ProductID] = [AdventureWorks2019].[Production].[Product].[ProductID] AND [AdventureWorks2019].[Production].[Product].[ProductSubcategoryID] = [AdventureWorks2019].[Production].[ProductSubcategory].[ProductSubcategoryID] ORDER BY [AdventureWorks2019].[Sales].[SalesOrderDetail].[SalesOrderID] ASC;"

    return sql

def getSubcategoriesByCountry(country):
    sql = "SELECT DISTINCT [AdventureWorks2019].[Sales].[SalesOrderDetail].[SalesOrderID], [AdventureWorks2019].[Production].[ProductSubcategory].[ProductSubcategoryID] FROM [AdventureWorks2019].[Sales].[SalesOrderHeader], [AdventureWorks2019].[Sales].[SalesOrderDetail], [AdventureWorks2019].[Production].[Product], [AdventureWorks2019].[Production].[ProductSubcategory] WHERE [AdventureWorks2019].[Sales].[SalesOrderHeader].[SalesOrderID] = [AdventureWorks2019].[Sales].[SalesOrderDetail].[SalesOrderID] AND [AdventureWorks2019].[Sales].[SalesOrderDetail].[ProductID] = [AdventureWorks2019].[Production].[Product].[ProductID] AND [AdventureWorks2019].[Production].[Product].[ProductSubcategoryID] = [AdventureWorks2019].[Production].[ProductSubcategory].[ProductSubcategoryID] AND [AdventureWorks2019].[Sales].[SalesOrderHeader].[TerritoryID] IN(" + getCountryID(country) + ") ORDER BY [AdventureWorks2019].[Sales].[SalesOrderDetail].[SalesOrderID] ASC;"

    return sql

def getSubcategoriesBySaison(saison):
    sql = "SELECT DISTINCT [AdventureWorks2019].[Sales].[SalesOrderDetail].[SalesOrderID], [AdventureWorks2019].[Production].[ProductSubcategory].[ProductSubcategoryID] FROM [AdventureWorks2019].[Sales].[SalesOrderDetail], [AdventureWorks2019].[Production].[Product], [AdventureWorks2019].[Production].[ProductSubcategory] WHERE [AdventureWorks2019].[Sales].[SalesOrderDetail].[ProductID] = [AdventureWorks2019].[Production].[Product].[ProductID] AND [AdventureWorks2019].[Production].[Product].[ProductSubcategoryID] = [AdventureWorks2019].[Production].[ProductSubcategory].[ProductSubcategoryID] AND (" + getQuartal(saison) + ") ORDER BY [AdventureWorks2019].[Sales].[SalesOrderDetail].[SalesOrderID] ASC;"

    return sql

def getSubcategoriesByCountryAndSaison(country,saison):
    sql = "SELECT DISTINCT [AdventureWorks2019].[Sales].[SalesOrderDetail].[SalesOrderID], [AdventureWorks2019].[Production].[ProductSubcategory].[ProductSubcategoryID] FROM [AdventureWorks2019].[Sales].[SalesOrderHeader], [AdventureWorks2019].[Sales].[SalesOrderDetail], [AdventureWorks2019].[Production].[Product], [AdventureWorks2019].[Production].[ProductSubcategory]  WHERE [AdventureWorks2019].[Sales].[SalesOrderHeader].[SalesOrderID] = [AdventureWorks2019].[Sales].[SalesOrderDetail].[SalesOrderID] AND [AdventureWorks2019].[Sales].[SalesOrderDetail].[ProductID] = [AdventureWorks2019].[Production].[Product].[ProductID] AND [AdventureWorks2019].[Production].[Product].[ProductSubcategoryID] = [AdventureWorks2019].[Production].[ProductSubcategory].[ProductSubcategoryID] AND [AdventureWorks2019].[Sales].[SalesOrderHeader].[TerritoryID] IN(" + getCountryID(country) + ") AND (" + getQuartal(saison) + ") ORDER BY [AdventureWorks2019].[Sales].[SalesOrderDetail].[SalesOrderID] ASC;"

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
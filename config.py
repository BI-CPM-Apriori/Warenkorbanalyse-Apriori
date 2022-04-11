import pyodbc 
# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port

server = 'NB-DK-DELL\SQLEXPRESS' 
database = 'AdventureWorks2019' 
username = 'NB-DK-DELL\Daniel' 
password = 'dk17' 
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
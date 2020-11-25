import pyodbc as pydb

from sqlalchemy import create_engine, event
from urllib.parse import quote_plus
#=====================================================
# Chaves de conexão com Banco de dados
#------------------------------------------------------ 
server_bd = 'localhost'
username_bd = 'sa'
password_bd = 'sa'
driver = '{ODBC Driver 17 for SQL Server}'

def connection(database):
    connection = string_connection_odbc(database)
    return pydb.connect(connection)

def alchemy_connection(database):
    con = 'mssql+pyodbc:///?odbc_connect={}'.format(string_connection(database))
    return create_engine(con)

def string_connection_odbc(database):
    con = 'DRIVER='+driver+';SERVER='+server_bd+';PORT=1433;DATABASE='+database+';UID='+username_bd+';PWD='+password_bd
    return con

def string_connection(database):
    return quote_plus('DRIVER='+driver+';SERVER='+server_bd+';DATABASE='+database+';UID='+username_bd+';PWD='+password_bd)
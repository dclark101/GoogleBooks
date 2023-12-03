import pytest
import pyodbc
from dotenv import load_dotenv, dotenv_values
from src.authentication.db_connection import SQLConnection
from src.authentication.signup import sql_connection

load_dotenv()

config = dotenv_values(".env")

# faulty sql_connection
bad_sql_connection = SQLConnection(
    server=config["SERVER"],
    database="BikStores",
    username=config["USERNAME"],
    password=config["PASSWORD"],
    driver="ODBC Driver 17 for SQL Server",
)


def test_if_sql_connection_failed():
    with pytest.raises(pyodbc.InterfaceError):
        conn = pyodbc.connect(bad_sql_connection.connection_string)


def test_if_sql_connection_succeeds():
    assert type(pyodbc.connect(sql_connection.connection_string)) == pyodbc.Connection

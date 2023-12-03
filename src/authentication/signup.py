from db_connection import *
import pyodbc
from dotenv import load_dotenv, dotenv_values
import helper.helper_functions as helper

load_dotenv()

config = dotenv_values(".env")

sql_connection = SQLConnection(
    server=config["SERVER"],
    database="GoogleBooks",
    username=config["USERNAME"],
    password=config["PASSWORD"],
    driver="ODBC Driver 17 for SQL Server",
)


conn = pyodbc.connect(sql_connection.connection_string)

cursor = conn.cursor()

user_input = "HelloWorld$"

if helper.password_format(user_input):
    sql_insert = (
        """
    INSERT INTO UserAuthentication(user_email, user_password)
    VALUES ('sirpawser@gmail.com',
    """
        + "'"
        + user_input
        + "'"
        + ");"
    )
    cursor.execute(sql_insert)
    conn.commit()
else:
    print("password is invalid!")

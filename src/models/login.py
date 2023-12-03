from authentication.db_connection import SQLConnection
import pyodbc
from dotenv import load_dotenv, dotenv_values

load_dotenv()

config = dotenv_values(".env")


class Login(SQLConnection):
    def __init__(self, user_email, user_password):
        self.user_email = user_email
        self.user_password = user_password

        super().__init__(
            config["SERVER"],
            "GoogleBooks",
            config["USERNAME"],
            config["PASSWORD"],
            "ODBC Driver 17 for SQL Server",
        )

        self.conn = pyodbc.connect(self.connection_string)
        self.cursor = self.conn.cursor()

    def does_exist(self) -> bool:
        rows = self.get_credentials()

        for row in range(len(rows)):
            if (self.user_email == rows[row][0]) and (
                self.user_password == rows[row][1]
            ):
                return True

        return False

    def get_credentials(self):
        select = "SELECT user_email, user_password FROM UserAuthentication"

        rows = self.cursor.execute(select).fetchall()
        return rows


login = Login("danteclark66@gmail.com", "HelloWorld12$")

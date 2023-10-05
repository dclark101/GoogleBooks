import pyodbc

class SQLConnection():
    
    def __init__(self, server, database, username, password, driver):
        self.server = server 
        self.database = database
        self.username = username
        self.password = password 
        
        
    
    def connection_string(self) -> str:
        """function that returns database credentials"""
        return f'DRIVER={self.driver};SERVER={self.server};DATABASE={self.database};UID={self.username};PWD={self.password}'
    
    def conn(self) -> pyodbc.Connection:
        """returns pyodbc Connection object from connection_string function"""
        return pyodbc.connect(self.connection_string())
import pyodbc


def create_connection():
    server = 'localhost'
    database = 'your_database'
    username = 'your_username'
    password = 'your_password'

    connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

    try:
        conn = pyodbc.connect(connection_string)
        return conn
    except pyodbc.Error as e:
        print(f"Error connecting to SQL Server: {e}")

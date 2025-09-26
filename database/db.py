import mysql.connector

def get_db_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",          # Your MySQL username
        password="root",  # Your MySQL password
        database="user_database"
    )
    return conn

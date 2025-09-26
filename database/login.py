from db import get_db_connection

def login_user(username, password):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
    user = cursor.fetchone()
    conn.close()

    if user:
        return "Login successful!"
    else:
        return "Invalid username or password."

from db import get_db_connection

def register_user(username, password):
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
        conn.commit()
        return "Registration successful!"
    except mysql.connector.IntegrityError:
        return "Username already exists."
    finally:
        conn.close()

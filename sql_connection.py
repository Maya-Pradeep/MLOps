import sqlite3

def get_connection():
    try:

        connection = sqlite3.connect("college.db")
        cursor = connection.cursor()

        # Employee Table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS employee(
            employee_id INTEGER PRIMARY KEY,
            employee_name TEXT NOT NULL,
            department TEXT NOT NULL,
            salary REAL,
            mentor_capacity INTEGER
        )
        """)

        # Student Table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS student(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            department TEXT NOT NULL,
            cgpa REAL,
            fees REAL
        )
        """)

        connection.commit()

        return connection

    except Exception as e:

        print("Database Connection Error")
        print(e)

        return None
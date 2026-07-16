from sql_connection import get_connection


def execute(query, values=None):

    connection = get_connection()

    if connection is None:
        return None

    cursor = connection.cursor()

    try:

        if values is not None:
            cursor.execute(query, values)
        else:
            cursor.execute(query)

        if query.strip().upper().startswith("SELECT"):
            result = cursor.fetchall()

        else:
            connection.commit()
            result = cursor.rowcount

        return result

    except Exception as e:

        print("SQL CONNECTION FAILED:", e)
        return None

    finally:

        cursor.close()
        connection.close()
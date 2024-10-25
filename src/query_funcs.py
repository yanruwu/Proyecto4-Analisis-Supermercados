import psycopg2
from psycopg2 import errorcodes, OperationalError

def conectar():
    try:
        connection = psycopg2.connect(
            database = "Analisis-Supermercados",
            user = "postgres",
            password = "admin",
            host = "localhost",
            port = "5432"
        )
    except OperationalError as e:
        if e.pgcode == errorcodes.INVALID_PASSWORD:
            print("La constraseña es errónea.")
        elif e.pgcode == errorcodes.CONNECTION_EXCEPTION:
            print("Error de conexión")
        else:
            print(f'Error:{e}')
    return connection

def query_fetch(connection, query_text):
    cursor = connection.cursor()
    cursor.execute(query_text)
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result

def query_commit(connection, query_text, *valores):
    cursor = connection.cursor()
    cursor.execute(query_text, *valores)
    connection.commit()
    cursor.close()
    connection.close()
    return print("Done!")

def query_commit_many(connection, query_text, *valores):
    cursor = connection.cursor()
    cursor.executemany(query_text, *valores)
    connection.commit()
    cursor.close()
    connection.close()
    return print("Done!")
import psycopg2
from psycopg2 import errorcodes, OperationalError

import os
import sys
import dotenv
sys.path.append("..")
dotenv.load_dotenv()

pw1 = os.getenv("pw1")


def conectar(pw: str = pw1) -> psycopg2.extensions.connection:
    """
    Establece una conexión a la base de datos PostgreSQL.

    Args:
        pw (str): La contraseña para acceder a la base de datos. Por defecto, se obtiene de las variables de entorno.

    Returns:
        connection: Un objeto de conexión a la base de datos PostgreSQL.

    Raises:
        OperationalError: Si hay un error de conexión o la contraseña es inválida.
    """
    try:
        connection = psycopg2.connect(
            database = "Analisis-Supermercados",
            user = "postgres",
            password = pw,
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

def query_fetch(connection: psycopg2.extensions.connection, query_text: str) -> list:
    """
    Ejecuta una consulta SQL de tipo SELECT y devuelve todos los resultados.

    Args:
        connection: Un objeto de conexión a la base de datos PostgreSQL.
        query_text (str): La consulta SQL a ejecutar.

    Returns:
        list: Una lista de tuplas que representan las filas devueltas por la consulta.

    Raises:
        Exception: Si ocurre un error al ejecutar la consulta.
    """
    cursor = connection.cursor()
    cursor.execute(query_text)
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result

def query_commit(connection: psycopg2.extensions.connection, query_text: str, *valores) -> None:
    """
    Ejecuta una consulta SQL que modifica la base de datos (INSERT, UPDATE, DELETE).

    Args:
        connection: Un objeto de conexión a la base de datos PostgreSQL.
        query_text (str): La consulta SQL a ejecutar.
        *valores: Valores a insertar en la consulta.

    Returns:
        None: Imprime "Done!" al finalizar la operación.

    Raises:
        Exception: Si ocurre un error al ejecutar la consulta.
    """
    cursor = connection.cursor()
    cursor.execute(query_text, *valores)
    connection.commit()
    cursor.close()
    connection.close()
    return print("Done!")

def query_commit_many(connection, query_text, *valores):
    """
    Ejecuta una consulta SQL que modifica la base de datos utilizando múltiples valores (INSERT).

    Args:
        connection: Un objeto de conexión a la base de datos PostgreSQL.
        query_text (str): La consulta SQL a ejecutar.
        *valores: Una secuencia de tuplas que contienen los valores a insertar.

    Returns:
        None: Imprime "Done!" al finalizar la operación.

    Raises:
        Exception: Si ocurre un error al ejecutar la consulta.
    """
    cursor = connection.cursor()
    cursor.executemany(query_text, *valores)
    connection.commit()
    cursor.close()
    connection.close()
    return print("Done!")
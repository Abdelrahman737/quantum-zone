import mysql.connector
from mysql.connector import pooling
from config import DB_HOST, DB_PORT, DB_USER, DB_PASSWORD, DB_NAME

connection_pool = pooling.MySQLConnectionPool(
    pool_name = 'quantum_zone_pool',
    pool_size = 5,
    host = DB_HOST,
    port = DB_PORT,
    user = DB_USER,
    password = DB_PASSWORD,
    database = DB_NAME
)

def get_db():
    """Get a database connection from the pool."""

    connection = connection_pool.get_connection()

    try:
        yield connection # Gives the connection to whoever called this function
    finally:
        connection.close() # When done, it returns the connection the pool
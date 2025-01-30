import json
import pymysql
import os
import pandas as pd

def lambda_handler(event, context):

    db_host = os.getenv("DB_HOST")
    db_user = os.getenv("DB_USER")
    db_pwd = os.getenv("DB_PASSWORD")
    db_name = os.getenv("DB_NAME")
    try:
    # Conexion MySQL
        connection = pymysql.connect(
            host=db_host,
            user=db_user,
            password=db_pwd,
            database=db_name,
            cursorclass=pymysql.cursors.DictCursor
        )
        print("Conexion db exitosa")

        # Cursor para ejecutar consultas
        with connection.cursor() as cursor:
            sql_query = "SELECT * FROM clientes;"
            cursor.execute(sql_query)
            result = cursor.fetchall()
            df = pd.DataFrame(result)
            print(df.head(3))
        
        return {
            "statusCode": 200,
            "body": f"Conexión exitosa. Resultado: {result}"
        }

    except Exception as e:
        print("Error en la conexión:", e)
        return {
            "statusCode": 500,
            "body": f"Error en la conexión: {str(e)}"
        }

    finally:
        if 'connection' in locals() and connection.open:
            connection.close()
            print("Conexión cerrada")

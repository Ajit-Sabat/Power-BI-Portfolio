import mysql.connector
from mysql.connector import Error
import traceback


def load_csv_to_mysql(table_name, file_path):
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='ecom_data',
            allow_local_infile=True
        )

        if connection.is_connected():
            cursor = connection.cursor()

            load_sql = f"""
            LOAD DATA LOCAL INFILE '{file_path}'
            INTO TABLE {table_name}
            FIELDS TERMINATED BY ',' 
            ENCLOSED BY '"'
            LINES TERMINATED BY '\\r\\n'
            IGNORE 1 LINES;
            """

            cursor.execute(load_sql)
            connection.commit()
            print(f"✅ Data loaded successfully into {table_name}")

    except Error as e:
        print("MySQL error:", e)
        traceback.print_exc()

    except Exception as e:
        print("Unexpected error:", e)
        traceback.print_exc()

    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed")


# Example usage:
load_csv_to_mysql("dim_customers", r"C:\ProgramData\MySQL\MySQL Server 8.0\Uploads\dim_customers.csv")
load_csv_to_mysql("dim_sellers", r"C:\ProgramData\MySQL\MySQL Server 8.0\Uploads\dim_sellers.csv")
load_csv_to_mysql("dim_products", r"C:\ProgramData\MySQL\MySQL Server 8.0\Uploads\dim_products.csv")
load_csv_to_mysql("fact_orders", r"C:\ProgramData\MySQL\MySQL Server 8.0\Uploads\fact_orders.csv")

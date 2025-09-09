import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(
        host="mydbserver.mysql.database.azure.com",  # Azure MySQL server
        user="myadmin@mydbserver",                   # username@servername
        password="MyStrongPassword!",                # your password
        database="mydb",                             # database name
        port=3306
    )

    if connection.is_connected():
        print("Connected to Azure MySQL database")
        cursor = connection.cursor()
        cursor.execute("SELECT DATABASE();")
        record = cursor.fetchone()
        print("You're connected to:", record)

except Error as e:
    print("Error while connecting to MySQL", e)

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection closed")

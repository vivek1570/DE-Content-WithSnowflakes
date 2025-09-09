import mysql.connector
from mysql.connector import Error

connection=None
try:
    connection = mysql.connector.connect(
        host="vikashverma8888.mysql.database.azure.com",  # Azure MySQL server
        user="testuser",                   # username@servername
        password="Mindz@007",                # your password
        database="sampledb",                             # database name
        port=3306
    )

    if connection.is_connected():
        print("Connected to Azure MySQL database")
        cursor = connection.cursor()
        cursor.execute("SELECT DATABASE();")
        record = cursor.fetchone()
        print("You're connected to:", record)
        cursor.execute("CREATE TABLE IF NOT EXISTS Employees (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50))")
        cursor.execute("INSERT INTO Employees (name) VALUES ('Vikash')")
        connection.commit()
        cursor.execute("SELECT * FROM Employees")
        rows = cursor.fetchall()
        for row in rows:
            print(row)

except Error as e:
    print("Error while connecting to MySQL", e)

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection closed")

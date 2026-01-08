# Delete a Table....................................
'''
You can delete an existing table by using the "DROP TABLE" statement:
'''

import mysql.connector
from mysql.connector import Error

try:
    mydb = mysql.connector.connect(
        host="Enter your host name & IP address",
        user="Enter your user name here",
        password="Enter your password here",
        database="EmployeeDB"
    )

    cursor = mydb.cursor()

    # Drop the table (safely)
    table_name = "employees"
    
    cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
    
    print(f"Table '{table_name}' dropped successfully (or didn't exist).")

except Error as e:
    print(f"Error: {e}")

finally:
    if mydb.is_connected():
        cursor.close()
        mydb.close()
        print("Connection closed.")
'''
The WHERE clause filters rows from a table based on conditions. 
It's essential for selecting, updating, or deleting specific data.
'''

import mysql.connector
from mysql.connector import Error             # importing Error class for handling exceptions

try:
    mydb = mysql.connector.connect(
        host="Enter your host name & IP address",
        user="Enter your user name here",
        password="Enter your password here",
        database="EmployeeDB"
    )

    cursor = mydb.cursor()

    # Find employee with specific name
    cursor.execute("SELECT * FROM employees WHERE name = 'Peter'")

    results = cursor.fetchall()
    print("Employees named Peter:")
    for row in results:
        print(row)

except Error as e:
    print("Error while connecting to MySQL", e)

finally:
    if mydb.is_connected():
        cursor.close()
        mydb.close()
        print("Connection closed.")


'''
Safe Way: Use Parameterized Queries (Prevents SQL Injection)
Always use this method when conditions come from user input!
'''

mydb = mysql.connector.connect(
    host="Enter your host name & IP address",
    user="Enter your user name here",
    password="Enter your password here",
    database="EmployeeDB"
)

cursor = mydb.cursor()

sql = "SELECT * FROM customers WHERE address = %s"
adr = ("Yellow Garden 2", )

cursor.execute(sql, adr)

myresult = cursor.fetchall()

for x in myresult:
  print(x)
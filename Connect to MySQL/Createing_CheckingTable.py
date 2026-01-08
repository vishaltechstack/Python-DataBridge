# Create Table...................................
'''
To create a table in MySQL, use the "CREATE TABLE" statement.
'''
import mysql.connector
conn = mysql.connector.connect(
    host="Enter your host name & IP address",
    user="Enter your user name here",
    password="Enter your password here",
    database="EmployeeDB"
)

cursor = conn.cursor()
cursor.execute("CREATE TABLE employees (name VARCHAR(255), address VARCHAR(255))")  # Creating Table
print("Table created successfully")


# Checking if Table Exists........................
'''
You can check if a table exist by listing all tables 
in your database with the "SHOW TABLES" statement:
'''
cursor.execute("SHOW TABLES")       # Checking Table exists
for i in cursor:
    print(i)
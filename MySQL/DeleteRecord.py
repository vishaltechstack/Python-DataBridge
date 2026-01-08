'''
You can delete records from an existing table by using the "DELETE FROM" statement:
'''

import mysql.connector

mydb = mysql.connector.connect(
    host="Enter your host name & IP address",
    user="Enter your user name here",
    password="Enter your password here",
    database="EmployeeDB"
)

mycursor = mydb.cursor()

sql = "DELETE FROM employees WHERE address = 'Mountain 21'"         # SQL query to delete a record with specific condition
mycursor.execute(sql)
mydb.commit()

print(mycursor.rowcount, "record(s) deleted")                       # Print number of rows deleted



# Prevent SQL Injection...............................
'''
It is considered a good practice to escape the values of any query, also in delete statements.
This is to prevent SQL injections, which is a common web hacking technique to destroy or misuse your database.
The mysql.connector module uses the placeholder %s to escape values in the delete statement:
'''
mydb = mysql.connector.connect(
    host="Enter your host name & IP address",
    user="Enter your user name here",
    password="Enter your password here",
    database="EmployeeDB"
)
mycursor = mydb.cursor()

sql = "DELETE FROM employees WHERE address = %s"                    # SQL query with placeholder
adr = ("Yellow Garden 2", )

mycursor.execute(sql, adr)
mydb.commit()
print(mycursor.rowcount, "record(s) deleted")
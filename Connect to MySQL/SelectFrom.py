# To select from a table in MySQL, use the "SELECT" statement:

import mysql.connector

mydb = mysql.connector.connect(
  host="Enter your host name & IP address",
  user="Enter your user name here",
  password="Enter your password here",
  database="EmployeeDB"
)

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM employees")         # Selecting All Columns
myresult = mycursor.fetchall()                      # Fetching All Results

for x in myresult:                                  # Iterating Through Results
  print(x)


# Selecting Columns :-
'''
To select only some of the columns in a table, use the "SELECT" statement followed by the column name(s):
'''
mycursor.execute("SELECT name, address FROM employees")
myresult = mycursor.fetchall()

for x in myresult:
  print(x)



# Using the fetchone() Method :-
'''
If you are only interested in one row, you can use the fetchone() method.
The fetchone() method will return the first row of the result:
'''

mycursor.execute("SELECT * FROM employees")
myresult = mycursor.fetchone()

print(myresult)
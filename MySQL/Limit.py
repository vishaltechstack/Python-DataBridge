'''
The LIMIT clause restricts the number of rows returned by a SELECT query.
It's perfect for pagination, getting top results, or just limiting output.
'''

import mysql.connector

mydb = mysql.connector.connect(
  host="Enter your host name & IP address",
  user="Enter your user name here",
  password="Enter your password here",
  database="EmployeeDB"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM employees LIMIT 5")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)



# Start From Another Position
'''
If you want to return five records, starting from the third record, you can use the "OFFSET" keyword:
'''

mydb = mysql.connector.connect(
  host="Enter your host name & IP address",
  user="Enter your user name here",
  password="Enter your password here",
  database="EmployeeDB"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM employees LIMIT 5 OFFSET 2")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
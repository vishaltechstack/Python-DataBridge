# Insert Single Record into MySQL Database...............................

import mysql.connector

mydb = mysql.connector.connect(
  host="Enter your host name & IP address",
  user="Enter your user name here",
  password="Enter your password here",
  database="EmployeeDB"
)

mycursor = mydb.cursor()

sql = "INSERT INTO employees (name, address) VALUES (%s, %s)"      # SQL query to insert a record
val = ("John", "Highway 21")                                       # Values to be inserted
mycursor.execute(sql, val)                                         # Execute the SQL command

mydb.commit()                                                      # Commit the transaction
print(mycursor.rowcount, "record inserted.")


# Insert Multiple Records into MySQL Database............................

'''
To insert multiple rows into a table, use the executemany() method.
The second parameter of the executemany() method is a list of tuples, containing the data you want to insert:
'''

sql = "INSERT INTO employees (name, address) VALUES (%s, %s)"
val = [                                                                # List of tuples with multiple records                          
  ('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')
]

mycursor.executemany(sql, val)                                           # Execute the SQL command for multiple records      

mydb.commit()

print(mycursor.rowcount, "was inserted.")                                # Print number of rows inserted


# Get Inserted ID........................................................
'''
You can get the id of the row you just inserted by asking the cursor object.
'''

sql = "INSERT INTO employees (name, address) VALUES (%s, %s)"
val = ("Michelle", "Blue Village")
mycursor.execute(sql, val)

mydb.commit()

print("1 record inserted, ID:", mycursor.lastrowid)                      # Print the last inserted ID
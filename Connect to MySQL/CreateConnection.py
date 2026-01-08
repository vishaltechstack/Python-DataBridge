# Establishing connection to MySQL database using mysql-connector-python

import mysql.connector   # importing mysql connector module

mydb = mysql.connector.connect(             # creating connection object 
  host="Enter your host name & IP address",                # host name or IP address of MySQL server
  user="Enter your user name here",                     # username of MySQL server
  password="Enter your password here"             # password of MySQL server
)

print(mydb)                        # printing connection object to verify connection
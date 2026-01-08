# Creating a Database

import mysql.connector   # importing mysql connector module

mydb = mysql.connector.connect(             # creating connection object 
    host="Enter your host name & IP address",
    user="Enter your user name here",
    password="Enter your password here",
    database="EmployeeDB"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE EmployeeDB")    # Creating Database



# Checking Existing Database
mycursor.execute("SHOW DATABASES")                # Fetching all databases

for x in mycursor:                                # Iterating through the databases
    print(x)
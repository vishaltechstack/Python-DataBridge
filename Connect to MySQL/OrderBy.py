# 1. Basic ORDER BY Clause............................................
'''
The ORDER BY clause sorts the results of a SELECT query.
You can sort by one or more columns in ascending (ASC) or descending (DESC) order.
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

    # Sort by name (descending)
    cursor.execute("SELECT name, address FROM employees ORDER BY name DESC")

    print("Employees sorted by name (descending):")
    for row in cursor.fetchall():
        print(f"Name: {row[0]} - {row[1]}")
    # Sort by address (ascending)
    cursor.execute("SELECT name, address FROM employees ORDER BY address ASC")

    print("\nEmployees sorted by address (ascending):")
    for row in cursor.fetchall():
        print(f"{row[0]} - Address: {row[1]}")
except Error as e:
    print(f"Error: {e}")

finally:
    if mydb.is_connected():
        cursor.close()
        mydb.close()
        print("Connection closed.")


# 2. Safe Parameterized Queries with ORDER BY...........................
'''
Safe Parameterized Queries with ORDER BY
Note: You cannot directly parameterize column names or ASC/DESC with %s. But you can safely build the query string if input is trusted, or use a whitelist.
'''
mydb = mysql.connector.connect(
    host="Enter your host name & IP address",
    user="Enter your user name here",
    password="Enter your password here",
    database="EmployeeDB")

cursor = mydb.cursor()
# User chooses sort column and direction (from frontend or input)
sort_column = "address"      # Could be "name", "address", etc.
sort_direction = "DESC"     # "ASC" or "DESC"

# Whitelist allowed columns to prevent SQL injection
allowed_columns = ["name", "address"]

if sort_column not in allowed_columns:
    sort_column = "id"  # default fallback

# Validate direction
sort_direction = sort_direction.upper()
if sort_direction not in ["ASC", "DESC"]:
    sort_direction = "ASC"

query = f"SELECT name, address FROM employees ORDER BY {sort_column} {sort_direction}"

cursor.execute(query)

print(f"\nSorted by {sort_column} {sort_direction}:")
for row in cursor.fetchall():
    print(row)




# 3. Multiple Column Sorting...........................................
mydb = mysql.connector.connect(
    host="Enter your host name & IP address",
    user="Enter your user name here",
    password="Enter your password here",
    database="EmployeeDB"
)

cursor = mydb.cursor()
cursor.execute(
"SELECT name, address FROM employees ORDER BY name DESC, address DESC"
)
for row in cursor.fetchall():
    print(f"Name: {row[0]} - Address: {row[1]}")
'''
The UPDATE statement modifies existing rows in a table. It's very powerful — but always use a WHERE clause to avoid updating every row accidentally!
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

    # Give a 10% raise to Alice
    cursor.execute("""
        UPDATE employees 
        SET address = "Canyon 123"
        WHERE address = 'Valley 345'
    """)

    # Update email for a specific ID
    cursor.execute("""
        UPDATE employees 
        SET name = 'Amy Smith' 
        WHERE name = 'Amy'
    """)

    # Commit the changes!
    mydb.commit()

    print(f"{cursor.rowcount} row(s) updated successfully.")

except Error as e:
    print(f"Error: {e}")
    mydb.rollback()  # Undo changes on error

finally:
    if mydb.is_connected():
        cursor.close()
        mydb.close()
        print("Connection closed.")
# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 23:15:50 2016

@author: scornell
"""

#!/usr/bin/python
# version.py – Fetch and display the MySQL database server version.
# import the MySQLdb and sys modules
import MySQLdb
import sys
# open a database connection
# be sure to change the host IP address, username, password and database name to match your own
connection = MySQLdb.connect(host = “marketdataseed.c7snk6pfzyjm.us-east-1.rds.amazonaws.com”, user = “scornell”, passwd = “corn92.acc”, db = “mktdataseed”)
# prepare a cursor object using cursor() method
cursor = connection.cursor()
# execute the SQL query using execute() method.
cursor.execute(“SELECT VERSION()”)
# fetch a single row using fetchone() method.
row = cursor.fetchone()
# print the row[0]
# (Python starts the first row in an array with the number zero – instead of one)
print “Server version:”, row[0]
# close the cursor object
cursor.close ()
# close the connection
connection.close ()
# exit the program
sys.exit() 

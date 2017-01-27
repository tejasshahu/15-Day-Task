import psycopg2
import sys

try:
	conn = psycopg2.connect(database="testdb", user="postgres", password="pass123", host="127.0.0.1", port="5432")

	print "Opened database successfully"
except :
	print "I am unable to connect to the database"
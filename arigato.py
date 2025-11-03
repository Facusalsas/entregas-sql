import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="1234"
)

print(mydb)
mycursor = mydb.cursor()
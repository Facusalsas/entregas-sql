import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="1234",
  database="konichiwa"
)

print(mydb)
mycursor = mydb.cursor()
#mycursor.execute("create DATABASE konichiwa")
mycursor.execute("CREATE TABLE Videojuegos)"),
sql = "INSERT INTO Videojuegos (nombre, precio, creador, genero) VALUES (%s, %s, %s, %s)"
val = [( "Minecraft", 13647, "Mojang", "Aventura")
       ("Five nights at freddy's 2", 300, "Scott Cawton", "Terror")
       ("Ultrakill", 11000, "Hakita", "Fps")
       ("Left 4 dead 2", 8700, "VAlve", "Shooter")
       ("Angry birds space", 14000, "Rovio", "Puzzle")
       ("The battle cats", 0, "PONOS", "Tower defense")
       ("Plants vs zombies 2", 0, "Electronic Arts", "Tower defense")]
mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted")

sql = "UPDATE Videojuegos SET precio = 0 WHERE nombre = 'Ultrakill' "

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")

sql = "DELETE FROM Videojuegos WHERE nombre = 'Plants vs zombies 2' "

mycursor.execute(sql)

mydb.commit()

print("record(s) deleted")

mycursor.execute("SELECT nombre, precio FROM Videojuegos")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)
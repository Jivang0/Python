import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password ="12345jg",
    database = "mydatabase"
)

cor = conn.cursor()

cor.execute("SELECT * FROM customer")
 
result = cor.fetchall() # fetechone()


for x in result:
    print(x)

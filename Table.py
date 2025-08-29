import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "12345jg",
    database = "mydatabase" #mydatabase
)

cor = conn.cursor()
# simple create a Table in the mydatbase 
# cor.execute("CREATE TABLE customer (name VARCHAR(10),address VARCHAR(20),age INT)")


# check the table is exit 

cor.execute("SHOW TABLES")

for x in cor:
    print(x)

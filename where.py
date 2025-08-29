import mysql.connector
conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "12345jg",
    database ="mydatabase"
)
cor = conn.cursor()
sql = ("SELECT * FROM customer WHERE address = 'Butwal 05'")

cor.execute(sql)

myresult = cor.fetchall()

for a in myresult:
    print(a)


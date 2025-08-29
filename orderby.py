import mysql.connector
conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "12345jg",
    database ="mydatabase"
)
cor = conn.cursor()
sql = ("SELECT * FROM customer ORDER BY name")  #ORDER BY name DESC
                             

cor.execute(sql)

myresult = cor.fetchall()

for a in myresult:
    print(a)
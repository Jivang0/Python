import mysql.connector
conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "12345jg",
    database ="mydatabase"
)
cor = conn.cursor()
abc = "DELETE  FROM customer WHERE address = 'Butwal 01'"

cor.execute(abc)

conn.commit()

print(cor.rowcount," record deleted ")
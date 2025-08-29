import mysql.connector
conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "12345jg"

)

# cor = conn.cursor()
# cor.execute("CREATE DATABASE mydatabase")


# if conn.is_connected():
#     print("connection is established")

cor = conn.cursor()
cor.execute("SHOW DATABASES")

for a in cor:
    print(a)




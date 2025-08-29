import mysql.connector
conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "12345jg",
    database ="mydatabase"
)

cor = conn.cursor()
# table is customer
sql = "INSERT INTO customer (name,address) VALUES (%s, %s)" 
val = [
    ("Shiva","Butwal 12"),
    ("Shisan","Butwal 05"),
    ("Ram","Butwal 06"),
    ("God","Butwal 07"),
    ("Sita","Butwal 08"),
    ("Parbati","Butwal 09"),
    ("sus","Butwal 01"),
    ("ABC","Butwal 02"),
    ("XYZZ","Butwal 03"),
    ("Don","Butwal 11")
    
    ]
cor.executemany(sql, val) #simple multiple item lahi executemany garni other executemany
conn.commit()
print(cor.rowcount,"record inserted ")


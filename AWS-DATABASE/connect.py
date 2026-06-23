import mysql.connector

conn = mysql.connector.connect(
    host="YOUR_RDS_ENDPOINT",
    user="admin",
    password="YOUR_PASSWORD",
    database="decodelabs"
)

cursor = conn.cursor()

cursor.execute("SELECT * FROM Interns")

for row in cursor:
    print(row)

conn.close()
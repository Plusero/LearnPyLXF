import mysql.connector as mysql
db = mysql.connect(
    host="localhost",
    user="root",
    passwd="Garin@sql666"
)
print(db)

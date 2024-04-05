import mysql.connector as my

db = my.connect(host = 'localhost', user = 'root', password = "Sow15", database = 'wellness')

query = "select * from user_details;"
key = db.cursor()
m = key.execute(query)
print(m)
key.fetchall()






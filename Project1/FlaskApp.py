import sqlite3


connection = sqlite3.connect('database.db')

cursor = connection.cursor()

# Insert the Navid user for test
sql = "Insert into users (username) values ('Navid')"
cursor.execute(sql)

# Insert the project1 items for test
sql = "Insert into items (name) values ('Project1')"
cursor.execute(sql)

connection.commit()

sql = 'select *from  users'
cursor.execute(sql)

rows = cursor.fetchall()

for row in rows:
	print(row)

connection.close()






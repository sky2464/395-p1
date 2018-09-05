import sqlite3
from flask import Flask, redirect, url_for, request, flash, g, render_template, session
from functools import wraps

connection = sqlite3.connect('database.db')

cursor = connection.cursor()


connection.close()
# Create Flask object
app = Flask(__name__)

# index


@app.route('/')
def home():
	return render_template('index.html')

# Main page


@app.route('/todo', methods=['GET', 'POST'])
def items():
	g.db= connection()
	if request.methods == 'POST':
		newItem = request.form ['New_Item']
		cursor = g.db.execute("SELECT rowid From items WHERE name = ? ", (newItem,))
		theFetch =cursor.fetchone()



'''
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
'''
import sqlite3
from flask import Flask, redirect, url_for, request, flash, g, render_template, session
from functools import wraps

# Create Flask object
app = Flask(__name__)

with sqlite3.connect("database.db") as connection:
	c = connection.cursor()
	c.execute("CREATE TABLE IF NOT EXISTS Users (users_name text)")
	c.execute("CREATE TABLE IF NOT EXISTS items (items_names text)")


# connection = sqlite3.connect('database.db')

# cur = connection.cursor()
# cur.execute("Create TABLE Users (users_name text) ")
# cur.execute("Create TABLE items (items_names text)")
# cur.execute("DROP TABLE items")
# cur.execute("CREATE TABLE items(id INT, name Text)")


# index


@app.route('/', methods=['GET', 'POST'])
def home():

	if request.method == 'POST':
    flash('Hereeeeeeeeee i goooooooooooooo')
		session['logged_in'] = True
		flash('You were just logged in.')
		return redirect(url_for('item'))
	return render_template('index.html')




 def login():
	error = None
	g.db = connect_db()
	if request.method == 'POST':
		user = request.form['username']
		cur = g.db.execute("SELECT rowid FROM users WHERE Name = ?", (user,))
		data = cur.fetchone()
		g.db.close()
		if data is None:
			error = 'Invalid Credential. Please try again.'
		else:
			session['logged_in'] = True
			flash('You were just logged in.')
			return redirect(url_for('item'))
	return render_template('login.html', error=error)
   
    
    
 
# Main page


@app.route('/todo', methods=['GET', 'POST'])
def items():
	g.db= connection()
	if request.methods == 'POST':
		newItem = request.form ['New_Item']
		#cursor = 
		connection.execute("SELECT rowid From items WHERE name = ?", (newItem,))
		#theFetch =cursor.fetchone()
	return render_template('todo.html')

    g.db.close()

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
# Connect to data base
def connection():
	return sqlite3.connect("database.db")


if __name__ == '__main__':
	app.run(debug=True)

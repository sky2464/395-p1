from flask import Flask, flash, redirect, render_template, request, session, abort, g
import sqlite3
from functools import wraps

# Create Flask object
app = Flask(__name__)

app.database = "database.db"


def connection_db():
    return sqlite3.connect(app.database)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        flash('Hereeeeeeeeee i goooooooooooooo')
        session['logged_in'] = True
        flash('You were just logged in.')
        return redirect("todo.html")
    return render_template('index.html')


@app.route('/login')
def login():
    flash('Welcome')
    return render_template("todo.html")


@app.route('/logout')
def logout():
    flash('Logged out')
    return render_template("index.html")


@app.route("/register")
def register():
    # return render_template("register.html")
    return render_template('register.html')


'''create account '''


@app.route('/create', methods=['GET', 'POST'])
def create():
    return render_template("register.html")


@app.route('/register')
def register():
    # return redirect(url_for('index'))
    flash('Now log in')
    return render_template("home.html")


@app.route('/todo')
# def todo():
# return render_template('todo.html')
# to do list
g.db.close()
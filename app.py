from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
import sys
from flask_sqlalchemy import SQLAlchemy
import db_model
import queries as q

app = Flask(__name__)
app.run(debug=False)

app.secret_key = 'you gonna finish that'

############### CHANGE THIS FOR UR SPECIC MACHINE ###############
app.config['MYSQL_HOST'] = 'localhost' 
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Password123!'
app.config['MYSQL_DB'] = 'RMP_DB'

mysql = MySQL(app)

#db = SQLAlchemy(app)

@app.route('/')
@app.route('/login', methods =['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'uname' in request.form and 'upass' in request.form:
        username = request.form['uname']
        password = request.form['upass']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        # cursor.execute('SELECT * FROM USER WHERE uname = % s AND upass = % s', (username, password, ))
        # user = cursor.fetchone()
        user = q.login_query(cursor,username,password)
        if user:
            session['loggedin'] = True
            session['id'] = user['uid']
            session['uname'] = user['uname']
            msg = 'Logged in successfully !'
            return render_template('index2.html', msg = msg)
        else:
            msg = 'Incorrect username / password !'
    return render_template('login.html', msg = msg)
  
@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('uname', None)
    return redirect(url_for('login'))
  
@app.route('/register', methods =['GET', 'POST'])
def register():
    msg = ''
    if request.method == 'POST' and 'uname' in request.form and 'upass' in request.form :
        uname = request.form['uname']
        upass = request.form['upass']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

        user = q.register_query(cursor, uname, upass)

        if user:
            msg = 'Account already exists !'
        elif not re.match(r'[A-Za-z0-9]+', uname):
            msg = 'Username must contain only characters and numbers !'
        elif not uname or not upass:
            msg = 'Please fill out the form !'
        else:
            #cursor.execute('INSERT INTO USER VALUES (% s, % s, % s)', (id, uname, upass ))
            q.add_user(cursor, uname, upass)
            mysql.connection.commit()
            msg = 'You have successfully registered !'
    elif request.method == 'POST':
        msg = 'Please fill out the form !'
    return render_template('register.html', msg = msg)

@app.route('/professor_default', methods = ['GET', 'POST'])
def professor_default():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    prof_default_table = q.load_prof_default(cursor)

    # dict_prof_table = {}
    # for i in prof_default_table
    #print(prof_default_table)
    return render_template('professors.html', prof_default_table=prof_default_table)

@app.route('/prof_info', methods = ['GET', 'POST'])
def prof_info():
    # cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    # prof_default_table = q.load_prof_default(cursor)

    # dict_prof_table = {}
    # for i in prof_default_table
    #print(prof_default_table)
    return render_template('prof_info.html')
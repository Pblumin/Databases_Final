from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
from flask import request
import MySQLdb.cursors
import re
import sys
#from flask_sqlalchemy import SQLAlchemy
import db_model
import queries as q

app = Flask(__name__)
app.run(debug=False)

app.secret_key = 'you gonna finish that'

############### CHANGE THIS FOR UR SPECIC MACHINE ###############
# app.config['MYSQL_HOST'] = 'localhost' 
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = 'Password123!'
# app.config['MYSQL_DB'] = 'RMP_DB'
app.config['MYSQL_HOST'] = 'localhost' 
# app.config['MYSQL_USER'] = 'paul'
# app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Mysqlpass123!'
app.config['MYSQL_DB'] = 'RMP_DB'

mysql = MySQL(app)

#db = SQLAlchemy(app)

############################# LOGIN IN APIS #############################
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

############################# CLICKING ON PROFESSOR TAB APIS #############################
@app.route('/professor_default', methods = ['GET', 'POST'])
def professor_default():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    input = request.args.get('search')
    if input == None:
        prof_default_table = q.load_prof_default(cursor)
    else:
        prof_default_table = q.get_prof_by_name(cursor,input)

    return render_template('professors.html', prof_default_table=prof_default_table)

@app.route('/professor_reverse', methods = ['GET', 'POST'])
def professor_reverse():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    input = request.args.get('search')
    if input == None:
        prof_default_table = q.load_prof_reverse(cursor)
    else:
        prof_default_table = q.get_prof_by_name(cursor,input)

    return render_template('professors.html', prof_default_table=prof_default_table)

@app.route('/professor_diff', methods = ['GET', 'POST'])
def professor_diff():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    input = request.args.get('search')
    if input == None:
        prof_default_table = q.load_prof_diff(cursor)
    else:
        prof_default_table = q.get_prof_by_name(cursor,input)

    return render_template('professors.html', prof_default_table=prof_default_table)

@app.route('/professor_diff_reverse', methods = ['GET', 'POST'])
def professor_diff_reverse():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    input = request.args.get('search')
    if input == None:
        prof_default_table = q.load_prof_diff_reverse(cursor)
    else:
        prof_default_table = q.get_prof_by_name(cursor,input)

    return render_template('professors.html', prof_default_table=prof_default_table)

@app.route('/professor_abc', methods = ['GET', 'POST'])
def professor_abc():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    input = request.args.get('search')
    if input == None:
        prof_default_table = q.load_prof_abc(cursor)
    else:
        prof_default_table = q.get_prof_by_name(cursor,input)

    return render_template('professors.html', prof_default_table=prof_default_table)

############################# CLICKING ON SCHOOL TAB APIS #############################
@app.route('/school_default', methods = ['GET', 'POST'])
def school_default():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    input = request.args.get('search')
    if input == None:
        school_default_table = q.load_school_default(cursor)
    else:
        school_default_table = q.get_school_by_name(cursor,input)

    return render_template('schools.html', school_default_table=school_default_table)

@app.route('/school_reverse', methods = ['GET', 'POST'])
def school_reverse():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    school_default_table = q.load_school_reverse(cursor)
    input = request.args.get('search')
    if input == None:
        school_default_table = q.load_school_reverse(cursor)
    else:
        school_default_table = q.get_school_by_name(cursor,input)

    return render_template('schools.html', school_default_table=school_default_table)

@app.route('/school_abc', methods = ['GET', 'POST'])
def school_abc():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    input = request.args.get('search')
    if input == None:
        school_default_table = q.load_school_abc(cursor)
    else:
        school_default_table = q.get_prof_by_name(cursor,input)

    return render_template('schools.html', school_default_table=school_default_table)

############################# VIEWING THE PROFESSOR PAGE API #############################
@app.route('/prof_info/<pid>', methods = ['GET', 'POST'])
def prof_info(pid):
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    prof_table = q.get_prof_by_id(cursor, pid)
    class_table = q.get_classes_by_prof(cursor, pid)
    review_table = q.get_reviews(cursor, pid)
    rec_perc = q.get_rec_perc(cursor, pid)

    return render_template('prof_info.html', prof_table=prof_table, class_table=class_table, review_table=review_table, rec_perc=rec_perc)

@app.route('/add_like/<rid>', methods = ['GET', 'POST'])
def add_like(rid):
    uid = session['id']
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    q.add_like(cursor, rid, uid)
    mysql.connection.commit()
    print("added like!")
    pid = q.get_pid(cursor, rid)
    print("pid value: ", pid)
    prof_table = q.get_prof_by_id(cursor, pid)
    class_table = q.get_classes_by_prof(cursor, pid)
    review_table = q.get_reviews(cursor, pid)
    rec_perc = q.get_rec_perc(cursor, pid)
    
    print()

    return render_template('prof_info.html', prof_table=prof_table, class_table=class_table, review_table=review_table, rec_perc=rec_perc)

############################# CLICKING ON SCHOOL FROM SCHOOL TAB API #############################
@app.route('/professor_by_school/<sid>', methods = ['GET', 'POST'])
def professor_by_school(sid):
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    prof_default_table = q.load_prof_by_school(cursor,sid)
    input = request.args.get('search')
    if input == None:
        prof_default_table = q.load_prof_by_school(cursor,sid)
    else:
        prof_default_table = q.get_prof_by_name(cursor,input)
        return render_template('professors.html', prof_default_table=prof_default_table)
    
    return render_template('professors_school.html', prof_default_table=prof_default_table, sid=sid)

@app.route('/professor_by_school_rev/<sid>', methods = ['GET', 'POST'])
def professor_by_school_rev(sid):
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

    input = request.args.get('search')
    if input == None:
        prof_default_table = q.load_prof_by_school_rev(cursor,sid)
    else:
        prof_default_table = q.get_prof_by_name(cursor,input)
        return render_template('professors.html', prof_default_table=prof_default_table)

    return render_template('professors_school.html', prof_default_table=prof_default_table, sid=sid)

@app.route('/professor_by_school_diff/<sid>', methods = ['GET', 'POST'])
def professor_by_school_diff(sid):
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

    input = request.args.get('search')
    if input == None:
        prof_default_table = q.load_prof_by_school_diff(cursor,sid)
    else:
        prof_default_table = q.get_prof_by_name(cursor,input)
        return render_template('professors.html', prof_default_table=prof_default_table)

    return render_template('professors_school.html', prof_default_table=prof_default_table, sid=sid)

@app.route('/professor_by_school_diff_rev/<sid>', methods = ['GET', 'POST'])
def professor_by_school_diff_rev(sid):
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

    input = request.args.get('search')
    if input == None:
        prof_default_table = q.load_prof_by_school_diff_rev(cursor,sid)
    else:
        prof_default_table = q.get_prof_by_name(cursor,input)
        return render_template('professors.html', prof_default_table=prof_default_table)

    return render_template('professors_school.html', prof_default_table=prof_default_table, sid=sid)

@app.route('/professor_by_school_abc/<sid>', methods = ['GET', 'POST'])
def professor_by_school_abc(sid):
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

    input = request.args.get('search')
    if input == None:
        prof_default_table = q.load_prof_by_school_abc(cursor,sid)
    else:
        prof_default_table = q.get_prof_by_name(cursor,input)
        return render_template('professors.html', prof_default_table=prof_default_table)

    return render_template('professors_school.html', prof_default_table=prof_default_table, sid=sid)

############################# LIKES STUFF #############################


@app.route('/add_prof_form', methods = ['GET','POST'])
def add_prof_form():
    msg = ''
    if request.method == 'POST' and 'profname' in request.form and 'profschool' in request.form and 'profclasses' in request.form:
        profname = request.form['profname']
        # So thinking we could just use these to query for more 
        # specific professors or ignore them entirely - he wont care
        # maybe we could just upadte these to all resulting professors
        # profschool = request.form['profschool']
        profclasses = request.form['profclasses']
        profschool = request.form['profschool']
        classes=profclasses.split(",")

        # also check if the existcount is actually updated
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

        prof = q.check_prof_exists_initial(cursor, profschool,profname)
        #if the prof exists 
        if prof:
            prof = q.inc_prof_existcount(cursor, profname)
            msg = 'Thank you for updating the database !'

        #if the prof doesnt exist
        else:
            q.add_prof(cursor, profschool, profname)
            msg = 'Professor is not in our database but is added now'

        for profclass in classes:
            q.add_class(cursor, profclass.strip(), profname)

            mysql.connection.commit()

    return render_template('add_prof_form.html', msg = msg)

   
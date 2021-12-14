from flask import session

# LOGIN QUERIES
def login_query(cursor, username, password):
    cursor.execute('SELECT * \
                    FROM USER \
                    WHERE uname = % s AND upass = % s',
                    (username, password, ))
    
    user = cursor.fetchone()

    return user

def register_query(cursor, uname, upass):
    cursor.execute('SELECT * \
                    FROM USER \
                    WHERE uname = % s AND upass = % s',
                    (uname, upass))
    user = cursor.fetchone()
    
    return user

# GET MAX IDS QUERIES
def max_user_id(cursor):
    cursor.execute('SELECT max(uid) as maxID \
                    FROM USER')
    max_id = cursor.fetchone()

    return max_id

def max_prof_id(cursor):
    cursor.execute('SELECT max(pid) as maxID \
                        FROM PROFESSOR')
    max_id = cursor.fetchone()

    return max_id

def max_rev_id(cursor):
    cursor.execute('SELECT max(rid) as maxID \
                    FROM REVIEW')
    max_id = cursor.fetchone()

    return max_id

def max_class_id(cursor):
    cursor.execute('SELECT max(cid) as maxID \
                    FROM CLASS')
    max_id = cursor.fetchone()

    return max_id

def max_likes_id(cursor):
    cursor.execute('SELECT max(lid) as maxID \
                    FROM LIKES')
    max_id = cursor.fetchone()

    return max_id

# Query 1
def load_prof_default(cursor):

    query = """ SELECT p.pid, p.pname, s.sname, avg(r.overall) as avgRating, avg(r.difficulty) as avgDiff
                FROM  SCHOOL s, PROFESSOR p 
                LEFT JOIN REVIEW r on p.pid=r.pid
                WHERE p.sid=s.sid and p.existcount>=2
                GROUP BY p.pid
                ORDER BY avg(r.overall) desc """

    cursor.execute(query)
    prof_default_table = cursor.fetchall()

    return prof_default_table

def load_prof_reverse(cursor):

    query = """ SELECT p.pid, p.pname, s.sname, avg(r.overall) as avgRating, avg(r.difficulty) as avgDiff
                FROM  SCHOOL s, PROFESSOR p 
                LEFT JOIN REVIEW r on p.pid=r.pid
                WHERE p.sid=s.sid and p.existcount>=2
                GROUP BY p.pid
                ORDER BY avg(r.overall) """

    cursor.execute(query)
    prof_default_table = cursor.fetchall()

    return prof_default_table

def load_prof_diff(cursor):

    query = """ SELECT p.pid, p.pname, s.sname, avg(r.overall) as avgRating, avg(r.difficulty) as avgDiff
                FROM  SCHOOL s, PROFESSOR p 
                LEFT JOIN REVIEW r on p.pid=r.pid
                WHERE p.sid=s.sid and p.existcount>=2
                GROUP BY p.pid
                ORDER BY avgDiff desc """

    cursor.execute(query)
    prof_default_table = cursor.fetchall()

    return prof_default_table

def load_prof_diff_reverse(cursor):

    query = """ SELECT p.pid, p.pname, s.sname, avg(r.overall) as avgRating, avg(r.difficulty) as avgDiff
                FROM  SCHOOL s, PROFESSOR p 
                LEFT JOIN REVIEW r on p.pid=r.pid
                WHERE p.sid=s.sid and p.existcount>=2
                GROUP BY p.pid
                ORDER BY avgDiff"""

    cursor.execute(query)
    prof_default_table = cursor.fetchall()

    return prof_default_table

def load_prof_abc(cursor):

    query = """ SELECT p.pid, p.pname, s.sname, avg(r.overall) as avgRating, avg(r.difficulty) as avgDiff
                FROM  SCHOOL s, PROFESSOR p 
                LEFT JOIN REVIEW r on p.pid=r.pid
                WHERE p.sid=s.sid and p.existcount>=2
                GROUP BY p.pid
                ORDER BY p.pname"""

    cursor.execute(query)
    prof_default_table = cursor.fetchall()

    return prof_default_table


def load_prof_by_school(cursor, sid):

    q1 = """ SELECT p.pid, p.pname, s.sname, avg(r.overall) as avgRating, avg(r.difficulty) as avgDiff
                FROM  SCHOOL s, PROFESSOR p 
                LEFT JOIN REVIEW r on p.pid=r.pid
                WHERE p.sid=s.sid and p.existcount>=2 and s.sid = """
    q2 = """ GROUP BY p.pid
            ORDER BY avg(r.overall) desc """
    query = q1 + str(sid) + q2
    cursor.execute(query)
    prof_default_table = cursor.fetchall()

    return prof_default_table

def load_prof_by_school_rev(cursor, sid):

    q1 = """ SELECT p.pid, p.pname, s.sname, avg(r.overall) as avgRating, avg(r.difficulty) as avgDiff
                FROM  SCHOOL s, PROFESSOR p 
                LEFT JOIN REVIEW r on p.pid=r.pid
                WHERE p.sid=s.sid and p.existcount>=2 and s.sid = """
    q2 = """ GROUP BY p.pid
            ORDER BY avg(r.overall) """
    query = q1 + str(sid) + q2
    cursor.execute(query)
    prof_default_table = cursor.fetchall()

    return prof_default_table

def load_prof_by_school_diff(cursor, sid):

    q1 = """ SELECT p.pid, p.pname, s.sname, avg(r.overall) as avgRating, avg(r.difficulty) as avgDiff
                FROM  SCHOOL s, PROFESSOR p 
                LEFT JOIN REVIEW r on p.pid=r.pid
                WHERE p.sid=s.sid and s.sid = """
    q2 = """ GROUP BY p.pid
            ORDER BY avgDiff desc """
    query = q1 + str(sid) + q2
    cursor.execute(query)
    prof_default_table = cursor.fetchall()

    return prof_default_table

def load_prof_by_school_diff_rev(cursor, sid):

    q1 = """ SELECT p.pid, p.pname, s.sname, avg(r.overall) as avgRating, avg(r.difficulty) as avgDiff
                FROM  SCHOOL s, PROFESSOR p 
                LEFT JOIN REVIEW r on p.pid=r.pid
                WHERE p.sid=s.sid and p.existcount>=2 and s.sid = """
    q2 = """ GROUP BY p.pid
            ORDER BY avgDiff """
    query = q1 + str(sid) + q2
    cursor.execute(query)
    prof_default_table = cursor.fetchall()

    return prof_default_table

def load_prof_by_school_abc(cursor, sid):

    q1 = """ SELECT p.pid, p.pname, s.sname, avg(r.overall) as avgRating, avg(r.difficulty) as avgDiff
                FROM  SCHOOL s, PROFESSOR p 
                LEFT JOIN REVIEW r on p.pid=r.pid
                WHERE p.sid=s.sid and p.existcount>=2 and s.sid = """
    q2 = """ GROUP BY p.pid
            ORDER BY p.pname """
    query = q1 + str(sid) + q2
    cursor.execute(query)
    prof_default_table = cursor.fetchall()

    return prof_default_table

def load_school_default(cursor):
    query = """ SELECT s.sid, s.sname, COUNT(p.pid) as profCnt
                FROM SCHOOL s, PROFESSOR p
                WHERE p.sid=s.sid
                GROUP BY s.sid
                ORDER BY profCnt desc """

    cursor.execute(query)
    school_default_table = cursor.fetchall()

    return school_default_table

def load_school_reverse(cursor):
    query = """ SELECT s.sid, s.sname, COUNT(p.pid) as profCnt
                FROM SCHOOL s, PROFESSOR p
                WHERE p.sid=s.sid
                GROUP BY s.sid
                ORDER BY profCnt """

    cursor.execute(query)
    school_default_table = cursor.fetchall()

    return school_default_table

def load_school_abc(cursor):
    query = """ SELECT s.sid, s.sname, COUNT(p.pid) as profCnt
                FROM SCHOOL s, PROFESSOR p
                WHERE p.sid=s.sid
                GROUP BY s.sid
                ORDER BY s.sname """

    cursor.execute(query)
    school_default_table = cursor.fetchall()

    return school_default_table

    
def get_prof_by_name(cursor, input):
    
    likestr = "'%" + input + "%' "
    testquery = """ SELECT p.pname, s.sname, avg(r.overall) as avgRating, avg(r.difficulty) as avgDiff
                FROM PROFESSOR p, SCHOOL s, REVIEW r
                WHERE p.sid=s.sid and r.pid=p.pid and p.existcount=2 and p.pname LIKE '%Keene%'
                GROUP BY p.pid
                ORDER BY avg(r.overall) desc """

    q1 = """SELECT p.pid, p.pname, s.sname, avg(r.overall) as avgRating, avg(r.difficulty) as avgDiff
            FROM PROFESSOR p, SCHOOL s, REVIEW r
            WHERE p.sid=s.sid and r.pid=p.pid and p.existcount>=2 and p.pname LIKE """
    
    q2 = """GROUP BY p.pid
            ORDER BY avg(r.overall) desc"""

    query = q1 + likestr + q2 

    cursor.execute(query)
    prof = cursor.fetchall()

    return prof



def get_prof_by_name_initial(cursor, profname):
    
    profname="'"+str(profname)+"'"
 
    q1 = """select pid from PROFESSOR where pname="""

    query = q1 + profname

    cursor.execute(query)
    prof = cursor.fetchone()

    return prof

def get_prof_by_id(cursor, id):
    

    q1 = """SELECT p.pid, p.pname, s.sname, avg(r.overall) as avgRating, avg(r.difficulty) as avgDiff
            FROM SCHOOL s, PROFESSOR p
            LEFT JOIN REVIEW r on p.pid=r.pid
            WHERE p.sid=s.sid and p.existcount>=2 and p.pid =  """

    query = q1 + str(id)

    cursor.execute(query)
    prof = cursor.fetchone()

    return prof


def get_school_by_name(cursor, input):

    likestr = "'%" + input + "%' "

    testquery = """ SELECT s.sname, COUNT(p.pid) as profCnt
                FROM SCHOOL s, PROFESSOR p
                WHERE p.sid=s.sid and s.sname LIKE '%Cooper%'
                GROUP BY s.sid
                ORDER BY profCnt desc """
    
    q1 = """SELECT s.sid, s.sname, COUNT(p.pid) as profCnt
            FROM SCHOOL s, PROFESSOR p
            WHERE p.sid=s.sid and s.sname LIKE"""

    q2 = """ GROUP BY s.sid
            ORDER BY profCnt desc """
    
    query = q1 + likestr + q2 

    cursor.execute(query)
    school = cursor.fetchall()

    return school


# Query 5
def get_prof_by_class(cursor, input):
    likestr = "'%" + input + "%') "
    
    testquery = """ SELECT p.pname, s.sname, avg(r.overall) as avgRating, avg(r.difficulty) as avgDiff
                    FROM PROFESSOR p, SCHOOL s, REVIEW r
                    WHERE p.sid=s.sid and r.pid=p.pid and p.existcount=2 and 
                        p.pid = (SELECT c.pid
                                FROM CLASS c
                                WHERE c.cname LIKE '%physics%')
                    GROUP BY p.pid
                    ORDER BY avg(r.overall) desc """
    
    q1 = """SELECT p.pname, s.sname, avg(r.overall) as avgRating, avg(r.difficulty) as avgDiff
            FROM PROFESSOR p, SCHOOL s, REVIEW r
            WHERE p.sid=s.sid and r.pid=p.pid and p.existcount>=2 and 
                p.pid = (SELECT c.pid
                        FROM CLASS c
                        WHERE c.cname LIKE """

    q2 = """GROUP BY p.pid
            ORDER BY avg(r.overall) desc"""

    query = q1 + likestr + q2

    cursor.execute(query)
    prof = cursor.fetchall()

    return prof

# Query 6
def prof_count(cursor):

    query = """SELECT s.sname, COUNT(p.pid) as profCnt
                FROM SCHOOL s, PROFESSOR p
                WHERE s.sid=p.sid
                GROUP BY s.sid"""

    cursor.execute(query)
    prof_cnt_table = cursor.fetchone()

    return prof_cnt_table

# Query 7
def get_classes_by_prof(cursor, pid):

    q1 = """SELECT p.pname, c.cname
            FROM PROFESSOR p, CLASS c
            WHERE c.pid=p.pid and p.pid="""

    query = q1 + str(pid)

    cursor.execute(query)
    class_list = cursor.fetchall()

    return class_list


def get_avg_prof_rating(cursor, prof):

    likestr = "'%" + prof + "%' "

    q1 = """SELECT avg(r.overall) as profAvg
            FROM PROFESSOR p, REVIEW r
            WHERE p.pid=r.pid and p.pname LIKE """
    
    query = q1 + likestr
    cursor.execute(query)
    avg_rating = cursor.fetchone()

    return avg_rating

# Query 11
def get_avg_prof_diff(cursor, prof):
    likestr = "'%" + prof + "%' "

    q1 = """SELECT avg(r.difficulty) as profAvg
            FROM PROFESSOR p, REVIEW r
            WHERE p.pid=r.pid and p.pname LIKE """
    
    query = q1 + likestr
    cursor.execute(query)
    avg_difficulty = cursor.fetchall()

    return avg_difficulty


def get_reviews(cursor, pid):
  
    testq = """select t.rid, t.difficulty, t.overall, t.recommend, t.description, count(t.lid) as numOfLikes
                from (select r.rid, r.pid, l.lid, r.difficulty, r.overall, r.recommend, r.description
                    from REVIEW r 
                    LEFT JOIN LIKES l 
                    on r.rid=l.rid where r.pid=31) as t
                group by t.rid"""

    q1 = """SELECT t.rid, t.difficulty, t.overall, t.recommend, t.description, count(t.lid) as numOfLikes
            FROM (SELECT r.rid, r.pid, l.lid, r.difficulty, r.overall, r.recommend, r.description
                    FROM REVIEW r 
                    LEFT JOIN LIKES l 
                    ON r.rid=l.rid where r.pid="""
    q2 = """) as t
                group by t.rid"""

    query = q1 + str(pid) + q2
    cursor.execute(query)
    reviews = cursor.fetchall()

    return reviews


def get_rec_perc(cursor, pid):

    q1 = """SELECT ((sum(r.recommend)/count(r.rid)) * 100) as rec_prec
            FROM PROFESSOR p, REVIEW r
            WHERE p.pid=r.pid and p.pid = """

    query = q1 + str(pid) 

    cursor.execute(query)
    recommend_percent = cursor.fetchall()

    return recommend_percent


def add_user(cursor, uname, upass):

    max_id = max_user_id(cursor)
    id = max_id.get('maxID') + 1
    
    cursor.execute('INSERT INTO USER VALUES (% s, % s, % s)', (id, uname, upass ))

def get_professor_pid(cursor, input):

    likestr = "'%" + input + "%' "
    
    q1= """select s.sid from PROFESSOR p, SCHOOL s 
    where p.sid=s.sid and s.sname LIKE """
    
    q2=""" limit 1"""
   
    query = q1 + likestr + q2 

    cursor.execute(query)
    school_sid = cursor.fetchone()

    return school_sid

def get_school_sid(cursor, input):

    likestr = "'%" + input + "%' "

    q1= """select s.sid from PROFESSOR p, SCHOOL s 
    where p.sid=s.sid and s.sname LIKE """
    
    q2=""" limit 1"""
    
    query = q1 + likestr + q2 

    cursor.execute(query)
    school_sid = cursor.fetchone()

    return school_sid

def add_prof(cursor, school, pname):

    max_id = max_prof_id(cursor)
    id = max_id.get('maxID') + 1

    school_data = get_school_sid(cursor, school)
    sid = school_data.get('sid')

    cursor.execute('INSERT INTO PROFESSOR VALUES (% s, % s, % s, % s)', 
    (id, sid, pname, 1 ))


def add_class(cursor, cname, pname):

    max_id = max_class_id(cursor)
    id = max_id.get('maxID') + 1
    
    professor_data = get_prof_by_name_initial(cursor, pname)
    pid = professor_data.get('pid')

    cursor.execute('INSERT INTO CLASS VALUES (% s, % s, % s)', 
    (id, pid, cname))

  
def add_review(cursor, overall, difficulty, recommendation, description, pid,  uid):
    max_id = max_rev_id(cursor)
    id = max_id.get('maxID') + 1

    cursor.execute('INSERT INTO REVIEW VALUES (% s, % s, % s, % s,% s, % s, % s)', 
    (id, pid, uid, difficulty, overall, recommendation, description))
    pass

 
def add_like(cursor, rid, uid):

    max_id = max_likes_id(cursor)
    id = max_id.get('maxID') + 1
   
    cursor.execute('INSERT INTO LIKES VALUES (% s, % s, % s)', (id, rid, uid ))


def inc_prof_existcount(cursor, pid):
    
    r1 = """UPDATE PROFESSOR as p 
            SET existcount = existcount + 1 
            WHERE p.pid= """
    
    cursor.execute(r1 + str(pid))

    return 1

def get_pid(cursor, rid):

    q1="""SELECT pid from REVIEW WHERE rid="""

    query = q1 + str(rid) 

    cursor.execute(query)
    result = cursor.fetchone()
    pid = result.get('pid')

    return pid


def check_prof_exists(cursor, rid):

    q1="""SELECT pid from REVIEW WHERE rid="""

    query = q1 + str(rid) 

    cursor.execute(query)
    result = cursor.fetchone()
    pid = result.get('pid')

    return pid


def check_prof_exists_initial(cursor, schoolname, profname):
    schoolname=str(schoolname)
    profname=str(profname)
    query="select count(*) from PROFESSOR p, SCHOOL s where p.sid=s.sid and s.sname='{}' and p.pname='{}' ".format(schoolname,profname)

    cursor.execute(query)
    result = cursor.fetchone()
    count = result.get('count(*)')

    if count <= 0: 
        return False
    else:
        return True

def load_pending_prof(cursor, sid):

    q1 = """ SELECT p.pid, p.pname, s.sname, s.sid
                FROM  SCHOOL s, PROFESSOR p 
                WHERE p.sid=s.sid and p.existcount<2 and s.sid = """

    query = q1 + str(sid)
    cursor.execute(query)
    prof_default_table = cursor.fetchall()

    return prof_default_table

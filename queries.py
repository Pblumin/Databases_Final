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

'''
Queries we are gonna need:
DONE 1. when you click on professors tab see the following:
    table that has pname, school, 
    average overall review rating, average difficulty review rating
    order by rating (AND A QUERY THAT REVISES THE ORDER?)

IN PROGRESS 2. when you click on schools tab see the following:
    table that has school and top 3 professors
    order by school (on front end also will see query 6)

DONE 3. Search by professor: (takes in user input)
    query 1 but add a like claus (ie like=%input%)

DONE 4. Search by school: (takes in user input)
    query 2 but add a like claus

DONE 5. Search by class: (takes in user input)
    table should be like query 1 
    but you need to do a subquery to get the pid from class using like claus

DONE 6. get number of professors at a school

DONE 7. Get a list of all classes taught by a professor
    (add this under each prof in frontend?)

FRONTEND STUFF 8. When clicking on a specific school:
    does query 1

FRONTEND STUFF 9. When clicking on a specific professor: (takes in input)
    on front end see the following info:
    name, classes taught (query 7), 
    avg rating (query 10), avg rating (query 11), % recommend (query 13)
    all reviews (query 12) 
     
DONE 10. get average prof rating (input a prof)

DONE 11. get average difficulty rating (input a prof)

DONE 12. get all the reviews for a professor (input a prof):
    table that has the follow:
    diff, overall rating, recommend, description, num of likes
    order by like count

DONE 13. get the % of people that would recommend professor (input professor)

------------- adding/update db -------------
DONE 14. add a user 

DONE 15. add a professor 

DONE 16. add a class

LOOK INTO WHEN PROF PAGE DONE 17. add a review

LOOK INTO WHEN PROF PAGE DONE 18. add a like

DONE 19. update professor exist count

'''

# Query 1
def load_prof_default(cursor):

    query = """ SELECT p.pid, p.pname, s.sname, avg(r.overall) as avgRating, avg(r.difficulty) as avgDiff
                FROM PROFESSOR p, SCHOOL s, REVIEW r
                WHERE p.sid=s.sid and r.pid=p.pid and p.existcount=2
                GROUP BY p.pid
                ORDER BY avg(r.overall) desc """

    cursor.execute(query)
    prof_default_table = cursor.fetchall()

    return prof_default_table

def load_prof_reverse(cursor):

    query = """ SELECT p.pid, p.pname, s.sname, avg(r.overall) as avgRating, avg(r.difficulty) as avgDiff
                FROM PROFESSOR p, SCHOOL s, REVIEW r
                WHERE p.sid=s.sid and r.pid=p.pid and p.existcount=2
                GROUP BY p.pid
                ORDER BY avg(r.overall) """

    cursor.execute(query)
    prof_default_table = cursor.fetchall()

    return prof_default_table

def load_prof_diff(cursor):

    query = """ SELECT p.pid, p.pname, s.sname, avg(r.overall) as avgRating, avg(r.difficulty) as avgDiff
                FROM PROFESSOR p, SCHOOL s, REVIEW r
                WHERE p.sid=s.sid and r.pid=p.pid and p.existcount=2
                GROUP BY p.pid
                ORDER BY avgDiff desc """

    cursor.execute(query)
    prof_default_table = cursor.fetchall()

    return prof_default_table

def load_prof_diff_reverse(cursor):

    query = """ SELECT p.pid, p.pname, s.sname, avg(r.overall) as avgRating, avg(r.difficulty) as avgDiff
                FROM PROFESSOR p, SCHOOL s, REVIEW r
                WHERE p.sid=s.sid and r.pid=p.pid and p.existcount=2
                GROUP BY p.pid
                ORDER BY avgDiff"""

    cursor.execute(query)
    prof_default_table = cursor.fetchall()

    return prof_default_table


def load_prof_by_school(cursor, sid):

    q1 = """ SELECT p.pid, p.pname, s.sname, avg(r.overall) as avgRating, avg(r.difficulty) as avgDiff
                FROM PROFESSOR p, SCHOOL s, REVIEW r
                WHERE p.sid=s.sid and r.pid=p.pid and s.sid = """
    q2 = """ GROUP BY p.pid
            ORDER BY avg(r.overall) desc """
    query = q1 + str(sid) + q2
    cursor.execute(query)
    prof_default_table = cursor.fetchall()

    return prof_default_table

def load_prof_by_school_rev(cursor, sid):

    q1 = """ SELECT p.pid, p.pname, s.sname, avg(r.overall) as avgRating, avg(r.difficulty) as avgDiff
                FROM PROFESSOR p, SCHOOL s, REVIEW r
                WHERE p.sid=s.sid and r.pid=p.pid and s.sid = """
    q2 = """ GROUP BY p.pid
            ORDER BY avg(r.overall) """
    query = q1 + str(sid) + q2
    cursor.execute(query)
    prof_default_table = cursor.fetchall()

    return prof_default_table
# Query 2
# 2. when you click on schools tab see the following:
#     table that has school and top 3 professors
#     order by school (on front end also will see query 6)
def load_school_default(cursor):
    query = """ SELECT s.sid, s.sname, COUNT(p.pid) as profCnt
                FROM SCHOOL s, PROFESSOR p
                WHERE p.sid=s.sid
                GROUP BY s.sid
                ORDER BY profCnt desc """

    cursor.execute(query)
    school_default_table = cursor.fetchall()

    return school_default_table

# NOT WORKING FIGURE OUT
# http://www.silota.com/docs/recipes/sql-top-n-group.html

#this query gives the top rat
#SELECT p.pname,s.sname,avg(r.overall) as avgoverall from PROFESSOR p, SCHOOL s, REVIEW r where p.sid=s.sid and r.pid=p.pid and p.existcount>=2 group by r.pid order by avgoverall desc;

def top_3_prof(cursor):

    query = """ SELECT p.pname, s.sname, avg(r.overall) as avgRating,
                row_number() over (partition by s.sname order by avgRating desc) as rank 
                FROM PROFESSOR p, SCHOOL s, REVIEW r
                WHERE p.sid=s.sid and r.pid=p.pid and p.existcount=2 and rank <= 1"""
    top_3_prof = cursor.fetchall()

    return top_3_prof

# Query 3       
def get_prof_by_name(cursor, input):
    
    likestr = "'%" + input + "%' "
    testquery = """ SELECT p.pname, s.sname, avg(r.overall) as avgRating, avg(r.difficulty) as avgDiff
                FROM PROFESSOR p, SCHOOL s, REVIEW r
                WHERE p.sid=s.sid and r.pid=p.pid and p.existcount=2 and p.pname LIKE '%Keene%'
                GROUP BY p.pid
                ORDER BY avg(r.overall) desc """

    q1 = """SELECT p.pid, p.pname, s.sname, avg(r.overall) as avgRating, avg(r.difficulty) as avgDiff
            FROM PROFESSOR p, SCHOOL s, REVIEW r
            WHERE p.sid=s.sid and r.pid=p.pid and p.existcount=2 and p.pname LIKE """
    
    q2 = """GROUP BY p.pid
            ORDER BY avg(r.overall) desc"""

    query = q1 + likestr + q2 

    cursor.execute(query)
    prof = cursor.fetchall()

    return prof

def get_prof_by_id(cursor, id):
    
    #likestr = str(id)

    q1 = """SELECT p.pid, p.pname, s.sname, avg(r.overall) as avgRating, avg(r.difficulty) as avgDiff
            FROM PROFESSOR p, SCHOOL s, REVIEW r
            WHERE p.sid=s.sid and r.pid=p.pid and p.existcount=2 and p.pid =  """
    

    query = q1 + str(id)

    cursor.execute(query)
    prof = cursor.fetchall()

    return prof


# Query 4
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
            WHERE p.sid=s.sid and r.pid=p.pid and p.existcount=2 and 
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

    #likestr = "'%" + input + "%' "
    
    testquery = """SELECT p.pname, c.cname
                    FROM PROFESSOR p, CLASS c
                    WHERE c.pid=p.pid and p.pname LIKE '%vul%' """

    q1 = """SELECT p.pname, c.cname
            FROM PROFESSOR p, CLASS c
            WHERE c.pid=p.pid and p.pid="""

    query = q1 + str(pid)

    cursor.execute(query)
    class_list = cursor.fetchall()

    return class_list


# Query 10
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

# 12. get all the reviews for a professor (input a prof):
#     table that has the follow:
#     diff, overall rating, recommend, description, num of likes
#     order by like count
# HAD TO GET RID OF LIKES COUNT FOR NOW CAUSE THERES A ISSUE WHEN THERE R NO LIKES  
def get_reviews(cursor, pid):
    # likestr = "'%" + prof + "%' "
    testq = """SELECT r.rid, r.difficulty, r.overall, r.recommend, r.description, count(l.lid) numOfLikes
            FROM PROFESSOR p, REVIEW r, LIKES l
            WHERE p.pid=r.pid and l.rid=r.rid and p.pid = 7
            GROUP BY l.rid
            ORDER BY numOfLikes desc"""

    q1 = """SELECT r.rid, r.difficulty, r.overall, r.recommend, r.description
            FROM PROFESSOR p, REVIEW r
            WHERE p.pid=r.pid and p.pid = """
    
    # q2 = """ GROUP BY l.rid
    #         ORDER BY numOfLikes desc"""

    # '''SELECT r.difficulty, r.overall, r.recommend, r.description, count(l.lid) numOfLikes
    # FROM PROFESSOR p, REVIEW r, LIKES l
    # WHERE p.pid=r.pid and l.rid=r.rid and p.pname LIKE '%vul%'
    # GROUP BY l.rid
    # ORDER BY numOfLikes desc'''

    query = q1 + str(pid)
    cursor.execute(query)
    reviews = cursor.fetchall()

    return reviews


# Query 13

def get_rec_perc(cursor, pid):

    # likestr = "'%" + prof + "%' "

    testquery = """ SELECT p.pname, (sum(r.recommend)/count(r.rid)) as rec_prec
                    FROM PROFESSOR p, REVIEW r
                    WHERE p.pid=r.pid and p.pname LIKE '%neveen%'
                    GROUP BY p.pid"""

    q1 = """SELECT ((sum(r.recommend)/count(r.rid)) * 100) as rec_prec
            FROM PROFESSOR p, REVIEW r
            WHERE p.pid=r.pid and p.pid = """

    query = q1 + str(pid) 

    cursor.execute(query)
    recommend_percent = cursor.fetchall()

    return recommend_percent

# Query 14 - add user
def add_user(cursor, uname, upass):

    max_id = max_user_id(cursor)
    id = max_id.get('maxID') + 1
    
    cursor.execute('INSERT INTO USER VALUES (% s, % s, % s)', (id, uname, upass ))

# Query 15 - add prof
def add_prof(cursor, school, pname):

    max_id = max_prof_id(cursor)
    id = max_id.get('maxID') + 1

    school_data = get_school_by_name(cursor, school)
    sid = school_data.get('s.sid')

    cursor.execute('INSERT INTO PROFESSOR VALUES (% s, % s, % s, % s)', 
    (id, sid, pname, 0 ))

# Query 16 - add class
def add_class(cursor, cname, pname):

    max_id = max_class_id(cursor)
    id = max_id.get('maxID') + 1
    
    professor_data = get_prof_by_name(cursor, pname)
    pid = professor_data.get('p.pid')

    cursor.execute('INSERT INTO CLASS VALUES (% s, % s, % s)', 
    (id, pid, cname))

# DO LATER WHEN PROF PAGE IS WORKING    
def add_review(cursor):
    pass

# Query 18 - add a like

# DO LATER WHEN PROF PAGE IS WORKING    
def add_like(cursor, rid, uid):

    max_id = max_user_id(cursor)
    id = max_id.get('maxID') + 1
    
    cursor.execute('INSERT INTO USER VALUES (% s, % s, % s)', (id, rid, uid ))

# Query 19 - update professor exist count

def inc_prof_existcount(cursor, prof):
    
    r1 = 'UPDATE professor as p \
        SET existcount = existcount + 1 \
        WHERE p.pname LIKE '

    likestr = "'%" + prof + "%'"

    
    cursor.execute(r1 + likestr)
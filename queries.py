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

12. get all the reviews for a professor (input a prof):
    table that has the follow:
    diff, overall rating, recommend, description, num of likes
    order by like count

13. get the % of people that would recommend professor (input professor)

------------- adding/update db -------------
DONE 14. add a user 

15. add a professor 

16. add a class

17. add a review

18. add a like

19. update professor exist count

'''

# Query 1
def load_prof_default(cursor):

    query = """ SELECT p.pname, s.sname, avg(r.overall) as avgRating, avg(r.difficulty) as avgDiff
                FROM PROFESSOR p, SCHOOL s, REVIEW r
                WHERE p.sid=s.sid and r.pid=p.pid and p.existcount=2
                GROUP BY p.pid
                ORDER BY avg(r.overall) desc """

    cursor.execute(query)
    prof_default_table = cursor.fetchone()

    return prof_default_table

# Query 2
# 2. when you click on schools tab see the following:
#     table that has school and top 3 professors
#     order by school (on front end also will see query 6)
def load_school_default(cursor):
    query = """ SELECT s.sname, COUNT(p.pid) as profCnt
                FROM SCHOOL s, PROFESSOR p
                WHERE p.sid=s.sid
                GROUP BY s.sid
                ORDER BY profCnt desc """

    cursor.execute(query)
    school_default_table = cursor.fetchone()

    return school_default_table

# NOT WORKING FIGURE OUT
# http://www.silota.com/docs/recipes/sql-top-n-group.html
def top_3_prof(cursor):

    query = """ SELECT p.pname, s.sname, avg(r.overall) as avgRating,
                row_number() over (partition by s.sname order by avgRating desc) as rank 
                FROM PROFESSOR p, SCHOOL s, REVIEW r
                WHERE p.sid=s.sid and r.pid=p.pid and p.existcount=2 and rank <= 1"""
    
    cursor.execute(query)
    top_3_prof = cursor.fetchone()

    return top_3_prof

# Query 3       
def get_prof_by_name(cursor, input):
    
    likestr = "'%" + input + "%' "
    testquery = """ SELECT p.pname, s.sname, avg(r.overall) as avgRating, avg(r.difficulty) as avgDiff
                FROM PROFESSOR p, SCHOOL s, REVIEW r
                WHERE p.sid=s.sid and r.pid=p.pid and p.existcount=2 and p.pname LIKE '%Keene%'
                GROUP BY p.pid
                ORDER BY avg(r.overall) desc """

    q1 = """SELECT p.pname, s.sname, avg(r.overall) as avgRating, avg(r.difficulty) as avgDiff
            FROM PROFESSOR p, SCHOOL s, REVIEW r
            WHERE p.sid=s.sid and r.pid=p.pid and p.existcount=2 and p.pname LIKE """
    
    q2 = """GROUP BY p.pid
            ORDER BY avg(r.overall) desc"""

    query = q1 + likestr + q2 

    cursor.execute(query)
    prof = cursor.fetchone()

    return prof

# Query 4
def get_school_by_name(cursor, input):

    likestr = "'%" + input + "%' "

    testquery = """ SELECT s.sname, COUNT(p.pid) as profCnt
                FROM SCHOOL s, PROFESSOR p
                WHERE p.sid=s.sid and s.sname LIKE '%Cooper%'
                GROUP BY s.sid
                ORDER BY profCnt desc """
    
    q1 = """SELECT s.sname, COUNT(p.pid) as profCnt
            FROM SCHOOL s, PROFESSOR p
            WHERE p.sid=s.sid and s.sname LIKE"""

    q2 = """ GROUP BY s.sid
            ORDER BY profCnt desc """
    
    query = q1 + likestr + q2 

    cursor.execute(query)
    school = cursor.fetchone()

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
    prof = cursor.fetchone()

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
def get_classes_by_prof(cursor, input):

    likestr = "'%" + input + "%' "
    
    testquery = """SELECT p.pname, c.cname
                    FROM PROFESSOR p, CLASS c
                    WHERE c.pid=p.pid and p.pname LIKE '%vul%' """

    q1 = """SELECT p.pname, c.cname
            FROM PROFESSOR p, CLASS c
            WHERE c.pid=p.pid and p.pname LIKE """

    query = q1 + likestr

    cursor.execute(query)
    class_list = cursor.fetchone()

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
    avg_difficulty = cursor.fetchone()

    return avg_difficulty

# 12. get all the reviews for a professor (input a prof):
#     table that has the follow:
#     diff, overall rating, recommend, description, num of likes
#     order by like count
def get_avg_prof_diff(cursor, prof):
    likestr = "'%" + prof + "%' "

    q1 = """SELECT r.diff, r.overall, r.recommend, r.description, r.
            FROM PROFESSOR p, REVIEW r
            WHERE p.pid=r.pid and p.pname LIKE"""
    
    query = q1 + likestr
    cursor.execute(query)
    avg_difficulty = cursor.fetchone()

    return avg_difficulty


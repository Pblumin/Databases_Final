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
1. when you click on professors tab see the following:
    table that has pname, school, 
    average overall review rating, average difficulty review rating
    order by rating (AND A QUERY THAT REVISES THE ORDER?)

2. when you click on schools tab see the following:
    table that has school and top 3 professors
    order by school (on front end also will see query 6)

3. Search by professor: (takes in user input)
    query 1 but add a like claus (ie like=%input%)

4. Search by school: (takes in user input)
    query 2 but add a like claus

5. Search by class: (takes in user input)
    table should be like query 1 
    but you need to do a subquery to get the pid from class using like claus

6. get number of professors at a school

7. Get a list of all classes taught by a professor
    (add this under each prof in frontend?)

8. When clicking on a specific school:
    does query 1

9. When clicking on a specific professor: (takes in input)
    on front end see the following info:
    name, classes taught (query 7), 
    avg rating (query 10), avg rating (query 11), % recommend (query 13)
    all reviews (query 12) 
     
10. get average prof rating (input a prof)

11. get average difficulty rating (input a prof)

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

# when you click on professors tab see the following:
#     table that has pname, school, 
#     average overall review rating, average difficulty review rating
#     order by rating (AND A QUERY THAT REVISES THE ORDER?)

def load_init_page(cursor):

    query = """ SELECT p.pname, s.sname, avg(r.overall) as avgRating, avg(r.difficulty) as avgDiff
                FROM PROFESSOR p, SCHOOL s, REVIEW r
                WHERE p.sid=s.sid and r.pid=p.pid and p.existcount=2
                GROUP BY p.pid
                ORDER BY avg(r.overall) desc"""

    cursor.execute(query)
    prof_init_table = cursor.fetchone()

    return prof_init_table
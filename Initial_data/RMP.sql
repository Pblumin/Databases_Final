/*
SQL queries to create and populate dataset

CLASS
*/

CREATE TABLE SCHOOL(sid INTEGER,
    sname CHAR(20),
    PRIMARY KEY (sid));

CREATE TABLE PROFESSOR(pid INTEGER,
    sid INTEGER,
    pname CHAR(40),
    existcount INTEGER,
    PRIMARY KEY (pid),
    FOREIGN KEY (sid) references SCHOOL(sid));

CREATE TABLE CLASS( cid INTEGER,
    pid INTEGER,
    cname CHAR(50),
    PRIMARY KEY (cid),
    FOREIGN KEY (pid) references PROFESSOR(pid));

CREATE TABLE USER( uid INTEGER,
    uname CHAR(20),
    upass CHAR(20),
    PRIMARY KEY (uid));

CREATE TABLE REVIEW( rid INTEGER,
    pid INTEGER,
    uid INTEGER,
    difficulty INTEGER,
    overall INTEGER,
    recommend BOOLEAN,
    description CHAR(255),
    PRIMARY KEY (rid),
    FOREIGN KEY (pid) references PROFESSOR(pid),
    FOREIGN KEY (uid) references USER(uid) );

CREATE TABLE LIKES( lid INTEGER,
    rid INTEGER,
    uid INTEGER,
    PRIMARY KEY (lid),
    FOREIGN KEY (rid) references REVIEW(rid),
    FOREIGN KEY (uid) references USER(uid));


/*insert into sailors values (22,'dusting',7,45);*/

/*SCHOOLS - sid, name*/
insert into SCHOOL values (1, 'Cooper Union');
insert into SCHOOL values (2, 'Columbia');

/*Professor - pid, sid, name, existcount*/
insert into PROFESSOR values (1, 1, 'Leonid Vulakh', 2);
insert into PROFESSOR values (2, 1, 'Fred Fontaine', 2);
insert into PROFESSOR values (3, 1, 'Yahshodhan Risbud', 2);
insert into PROFESSOR values (4, 1, 'Stuart Kirtman', 2);
insert into PROFESSOR values (5, 1, 'Jeff Hakner', 2);
insert into PROFESSOR values (6, 1, 'Sam Keene', 2);
insert into PROFESSOR values (7, 1, 'Carl Sable', 2);
insert into PROFESSOR values (8, 1, 'Eugene Sokolov', 2);
insert into PROFESSOR values (9, 1, 'William Germano', 2);
insert into PROFESSOR values (10, 1, 'Neveen Shlayan', 2);


/*Classes - cid, pid, name*/
insert into CLASS values (1, 1, 'Calculus 1');
insert into CLASS values (2, 1, 'Calculus 2');
insert into CLASS values (3, 1, 'Differential Equations');

insert into CLASS values (4, 2, 'Signals Processing');
insert into CLASS values (5, 2, 'Finance');

insert into CLASS values (6, 3, 'Digital Logic and Design');

insert into CLASS values (7, 4, 'Junior Lab');
insert into CLASS values (8, 4, 'Computer Architecture');

insert into CLASS values (10, 5, 'Operating Systems');
insert into CLASS values (11, 5, 'Electromagnetics');

insert into CLASS values (12, 6, 'Machine Learning');
insert into CLASS values (13, 6, 'Digital Signals Processing');

insert into CLASS values (14, 7, 'DSA 2');
insert into CLASS values (15, 7, 'NLP');

insert into CLASS values (16, 8, 'Databases');

insert into CLASS values (17, 9, 'Polar Expedition');
insert into CLASS values (18, 9, 'Opera');

insert into CLASS values (19, 10, 'Electronics 2');
insert into CLASS values (20, 10, 'Gastronomy');


/*User - uid, uname, upass*/
insert into USER values (1, 'Awesomephil7', '#ilovedb');
insert into USER values (2, 'Pcucchi', 'plantplayer');
insert into USER values (3, 'Winner', 'cuise2022');
insert into USER values (4, 'NPR', 'fries');

/*Review - rid, pid, uid, difficuly, overallrating, recommendbool, review */
/*FIX IN PROPOSOAL THERE WERE TWO OVERALL REVIEWS; GET RID OF THE CHAR ONE
ALSO I THINK WE SHOULD GET OF SEMESTER TAKEN
MAYBE WE CAN GET RID OF OVERALL DIFF AS WELL*/
insert into REVIEW values (1, 1, 1, 3, 5, 1, 'Awesome guy!')
insert into REVIEW values (2, 7, 4, 1, 5, 1, 'DSA2 was easy for me! You need to be nice at coding tho.')

/*LIKES - lid, rid, user*/
insert into LIKES values (1, 1, 1);
insert into LIKES values (1, 1, 2);
insert into LIKES values (1, 1, 3);
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
insert into SCHOOL values (3, 'NYU');

/*Professor - pid, sid, name, existcount*/
/*Cooper Profs*/
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

/*Columbia Profs*/
insert into PROFESSOR values (11, 2, 'Claire Catenaccio', 2);
insert into PROFESSOR values (12, 2, 'Robert Thurman', 2);
insert into PROFESSOR values (13, 2, 'Richard Braverman', 2);
insert into PROFESSOR values (14, 2, 'Herbert Terrace', 2);
insert into PROFESSOR values (15, 2, 'David Albert', 2);
insert into PROFESSOR values (16, 2, 'David Yerkes', 2);
insert into PROFESSOR values (17, 2, 'Richard Howard', 2);
insert into PROFESSOR values (18, 2, 'Amanda Claybaugh', 2);
insert into PROFESSOR values (19, 2, 'Rene Testa', 2);
insert into PROFESSOR values (20, 2, 'Joseph Slaughter', 2);

/*NYU Profs*/
insert into PROFESSOR values (21, 3, 'Partha Debroy', 2);
insert into PROFESSOR values (22, 3, 'Julia Keefer', 2);
insert into PROFESSOR values (23, 3, 'Alan Corns', 2);
insert into PROFESSOR values (24, 3, 'Hasia Diner', 2);
insert into PROFESSOR values (25, 3, 'Steve Hutkins', 2);
insert into PROFESSOR values (26, 3, 'Tyler Volk', 2);
insert into PROFESSOR values (27, 3, 'Barbara Heyns', 2);
insert into PROFESSOR values (28, 3, 'Joel Spencer', 2);
insert into PROFESSOR values (29, 3, 'Phillip Kaim', 2);
insert into PROFESSOR values (30, 3, 'Steve Blader', 2);



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

insert into CLASS values (21, 11, 'Greek');
insert into CLASS values (22, 11, 'Theater');

insert into CLASS values (23, 12, 'Physics 201');

insert into CLASS values (24, 13, 'Physics 301');

insert into CLASS values (25, 14, 'Physics 301');

insert into CLASS values (26, 15, 'Ancient Greece');

insert into CLASS values (27, 16, 'Artifical Intelligence');

insert into CLASS values (28, 17, 'Computer Vision');

insert into CLASS values (29, 18, 'Psychology');

insert into CLASS values (30, 19, 'Business 101');

insert into CLASS values (31, 20, 'Creative Writing');

insert into CLASS values (32, 21, 'Biology');

insert into CLASS values (33, 22, 'Film');

insert into CLASS values (34, 23, 'Macro');

insert into CLASS values (35, 24, 'Micro');

insert into CLASS values (36, 25, 'Chemistry');

insert into CLASS values (37, 26, 'E&M Physics');

insert into CLASS values (38, 27, 'Gender Studies');

insert into CLASS values (39, 28, 'How to Economics');

insert into CLASS values (40, 29, 'Intro to Python');

insert into CLASS values (41, 30, 'English');




/*User - uid, uname, upass*/
insert into USER values (1, 'Awesomephil7', '#ilovedb');
insert into USER values (2, 'Pcucchi', 'plantplayer');
insert into USER values (3, 'Winner', 'cruise2022');
insert into USER values (4, 'NPR', 'fries');

/*Review - rid, pid, uid, difficuly, overallrating, recommendbool, review */
/*FIX IN PROPOSOAL THERE WERE TWO OVERALL REVIEWS; GET RID OF THE CHAR ONE
ALSO I THINK WE SHOULD GET OF SEMESTER TAKEN
MAYBE WE CAN GET RID OF OVERALL DIFF AS WELL*/
insert into REVIEW values (1, 1, 1, 3, 5, 1, 'Awesome guy!');
insert into REVIEW values (2, 7, 4, 1, 5, 1, 'DSA2 was easy for me! You need to be nice at coding tho.');
insert into REVIEW values (3, 1, 1, 1, 4, 0, 'Awesome guy!');
insert into REVIEW values (4, 2, 1, 3, 3, 1, 'Awesome guy!');
insert into REVIEW values (5, 3, 1, 4, 2, 0, 'Awesome guy!');
insert into REVIEW values (6, 4, 1, 2, 1, 1, 'Awesome guy!');
insert into REVIEW values (7, 4, 1, 3, 2, 0, 'Awesome guy!');
insert into REVIEW values (8, 3, 1, 5, 3, 1, 'Awesome guy!');
insert into REVIEW values (9, 6, 1, 2, 4, 1, 'Awesome guy!');
insert into REVIEW values (10, 6, 1, 1, 5, 0, 'Awesome guy!');
insert into REVIEW values (11, 7, 1, 2, 3, 1, 'Awesome guy!');
insert into REVIEW values (12, 7, 1, 3, 2, 0, 'Awesome guy!');
insert into REVIEW values (13, 8, 1, 4, 1, 1, 'Awesome guy!');
insert into REVIEW values (14, 9, 2, 2, 3, 1, 'Cool guy!');
insert into REVIEW values (15, 9, 3, 3, 2, 0, 'Cool guy!');
insert into REVIEW values (16, 9, 4, 4, 1, 1, 'Cool guy!');
insert into REVIEW values (17, 10, 2, 2, 3, 1, 'Cool guy!');
insert into REVIEW values (18, 10, 1, 3, 2, 0, 'Cool guy!');
insert into REVIEW values (19, 10, 3, 4, 1, 1, 'Cool guy!');
insert into REVIEW values (20, 7, 1, 2, 3, 1, 'Cool guy!');
insert into REVIEW values (21, 5, 2, 3, 2, 0, 'Cool guy!');
insert into REVIEW values (22, 2, 1, 4, 1, 1, 'Cool guy!');

insert into REVIEW values (23, 15, 2, 1, 5, 1, 'Cool!');
insert into REVIEW values (24, 16, 3, 1, 5, 1, 'Cool guy!');
insert into REVIEW values (25, 17, 1, 5, 3, 1, 'Do not take this professor');
insert into REVIEW values (26, 18, 1, 2, 4, 1, 'A lot of assignments!');
insert into REVIEW values (27, 19, 1, 1, 5, 0, 'Gives no homework!');
insert into REVIEW values (28, 20, 1, 2, 3, 1, 'Ends class early!');
insert into REVIEW values (28, 21, 1, 2, 3, 1, 'Awesome guy!');
insert into REVIEW values (28, 22, 1, 2, 3, 1, 'Awesome guy!');
insert into REVIEW values (28, 23, 1, 2, 3, 1, 'Awesome guy!');


/*LIKES - lid, rid, user*/
insert into LIKES values (1, 1, 1);
insert into LIKES values (2, 1, 2);
insert into LIKES values (3, 1, 3);
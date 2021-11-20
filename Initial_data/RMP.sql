/*
SQL queries to create and populate dataset

CLASS

*/

/*
create table sailors(
    sid int PRIMARY KEY,
    sname varchar(30),
    rating int,
    age int
);

create table reserves(
    sid int,
    bid int,
    day date,
	PRIMARY KEY (sid, bid, day)
);

create table boats(
    bid int PRIMARY KEY,
	bname char(20),
	color char(10),
	length int
);
*/

CREATE TABLE PROFESSOR( pid INTEGER,
    sid INTEGER,
    pname CHAR(20),
    existcount INTEGER,
    PRIMARY KEY (pid),
    FOREIGN KEY (sid) );

CREATE TABLE SCHOOL( sid INTEGER,
    sname CHAR(20),
    PRIMARY KEY (sid));

CREATE TABLE CLASS( cid INTEGER,
    pid INTEGER,
    cname CHAR(20),
    PRIMARY KEY (cid),
    FOREIGN KEY (pid) );

CREATE TABLE REVIEW( rid INTEGER,
    pid INTEGER,
    uid INTEGER,
    overall CHAR(20),
    difficulty INTEGER,
    overall INTEGER,
    recommend BOOLEAN,
    semester_taken CHAR(20),
    description CHAR(500),
    PRIMARY KEY (rid),
    FOREIGN KEY (pid),
    FOREIGN KEY (uid) );

CREATE TABLE LIKES( lid INTEGER,
    rid INTEGER,
    uid INTEGER,
    PRIMARY KEY (lid),
    FOREIGN KEY (rid),
    FOREIGN KEY (uid));

CREATE TABLE USER( uid INTEGER,
    uname CHAR(20),
    upass CHAR(20),
    PRIMARY KEY (uid));

/*insert into sailors values (22,'dusting',7,45);*/
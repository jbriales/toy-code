#!/bin/sh
# bash script to create toy test sqlite3 database

dbfile="testDB.sqlite"

if [ -e $dbfile ]; then
  echo "test db already exists, removing"
  rm $dbfile
fi

# Create table following directions in tutorial:
# https://www.tutorialspoint.com/sqlite/sqlite_quick_guide.htm
sqlite3 $dbfile <<EOF
.header on
.mode column

create table n (id INTEGER PRIMARY KEY,f TEXT,l TEXT);
insert into n (f,l) values ('john','smith');
select * from n;

CREATE TABLE COMPANY(
   ID INT PRIMARY KEY     NOT NULL,
   NAME           VARCHAR NOT NULL,
   AGE            INT     NOT NULL,
   ADDRESS        TEXT,
   SALARY         REAL
);

CREATE TABLE DEPARTMENT(
   ID INT PRIMARY KEY      NOT NULL,
   DEPT           CHAR(50) NOT NULL,
   EMP_ID         INT      NOT NULL
);

.tables
.schema COMPANY

INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)
VALUES (1, 'Paul', 32, 'California', 20000.00 );

INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)
VALUES (2, 'Allen', 25, 'Texas', 15000.00 );

INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)
VALUES (3, 'Teddy', 23, 'Norway', 20000.00 );

INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)
VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 );

INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)
VALUES (5, 'David', 27, 'Texas', 85000.00 );

INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)
VALUES (6, 'Kim', 22, 'South-Hall', 45000.00 );

INSERT INTO COMPANY VALUES (7, 'James', 24, 'Houston', 10000.00 );

SELECT * from COMPANY;
EOF

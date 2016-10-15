# Constantine Athanitis, Stiven Peter, Kate Johnston
# DB1 Work 6

import sqlite3
import csv

fileName = "newDB.db"

db = sqlite3.connect(fileName)
c = db.cursor()


##PEEPS table

q = "CREATE TABLE students (name TEXT, id INTEGER, age INTEGER)"

c.execute(q)

fObj = open("peeps.csv")
d=csv.DictReader(fObj)

for row in d:
    insert = "INSERT INTO students VALUES ('" + row["name"] +"'," +row["id"]+","+ row["age"]+")"
   ## print insert
    c.execute(insert)

    
##COURSES table
    
q = "CREATE TABLE courses (code TEXT, id INTEGER, mark INTEGER)"

c.execute(q)

fObj = open("courses.csv")
d = csv.DictReader(fObj)

for row in d:
    insert2 = "INSERT INTO courses VALUES ('" + row["code"] +"'," + row["id"]+ "," +row["mark"]+")"
    ##print insert2
    c.execute(insert2)

db.commit()
db.close()

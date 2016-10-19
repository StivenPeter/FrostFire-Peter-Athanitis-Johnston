import sqlite3

db = sqlite3.connect("newDB.db")
c = db.cursor()

s = "SELECT name, students.id, mark FROM students, courses WHERE students.id = courses.id"

t = c.execute(s)

for record in t:
    print record

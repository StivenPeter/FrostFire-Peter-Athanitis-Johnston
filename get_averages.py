import sqlite3

db = sqlite3.connect("newDB.db")
c = db.cursor()

cmd = "SELECT name, courses.id, mark FROM students, courses WHERE students.id = courses.id"

sel = c.execute(cmd)

name = "kruder"
iD = 1
num=0.0
sUM=0.0


for record in sel:
    if (record[0] == name and iD == record[1]):
        
        num = num + 1
        sUM = sUM + record[2]
 
    else:
        print "Name: " + name
        print "ID: " + str(iD)
        print "Average: " + str(sUM/num)
        print "======================"
        name = record[0]
        iD = record[1]
        num=1.0
        sUM=record[2]

print "Name: " + name
print "ID: " + str(iD)
print "Average: " + str(sUM/num)

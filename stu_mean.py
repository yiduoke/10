import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O

f="discobandit.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE
c.execute("SELECT name, mark FROM peeps, courses WHERE peeps.id = courses.id;")
list = c.fetchall()
print(list)
print "\n"

dict = {};
for tuple in list:
    dict[tuple[0] ] = [0.0, 0.0, 0.0]
    #[total points, number of classes, avg]

for tuple in list:
    dict[tuple[0] ][0] += tuple[1]
    dict[tuple[0] ][1] += 1

print(dict)

for student in dict:
    dict[student][2] = dict[student][0] / dict[student][1]

print(dict)
#==========================================================
command = "CREATE TABLE IF NOT EXISTS averages (name TEXT, average NUMERIC);"          #put SQL statement in this string                               
c.execute(command)    #run SQL statement                                       

for student in dict:
    c.execute("INSERT INTO averages VALUES(" + student + "," + str(dict[student][2]) + ")")
    c.execute("SELECT * FROM averages;")
    print "\n"
    print(c.fetchall())
 
#==========================================================
db.commit() #save changes
db.close()  #close database

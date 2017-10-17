import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O

f="discobandit.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE
command = "CREATE TABLE IF NOT EXISTS courses (code TEXT, mark INTEGER, id INTEGER);"          #put SQL statement in this string
c.execute(command)    #run SQL statement

command = "CREATE TABLE IF NOT EXISTS peeps (name TEXT, age INTEGER, id INTEGER);"          #put SQL statement in this string
c.execute(command)    #run SQL statement

with open('data/courses.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        c.execute("INSERT INTO courses VALUES (?,?,?)", [row["code"], row["mark"], row["id"]])        
c.execute("SELECT * FROM courses;")
print(c.fetchall())
print "\n"


with open('data/peeps.csv') as csvfile:
    reader1 = csv.DictReader(csvfile)
    for row in reader1:
        c.execute("INSERT INTO peeps VALUES (?,?,?)", [row["name"], row["age"], row["id"]])
c.execute("SELECT * FROM peeps;")
print(c.fetchall())

#==========================================================
db.commit() #save changes
db.close()  #close database
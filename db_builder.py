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


with open('data/peeps.csv') as csvfile:
    reader1 = csv.DictReader(csvfile)
    for row in reader1:
        c.execute("INSERT INTO peeps VALUES (?,?,?)", [row["name"], row["age"], row["id"]])

c.execute("SELECT name, mark FROM peeps, courses WHERE peeps.id=courses.id;")
rows = c.fetchall()
dict = {}

current=rows[0][0]
currentSum=0
divideBy=0;
for thing in rows:
    if thing[0]!=current:
        dict[current]=currentSum/divideBy
        current=thing[0]
        currentSum=0
        divideBy=0
    currentSum+=thing[1]
    divideBy=divideBy+1

c.execute("CREATE TABLE IF NOT EXISTS peeps_avg (name TEXT, average INTEGER);")
for key in dict:
    c.execute("INSERT INTO peeps_avg VALUES(?,?)",[key, dict[key]])
#==========================================================
db.commit() #save changes
db.close()  #close database

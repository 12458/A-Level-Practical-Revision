import sqlite3

f1 = open("SALES.txt")
sales = []
tech = []
for item in f1:
	sales.append(item.strip().split(','))
f2 = open("TECH_SUPPORT.txt")

for item in f2:
	tech.append(item.strip().split(','))

db = sqlite3.connect('records.db')
cur = db.cursor()

for item in sales:
	cur.execute("INSERT INTO Employee VALUES(?,?,?,?,?,?)",
	(int(item[0]), item[1], "Sales", item[2],item[3]))
	
	cur.execute("INSERT INTO Sales VALUES(?,?)",
	(int(item[0]),int(item[4])))
	
for item in tech:
	cur.execute("INSERT INTO Employee VALUES(?,?,?,?,?,?)",
	(int(item[0]), item[1], "Tech_support", item[2], item[3]]))
	
	cur.execute("INSERT INTO Tech_support VALUES(?,?)",
	(int(item[0]),int(item[4])))

f1.close()
f2.close()
db.commit()
db.close()
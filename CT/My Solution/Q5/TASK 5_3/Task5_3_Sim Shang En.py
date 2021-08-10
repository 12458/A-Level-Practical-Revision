l = []
with open("IGP.CSV", "r") as f:
    import csv
    r = csv.reader(f)
    l = list(r)

import sqlite3

conn = sqlite3.connect('uni.db')

with conn:
    sql = '''
    CREATE TABLE UAS (
    id INTEGER AUTO INCREMENT PRIMARY KEY,
	school TEXT,
   	course TEXT,
	igp REAL
    );
    '''
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()

    for i in l:
        sql = '''
        INSERT INTO UAS(school,course,igp) VALUES (?,?,?);
        '''
        cur.execute(sql, (i[0], i[1], i[2]))
        conn.commit()
    
        
    

import sqlite3

from flask import Flask, render_template

from TASK4_2_NgJunSiang_COMP import JuniorCollege

app = Flask(__name__)

@app.route('/')
def home():
    c = sqlite3.connect('schools.db')
    cur = c.cursor()

    # METHOD 1
    # Get school info first
    cur.row_factory = sqlite3.Row
    cur.execute('''
SELECT SchoolID,Name,Zone FROM School
WHERE Name = 'NANYANG JUNIOR COLLEGE';
''')
    sch = cur.fetchone()
    school = JuniorCollege(
        sch['SchoolID'],
        sch['Name'],
        sch['Zone']
    )

    # Get subject info
    cur.execute('''
SELECT Name FROM Subject
WHERE SchoolID = ?;
''', (sch['SchoolID'],))
    subjects = []
    for row in cur.fetchall():
        subjects.append(row[0])
    c.close()
    
    # METHOD 2: Use the SQL lookup from Task 4_3 to retrieve data
    
    return render_template(
        'index.html',
        school=school,
        subjects=subjects)

app.run()

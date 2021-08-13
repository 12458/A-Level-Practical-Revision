from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def root():
    school = 'NANYANG JUNIOR COLLEGE'
    with sqlite3.connect('schools.db') as conn:
        cur = conn.cursor()
        sql = \
            """
            SELECT s.Zone, s.SchoolID FROM School s WHERE s.Name = ?
            """
        zone, schoolid = cur.execute(sql, (school,)).fetchone()

        sql = \
            """
            SELECT sub.Name FROM Subject sub
            INNER JOIN SchoolSubject schsub ON schsub.SubjectID = sub.SubjectID
            WHERE schsub.SchoolID = ?
            """
        
        subjects = cur.execute(sql, (schoolid,)).fetchall()

    return render_template('index.html', zone=zone, school=school, subjects=subjects)


app.run(debug=True)
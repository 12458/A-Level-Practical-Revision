import csv
with open('subjects_offered.csv') as f:
    c = csv.reader(f)
    next(c)
    subjects = list(c)

subject_unique = list(set([i[1] for i in subjects]))

import sqlite3
with sqlite3.connect('schools.db') as conn:
    cur = conn.cursor()
    for subject in subject_unique:
        cur.execute('INSERT INTO Subject(Name) VALUES (?)', (subject,))
    conn.commit()

    cur.execute('SELECT * FROM Subject')
    subject_with_id = cur.fetchall()
    subject_lut = {}
    for subject_name in subject_with_id:
        subject_lut[subject_name[1]] = subject_name[0]

    for i in range(len(subjects)):
        subjects[i][1] = subject_lut[subjects[i][1]]
    subjects = [tuple(i) for i in subjects]

    for subject_school in subjects:
        cur.execute('INSERT INTO SchoolSubject(SchoolID,SubjectID) VALUES(?,?)', subject_school)
    
    conn.commit()
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
        cur.execute('INSERT INTO Subject(Name) VALUES (?)', (subject[1]))
    conn.commit()
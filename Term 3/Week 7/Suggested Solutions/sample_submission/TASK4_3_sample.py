import sqlite3, csv



def conn():
    return sqlite3.connect('schools.db')



sql_create = '''
CREATE TABLE IF NOT EXISTS Subject (
    SchoolID INTEGER,
    Name TEXT,
    PRIMARY KEY (SchoolID, Name)
);
'''
sql_delete = '''
DELETE FROM Subject;
'''
sql_insert_subject = '''
INSERT INTO Subject
VALUES (?, ?);
'''

sql_insert_schsubj = '''
INSERT INTO SchoolSubject
VALUES (?, ?, ?);
'''



c = conn()
cur = c.cursor()
cur.row_factory = sqlite3.Row

# Clear old values
cur.execute(sql_create)
cur.execute(sql_delete)

# Method 1: manually generate and track subjIDs
subjectids = {}
next_subj_id = 1

f = open('subjects_offered.csv', 'r')
for row in csv.DictReader(f):
    # Lookup subject id
    subj_id = subjectids.get(row['subject_desc'], None)  # if not found, default to None
    if subj_id is None:
            subj_id = next_subj_id
            next_subj_id += 1
    # Insert subject record
    cur.execute(
        sql_insert_subject, (
            subj_id,
            row['subject_desc'],
        )
    )
    # Insert junction table record
    cur.execute(
        sql_insert_schsubj, (
            row['school_id'],
            subj_id,
            row['subject_desc'],
        )
    )
f.close()
c.commit()
c.close()

import sqlite3, csv

class School:
    def __init__(self, id_, name, zone):
        self.id = id_
        self.name = name
        self.zone = zone

    def safe_name(self):
        name = self.name.replace(' ', '_')
        for symbol in "'.,":
            name = name.replace(symbol, '')
        return name

    def as_record(self):
        return (
            self.id,
            self.name,
            self.zone,
            self.level,
            self.yearsofstudy
        )

class PrimarySchool(School):
    level = 'primary'
    yearsofstudy = 6

class SecondarySchool(School):
    level = 'secondary'
    yearsofstudy = 5

class JuniorCollege(School):
    level = 'junior college'
    yearsofstudy = 2



def conn():
    return sqlite3.connect('schools.db')



sql_create = '''
CREATE TABLE IF NOT EXISTS School (
    SchoolID INTEGER PRIMARY KEY,
    Name TEXT,
    Zone TEXT,
    Level TEXT,
    YearsOfStudy INTEGER
);
'''
sql_delete = '''
DELETE FROM School;
'''
sql_insert = '''
INSERT INTO School
VALUES (?, ?, ?, ?, ?);
'''



c = conn()
cur = c.cursor()
cur.row_factory = sqlite3.Row
cur.execute(sql_create)
cur.execute(sql_delete)

f = open('school_info.csv', 'r')
for row in csv.DictReader(f):
    skip = False
    if row['level'] == 'PRIMARY':
        sch = PrimarySchool(
            row['school_id'],
            row['school_name'],
            row['zone']
        )
    elif row['level'] == 'SECONDARY':
        sch = SecondarySchool(
            row['school_id'],
            row['school_name'],
            row['zone']
        )
    elif row['level'] == 'JUNIOR COLLEGE':
        sch = JuniorCollege(
            row['school_id'],
            row['school_name'],
            row['zone']
        )
    else:
        skip = True

    if not skip:
        cur.execute(sql_insert, sch.as_record())
f.close()
c.commit()
c.close()

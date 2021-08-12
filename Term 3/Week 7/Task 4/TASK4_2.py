class School:
    def __init__(self, _id, name, zone):
        self.id = _id
        self.name = name
        self.zone = zone

    def safe_name(self, s):
        return s.replace(' ', '_').replace("'", '').replace('.','').replace(',','')

    def as_record(self):
        return (self.id, self.name, self.zone, None, None)

class PrimarySchool(School):
    def __init__(self, _id, name, zone):
        self.level = 'primary'
        self.YearOfStudy = 6
        super().__init__(_id, name, zone)
    
    def as_record(self):
        return (self.id, self.name, self.zone, self.level, self.YearOfStudy)

class SecondarySchool(School):
    def __init__(self, _id, name, zone):
        self.level = 'secondary'
        self.YearOfStudy = 5
        super().__init__(_id, name, zone)

    def as_record(self):
        return (self.id, self.name, self.zone, self.level, self.YearOfStudy)

class JuniorCollege(School):
    def __init__(self, _id, name, zone):
        self.level = 'junior college'
        self.YearOfStudy = 2
        super().__init__(_id, name, zone)

    def as_record(self):
        return (self.id, self.name, self.zone, self.level, self.YearOfStudy)

with open('school_info.csv') as f:
    import csv
    c = csv.reader(f)
    next(c)
    c = list(c)
schools = []
for school in c:
    if school[3] == 'PRIMARY':
        schools.append(PrimarySchool(school[0],school[1],school[2]))
    elif school[3] == 'SECONDARY':
        schools.append(SecondarySchool(school[0],school[1],school[2]))
    elif school[3] == 'JUNIOR COLLEGE':
        schools.append(JuniorCollege(school[0],school[1],school[2]))
    else:
        schools.append(School(school[0],school[1],school[2]))


import sqlite3
with sqlite3.connect('schools.db') as conn:
    cur = conn.cursor()
    for school in schools:
        cur.execute('INSERT INTO School(SchoolID, Name, Zone, Level, YearsOfStudy) VALUES (?,?,?,?,?)', school.as_record())
    conn.commit()

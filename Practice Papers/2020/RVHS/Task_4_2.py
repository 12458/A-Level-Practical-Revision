import csv, sqlite3

with open('students.csv') as f:
    # MatricNo,Class,IndexNo,Gender
    c = csv.reader(f)
    next(c)
    students = list(c)

with open('candidates.csv') as f:
    # CandidateNo,Name,Slogan,PortraitLink
    c = csv.reader(f)
    next(c)
    candidates = list(c)

with open('votes.csv') as f:
    # MatricNo,CandidateNo
    c = csv.reader(f)
    next(c)
    votes = list(c)
with sqlite3.connect('voting_mgm.db') as conn:
    cur = conn.cursor()

    for student in students:
        cur.execute('INSERT INTO Student(MatricNo,Class,IndexNo,Gender) VALUES (?,?,?,?)',
        (student[0], student[1], int(student[2]), student[3]))

    for candidate in candidates:
        cur.execute('INSERT INTO Candidate(CandidateNo,Name,Slogan,PortraitLink) VALUES (?,?,?,?)',
        (int(candidate[0]), candidate[1], candidate[2], candidate[3]))

    for vote in votes:
        cur.execute('INSERT INTO Vote(MatricNo,CandidateNo) VALUES (?,?)',
        (vote[0], int(vote[1])))

    conn.commit()

CREATE TABLE School (
    SchoolID INTEGER PRIMARY KEY,
    Name TEXT,
    Zone TEXT,
    Level TEXT,
    YearsOfStudy INTEGER
);
CREATE TABLE Subject (
    SubjectID INTEGER,
    Name TEXT,
    PRIMARY KEY (SubjectID, Name)
);
CREATE TABLE SchoolSubject (
    SchoolID INTEGER,
    SubjectID INTEGER,
    Name TEXT,
    PRIMARY KEY (SchoolID, SubjectID, Name),
    FOREIGN KEY (SchoolID) REFERENCES School(SchoolID),
    FOREIGN KEY (SubjectID) REFERENCES Subject(SubjectID),
    FOREIGN KEY (Name) REFERENCES Subject(Name)
)
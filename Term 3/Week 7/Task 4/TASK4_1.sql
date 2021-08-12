CREATE TABLE "School" (
	"SchoolID"	INTEGER,
	"Name"	TEXT,
	"Zone"	TEXT,
	"Level"	TEXT,
	"YearsOfStudy"	INTEGER,
	PRIMARY KEY("SchoolID")
);

CREATE TABLE "Subject" (
	"SubjectID"	INTEGER,
	"Name"	INTEGER UNIQUE,
	PRIMARY KEY("SubjectID" AUTOINCREMENT)
);

CREATE TABLE "SchoolSubject" (
	"SchoolID"	INTEGER,
	"SubjectID"	INTEGER,
	FOREIGN KEY("SubjectID") REFERENCES "Subject"("SubjectID"),
	FOREIGN KEY("SchoolID") REFERENCES "School"("SchoolID"),
	PRIMARY KEY("SchoolID","SubjectID")
);
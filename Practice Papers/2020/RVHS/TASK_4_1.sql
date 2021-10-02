CREATE TABLE "Student" (
	"MatricNo"	TEXT,
	"Class"	TEXT,
	"IndexNo"	INTEGER,
	"Gender"	TEXT,
	PRIMARY KEY("MatricNo")
);

CREATE TABLE "Cabdidate" (
	"CandidateNo"	INTEGER,
	"Name"	TEXT,
	"Slogan"	TEXT,
	"PortraitLink"	TEXT,
	PRIMARY KEY("CandidateNo" AUTOINCREMENT)
);

CREATE TABLE "Vote" (
	"MatricNo"	TEXT,
	"CandidateNo"	INTEGER,
	PRIMARY KEY("MatricNo","CandidateNo")
);
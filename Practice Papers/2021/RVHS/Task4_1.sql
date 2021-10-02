CREATE TABLE "Car" (
	"VIN"	TEXT,
	"Brand"	TEXT,
	"VehicleType"	TEXT,
	"EnergySource"	TEXT,
	"DailyPrice"	REAL,
	"Avaliability"	TEXT,
	PRIMARY KEY("VIN")
);

CREATE TABLE "Customer" (
	"CustomerID"	INTEGER,
	"Name"	TEXT,
	"Gender"	TEXT,
	"Contact"	TEXT,
	PRIMARY KEY("CustomerID" AUTOINCREMENT)
);

CREATE TABLE "RentalPoint" (
	"PointID"	INTEGER,
	"Address"	TEXT,
	"OpWeekDay"	TEXT,
	"OpStartHour"	TEXT,
	"OpEndHr"	TEXT,
	PRIMARY KEY("PointID" AUTOINCREMENT)
);

CREATE TABLE "RentalRecord" (
	"CustomerID"	TEXT,
	"VIN"	TEXT,
	"StartDate"	TEXT,
	"CollectionPointID"	TEXT,
	"ReturnDate"	TEXT,
	"ReturnPointID"	TEXT,
	FOREIGN KEY("VIN") REFERENCES "Car"("VIN"),
	FOREIGN KEY("CustomerID") REFERENCES "Customer"("CustomerID"),
	FOREIGN KEY("ReturnPointID") REFERENCES "RentalPoint"("PointID"),
	FOREIGN KEY("CollectionPointID") REFERENCES "RentalPoint"("PointID"),
	PRIMARY KEY("CustomerID","VIN","StartDate")
);
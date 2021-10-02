CREATE TABLE "Customer" (
	"CustomerID"	INTEGER,
	"Name"	TEXT NOT NULL,
	"Gender"	TEXT NOT NULL CHECK("Gender" = 'M' OR "Gender" = 'F'),
	"Contact"	TEXT NOT NULL,
	PRIMARY KEY("CustomerID" AUTOINCREMENT)
);

CREATE TABLE "Car" (
	"VIN"	TEXT,
	"Brand"	TEXT NOT NULL,
	"VehicleType"	TEXT NOT NULL CHECK("VehicleType" = 'Sedan' OR "VehicleType" = 'Hatchback' OR "VehicleType" = 'SUV' OR "VehicleType" = 'MPV'),
	"EnergySource"	TEXT NOT NULL CHECK("EnergySource" = 'Diesel' OR "EnergySource" = 'Gasoline' OR "EnergySource" = 'Hybrid' OR "EnergySource" = 'Electricity'),
	"DailyPrice"	REAL NOT NULL,
	"Availability"	TEXT NOT NULL DEFAULT 'Available' CHECK("Availability" = 'Available' OR "Availability" = 'Unavailable'),
	PRIMARY KEY("VIN")
);

CREATE TABLE "RentalPoint" (
	"PointID"	INTEGER,
	"Address"	TEXT NOT NULL,
	"OpWeekDay"	TEXT NOT NULL,
	"OpStartHr"	TEXT NOT NULL,
	"OpEndHr"	TEXT NOT NULL,
	PRIMARY KEY("PointID" AUTOINCREMENT)
);

CREATE TABLE "RentalRecord" (
	"CustomerID"	INTEGER,
	"VIN"	TEXT,
	"StartDate"	TEXT,
	"CollectionPointID"	INTEGER NOT NULL,
	"ReturnDate"	TEXT,
	"ReturnPointID"	INTEGER,
	FOREIGN KEY("ReturnPointID") REFERENCES "RentalPoint"("PointID"),
	FOREIGN KEY("CollectionPointID") REFERENCES "RentalPoint"("PointID"),
	FOREIGN KEY("VIN") REFERENCES "Car"("VIN"),
	FOREIGN KEY("CustomerID") REFERENCES "Customer"("CustomerID"),
	PRIMARY KEY("CustomerID","VIN","StartDate")
);
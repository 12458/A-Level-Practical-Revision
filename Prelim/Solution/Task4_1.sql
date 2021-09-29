CREATE TABLE `Customer` (
	`PersonID`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`FullName`	TEXT,
	`DOB`	TEXT,
	`CreditCardNumber`	TEXT,
	`IsPriority`	INTEGER,
	`SavingAmount`	REAL
);
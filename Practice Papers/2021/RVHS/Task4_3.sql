SELECT c.Name, c.Contact, v.VehicleType, rr.StartDate, rr.ReturnDate, v.DailyPrice
FROM RentalRecord rr
INNER JOIN Customer c ON c.CustomerID = rr.CustomerID
INNER JOIN Car v ON v.VIN = rr.VIN
WHERE c.Name = 'Goh Yi Xi';
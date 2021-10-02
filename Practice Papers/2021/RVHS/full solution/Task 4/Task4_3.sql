SELECT Customer.Name, Customer.Contact, Car.VehicleType, RentalRecord.StartDate,RentalRecord.ReturnDate, Car.DailyPrice
FROM Customer, RentalRecord, Car
WHERE Customer.CustomerID = RentalRecord.CustomerID
AND RentalRecord.VIN = Car.VIN
AND Customer.Name = 'Goh Yi Xi'
ORDER BY RentalRecord.StartDate
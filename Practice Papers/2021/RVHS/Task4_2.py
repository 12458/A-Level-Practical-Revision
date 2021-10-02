import sqlite3
import csv

# exiting with statement inplictly invokes f.close()

with open('customers.csv') as f:
    c = csv.reader(f)
    next(c)
    customers = list(c)

with open('cars.csv') as f:
    c = csv.reader(f)
    next(c)
    cars = list(c)

with open('rental_points.csv') as f:
    c = csv.reader(f)
    next(c)
    rental_points = list(c)

with open('rental_records.csv') as f:
    c = csv.reader(f)
    next(c)
    rental_records = list(c)

with sqlite3.connect('car_rental.db') as conn:
    cur = conn.cursor()
    for car in cars:
        cur.execute('INSERT INTO Car(VIN, Brand, VehicleType, EnergySource, DailyPrice, Avaliability) VALUES (?,?,?,?,?,?)', 
        (car[0], car[1], car[2], car[3], car[4], car[5]))
    # Name,Gender,Contact
    for customer in customers:
        cur.execute('INSERT INTO Customer(Name, Gender, Contact) VALUES (?,?,?)', 
        (customer[1], customer[2], customer[3]))
    # PointID,Address,OpWeekDay,OpStartHr,OpEndHr
    for rental_point in rental_points:
        cur.execute('INSERT INTO RentalPoint(PointID, Address, OpWeekDay, OpStartHr, OpEndHr) VALUES (?,?,?,?,?)', 
        (rental_point[0], rental_point[1], rental_point[2], rental_point[3], rental_point[4]))
    # CustomerID,VIN,StartDate,CollectionPointID,ReturnDate,ReturnPointID
    for rental_record in rental_records:
        cur.execute('INSERT INTO RentalRecord(CustomerID,VIN,StartDate,CollectionPointID,ReturnDate,ReturnPointID) VALUES (?,?,?,?,?,?)', 
        (rental_record[0], rental_record[1], rental_record[2], rental_record[3], rental_record[4], rental_record[5] if rental_record[5] != '' else None))
    
    conn.commit()
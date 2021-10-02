import csv
import os
import sqlite3

curr_dir = os.path.dirname(os.path.abspath(__file__))
db_file = os.path.join(curr_dir, "car_rental.db")

customer_file = os.path.join(curr_dir, "data_files/customers.csv")
car_file = os.path.join(curr_dir, "data_files/cars.csv")
rp_file = os.path.join(curr_dir, "data_files/rental_points.csv")
rr_file = os.path.join(curr_dir, "data_files/rental_records.csv")

files = [customer_file, car_file, rp_file, rr_file]
table_names = ["Customer", "Car", "RentalPoint", "RentalRecord"]
fields = [
    "(?,?,?,?)",
    "(?,?,?,?,?,?)",
    "(?,?,?,?,?)",
    "(?,?,?,?,?,?)",
]


def read_file():
    for i in range(4):
        db = sqlite3.connect(db_file)
        with open(files[i], "r") as f:
            csv_reader = csv.reader(f)
            header = next(csv_reader)

            for row in csv_reader:
                query = "INSERT INTO {} {} VALUES {}"\
                    .format(table_names[i], tuple(header), fields[i])
                db.execute(query, tuple(row))

        db.commit()
        db.close()


read_file()

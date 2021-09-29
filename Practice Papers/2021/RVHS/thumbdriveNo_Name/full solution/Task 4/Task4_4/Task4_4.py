from flask import Flask, render_template, request
import sqlite3
import os

app = Flask(__name__)
curr_dir = os.path.dirname(os.path.abspath(__file__))
db_file = os.path.join(curr_dir, "car_rental.db")
db = sqlite3.connect(db_file)
db.close()


@app.route('/')
def index():
    return render_template('index.html')


def check_vin(vin):
    convert_table = {
        "A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8,
        "J": 1, "K": 2, "L": 3, "M": 4, "N": 5, "P": 7, "R": 9,
        "S": 2, "T": 3, "U": 4, "V": 5, "W": 6, "X": 7, "Y": 8, "Z": 9,
    }
    weight = [8, 7, 6, 5, 4, 3, 2, 10, 0, 9, 8, 7, 6, 5, 4, 3, 2]
    total = 0

    for i in range(len(vin)):

        if vin[i].isdigit():
            # print(vin[i])
            total += int(vin[i]) * weight[i]
        else:
            # print(vin[i], convert_table[vin[i]], weight[i])
            total += convert_table[vin[i]] * weight[i]

    check_digit = total % 11
    print(total, check_digit)
    if check_digit == 10:
        check_digit = "X"
    else:
        check_digit = str(check_digit)

    print(check_digit, vin[8], vin[8] == check_digit)

    return vin[8] == check_digit


@app.route('/new_car/', methods=["GET", "POST"])
def new_car():
    if request.method == "GET":
        return render_template("new_car.html")
    else:
        values = list(request.form.values())
        vin = values[0]
        print(values)
        header = ("VIN", "Brand", "VehicleType",
                  "EnergySource", "DailyPrice", "Availability")

        if check_vin(vin):
            db = sqlite3.connect(db_file)
            try:
                # only for debugging, delete the original record
                # before a new one inserted again
                query = """
                DELETE FROM CAR
                WHERE VIN = ?
                """
                db.execute(query, (vin,))
                db.commit()
            except:
                print("No old record found.")

            query = """
            INSERT INTO Car
            (VIN,Brand,VehicleType,EnergySource,DailyPrice, Availability)
            VALUES
            (?,?,?,?,?,'Available')
            """
            db.execute(query, tuple(values))
            db.commit()

            query = """
            SELECT * FROM CAR
            WHERE VIN = ?
            """
            cursor = db.execute(query, (vin,))
            data = cursor.fetchone()
            db.close()

            print(data)

            return render_template("valid_vin.html", header=header, data=data)
        else:
            return render_template("invalid_vin.html", vin=vin)


if __name__ == '__main__':
    app.run(debug=False)

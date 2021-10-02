from flask import Flask, request, render_template
import sqlite3
app = Flask(__name__)

@app.route('/')
def root():
    energy_sources = [
        ('Diesel', 'diesel'),
        ('Gasoline', 'gas'),
        ('Hybrid', 'hybrid'),
        ('Electricity', 'electric'),
    ]
    v_types = [
        ('Sedan', 'sedan'),
        ('Hatchback', 'h_back'),
        ('SUV', 'suv'),
        ('MPV', 'mpv')
    ]
    return render_template('input.html', energy_sources=energy_sources, v_types=v_types)
def validate_vin(vin):
    translate = {
        'A': 1,
        'B': 2,
        'C': 3,
        'D': 4,
        'E': 5,
        'F': 6,
        'G': 7,
        'H': 8,
        'J': 1,
        'K': 2,
        'L': 3,
        'M': 4,
        'N': 5,
        'P': 7,
        'R': 9,
        'S': 2,
        'T': 3,
        'U': 4,
        'V': 5,
        'W': 6,
        'X': 7,
        'Y': 8,
        'Z': 9
    }
    not_allowed = ['I', 'O', 'Q']
    for char in vin:
        if char in not_allowed:
            return False
    weight = [8,7,6,5,4,3,2,10,0,9,8,7,6,5,4,3,2]
    chars = [None for _ in range(len(vin))]
    for idx, char in enumerate(vin):
        chars[idx] = translate[char] if not char.isdigit() else int(char)
    weighted_vin = [i[0] * i[1] for i in zip(chars, weight)]
    summed_vin = sum(weighted_vin) % 11
    if summed_vin == 10:
        chk_digit = 'X'
    else:
        chk_digit = str(summed_vin)
    
    if vin[8] == chk_digit:
        return True
    else:
        return False

@app.route('/submit', methods=['POST'])
def submit():
    vin = request.form['vin']
    daily_price = request.form['d_price']
    vehicle_type = request.form['v_type']
    energy_source = request.form['energy_source']
    brand = request.form['brand']
    if validate_vin(vin):
        with sqlite3.connect('car_rental.db') as conn:
            cur = conn.cursor()
            cur.execute('INSERT INTO Car(VIN, Brand, VehicleType, EnergySource, DailyPrice, Avaliability) VALUES (?,?,?,?,?,?)',
            (vin, brand, vehicle_type, energy_source,daily_price, 'Available'))
            conn.commit
        return render_template('acknowledge.html', vin=vin, d_price=daily_price, v_type=vehicle_type, energy_source=energy_source, brand=brand)
    else:
        return render_template('invalid.html', vin=vin)



app.run(debug=True)
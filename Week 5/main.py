from flask import Flask
from flask import render_template
from flask import request
import sqlite3

app = Flask(__name__)


@app.route("/")
def root():
    with sqlite3.connect('dental.db') as conn:
        cur = conn.cursor()
        ret = cur.execute('SELECT Name FROM Doctor')
        doctors = list(ret)
    return render_template("appointment_submit.html", doctors=doctors)


@app.route('/submit_appointment', methods=['POST'])
def submit_appointment():
    with sqlite3.connect('dental.db') as conn:
        cur = conn.cursor()
        ret = cur.execute('SELECT * FROM Patient WHERE PatientId = ?', (request.form['id'],))
        if len(list(ret)) == 0:
            return render_template('patient_submit.html')
        else:
            sql = \
                """
                INSERT INTO Appointment(PatientId, DoctorName, Date, Time)
                VALUES(?,?,?,?)
                """
            # If this is a real qn, we need to check if DATE, TIME doesn't clash
            # ASSUME: Date and Time entered by the patient is unique
            cur.execute(sql, (request.form['id'], request.form['doctor'],
                        request.form['date'], request.form['time']))
        conn.commit()
    return render_template('redirect.html', msg=f"INSERT {(request.form['id'], request.form['doctor'], request.form['date'], request.form['time'])}")


@app.route('/submit_details', methods=['POST'])
def submit_details():
    with sqlite3.connect('dental.db') as conn:
        cur = conn.cursor()
        # One to many: Can FK reference a column that is not PK: Column must be UNIQUE and NOT NULL
        # Assuming Patient knows his ID -- like NRIC
        # Alternatively we can assume name is unique in schema but putting the UNIQUE constraint
        # and perform a search to check if patient exists
        sql = \
            """
            INSERT INTO Patient(PatientId, Name, Address, PostalCode, Contact, Allergies)
            VALUES(?,?,?,?,?,?)
            """
        cur.execute(sql, (request.form['id'], request.form['name'], request.form['address'], request.form['postalcode'], request.form['contact'], request.form['allergies']))
        conn.commit()
    return render_template('redirect.html', msg=f"INSERT {(request.form['id'], request.form['name'], request.form['address'], request.form['postalcode'], request.form['contact'], request.form['allergies'])}")


@app.route('/appointment/<date>')
def get_appointment(date):
    with sqlite3.connect('dental.db') as conn:
        cur = conn.cursor()
        sql = \
            """
            SELECT a.Time, p.Name, d.Name FROM Appointment a
            INNER JOIN Patient p ON p.PatientId = a.PatientId
            INNER JOIN Doctor d ON a.DoctorName = d.Name
            WHERE a.Date = ?
            """
        ret = cur.execute(sql, (date,))
        ret = cur.fetchall()
    return render_template('appointment.html', rows=ret, date=date)


@app.route('/doctor/<doctor_name>/<date>')
def get_doctor_date(doctor_name, date):
    with sqlite3.connect('dental.db') as conn:
        cur = conn.cursor()
        sql = \
            """
            SELECT a.Time, p.Name FROM Appointment a
            INNER JOIN Patient p ON p.PatientId = a.PatientId
            INNER JOIN Doctor d ON a.DoctorName = d.Name
            WHERE a.Date = ? AND d.Name = ?
            """
        ret = cur.execute(sql, (date, doctor_name))
        ret = cur.fetchall()
    return render_template('doctor_date.html', rows=ret, doctor=doctor_name, date=date)


app.run(debug=True)

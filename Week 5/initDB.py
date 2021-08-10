import sqlite3
import csv
import os

try:
    os.remove('dental.db')
except:
    pass

patient_sql = \
'''
CREATE TABLE "Patient" (
    "PatientID"	INTEGER,
    "Name"	TEXT,
    "Address"	TEXT,
    "PostalCode"	INTEGER,
    "Contact"	TEXT,
    "Allergies"	TEXT,
    PRIMARY KEY("Name")
);
'''

doctor_sql = \
'''
CREATE TABLE "Doctor" (
    "Name"	TEXT,
    "Contact"	TEXT,
    PRIMARY KEY("Name")
);
'''

appointment_sql = \
'''
CREATE TABLE "Appointment" (
    "PatientId"	TEXT,
    "DoctorName" TEXT,
    "Date" TEXT,
    "Time" TEXT,
    FOREIGN KEY("PatientId") REFERENCES "Patient"("PatientId"),
    FOREIGN KEY("DoctorName") REFERENCES "Doctor"("Name"),
    PRIMARY KEY("PatientId", "DoctorName", "Date")
);
'''

with open('dentists.txt') as f:
    c = csv.reader(f)
    next(c)
    dentists = list(c)


with sqlite3.connect('dental.db') as conn:
    cur = conn.cursor()
    cur.execute(patient_sql)
    cur.execute(doctor_sql)
    cur.execute(appointment_sql)
    conn.commit()

    for dentist in dentists:
        cur.execute('INSERT INTO Doctor(Name, Contact) VALUES(?,?)', (dentist[0], dentist[1]))
    
    conn.commit()
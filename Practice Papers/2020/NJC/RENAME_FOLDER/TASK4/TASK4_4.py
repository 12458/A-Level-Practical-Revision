from flask import Flask, request, render_template

import sqlite3
import datetime

app = Flask(__name__)

@app.route('/<location_id>')
def root(location_id):
    return render_template('checkin.html', location_id=location_id)

@app.route('/submit', methods=['POST'])
def submit():
    with sqlite3.connect('EntryDB.db') as conn:
        cur = conn.cursor()
        sql = \
        """
        INSERT INTO Vistor(NRIC,LocationID,Name,Contact,TimeIn,Date,TimeOut) 
        VALUES (?,?,?,?,?,?,?)
        """
        cur.execute(sql, (request.form['nric'],request.form['location_id'],request.form['name'],request.form['contact'], datetime.datetime.now().strftime('%H%M'), datetime.datetime.now().strftime('%y%m%d'), None))
        conn.commit()
    return f'<p>Please Click on link to check out <a href="/checkout/{request.form["nric"]}/{request.form["location_id"]}">Check Out</a></p>'

@app.route('/checkout/<nric>/<location>')
def checkout(nric, location):
    with sqlite3.connect('EntryDB.db') as conn:
        cur = conn.cursor()
        sql = \
        """
        UPDATE Vistor
        SET TimeOut = ?
        WHERE TimeOut IS NULL AND NRIC = ? AND LocationID = ?
        """
        cur.execute(sql, (datetime.datetime.now().strftime('%H%M'), nric, location))
        conn.commit()
    return f'<p>{nric} Check out at {location}</p>'

app.run(debug=True)
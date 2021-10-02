from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def root():
    return render_template('root.html')

@app.route('/submit', methods=['POST'])
def submit():
    matric_no = request.form['MatricNo']
    with sqlite3.connect('voting_mgm.db') as conn:
        cur = conn.cursor()
        sql = \
            """
            SELECT c.CandidateNo, c.Name FROM Vote v
            INNER JOIN Candidate c ON c.CandidateNo = v.CandidateNo
            WHERE v.MatricNo = ?
            ORDER BY c.CandidateNo ASC
            """
        result = cur.execute(sql, (matric_no,)).fetchall()
        print(result)
    return render_template('return.html', candidates=result)

app.run(debug=True)
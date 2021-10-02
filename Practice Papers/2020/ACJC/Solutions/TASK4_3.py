from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
	return render_template("index.html")
	
@app.route('/results')
def results():
	db = sqlite3.connect('records.db')
	cur = db.cursor()
	status = request.args['status']
	data = cur.execute("SELECT Employee_name from Employee where Service_status = ?", (status,))
	ans = []
	for item in data:
		ans.append(item)
	ans.sort()
	db.close()
	return render_template("results.html", data=ans)
	
app.run(debug=True)
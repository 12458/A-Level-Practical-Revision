import flask, sqlite3

app = flask.Flask(__name__)




@app.route('/') #1m
def index():
    results = []
    db = sqlite3.connect("bank.db") #1m
    db.row_factory = sqlite3.Row
    records = db.execute("SELECT * FROM Customer").fetchall() #1m
    db.close()
    ##sqlite.Row object is immutable, if u need to update it convert it to a dictionary
    ## using dictionary comprehension to convert to a dictionary
    for record in records: #1m
        d = { k: record[k] for k in record.keys() if k != "isPriority"}
        d["Type"]= 'Priority' if record["isPriority"] == 1 else "Customer"
        results.append(d)
        #results.append( (record,priority))
    #print(results)
    return flask.render_template('index.html', results = results,) #1m

if __name__ == '__main__':
    app.run(debug=False)
## html 1m content, 1m structure, 1m format
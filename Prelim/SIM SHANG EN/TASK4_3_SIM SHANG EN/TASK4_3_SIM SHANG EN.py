from flask import Flask, render_template
import csv

app = Flask(__name__)

@app.route('/')
def root():
    # Question does not require us to use SQL to query db
    with open('CUSTOMER.TXT') as f:
        customers = list(csv.reader(f))
    return render_template('customers.html', customers=customers)

app.run(debug=True)
# [8]
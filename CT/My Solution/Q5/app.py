from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/")
def root():
    return render_template("form.html")
    


@app.route("/submit", methods=["POST"])
def form_submit():
    lut_h2 = {'A': 20,
              'B': 17.5,
              'C': 15,
              'D': 12.5,
              'E': 10,
              'S': 5,
              'U': 0
              }
    lut_h1 = {'A': 10,
              'B': 8.75,
              'C': 7.5,
              'D': 6.25,
              'E': 5,
              'S': 2.5,
              'U': 0
              }
    # 10(GP) + 10(PW) + 60(3H2) + 10(1H1) = 90.
    igp = lut_h1[request.form['gp']] + lut_h1[request.form['pw']] + lut_h2[request.form['h2_1']] \
    + lut_h2[request.form['h2_2']] + lut_h2[request.form['h2_3']] + lut_h1[request.form['h1']]
    return render_template("index.html", igp=igp)


app.run(debug=True)  # infinite loop

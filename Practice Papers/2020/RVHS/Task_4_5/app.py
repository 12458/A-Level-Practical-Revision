from flask import Flask, request, render_template, redirect, url_for
import os

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'static/portraits/'

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    candidate_no = request.form['candidate_id']
    print(request.files['image'])
    if 'image' not in request.files:
        print('No Image')
        return 'no image'
    image = request.files['image']
    if image:
        image.save(app.config['UPLOAD_FOLDER']+f'portrait_{candidate_no}.png')
    return 'success'

app.run(debug=True)
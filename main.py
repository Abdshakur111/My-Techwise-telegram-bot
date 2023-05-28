# main.py
import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/registration')
def registration():
    return render_template('registration.html')

@app.route('/countdown')
def countdown():
    return render_template('countdown.html')

@app.route('/issue_reporting')
def issue_reporting():
    return render_template('issue_reporting.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

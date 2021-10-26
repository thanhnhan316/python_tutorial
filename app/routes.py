from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    users = [
        {'id': 'u01','name':'Uyen'},
        {'id': 'u02','name':'Nhat'},
        {'id': 'u03','name':'Nhan'}
        ]
    return render_template('index.html', users=users)

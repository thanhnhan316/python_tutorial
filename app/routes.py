from flask import render_template
import flask
from flask.helpers import flash
from app import app
from app.forms import LoginForm, RegisterForm
from flask import redirect
from app.models import User
from flask_login import login_user
from flask_login import current_user
from app import db

@app.route('/')
@app.route('/index')
def index():
    users = [
        {'id': 'u01','name':'Uyen'},
        {'id': 'u03','name':'Nhan'}
        ]
    return render_template('index.html', users=users)

@app.route('/login', methods=['GET', 'POST'])
def login():
    # nếu user đã login thì redirect đến index
    if current_user.is_authenticated:
        return redirect('/index')
    form = LoginForm()
    # nếu true thì sẽ chuyển hướng người dùng sang một trang khác
    if form.validate_on_submit():
        # Kiem tra user co trong db hay khong
        # Thong tin user lay tu form: form.username.data
        user = User.query.filter_by(username=form.username.data).first()
        # user khong ton tai
        if user is None:
            flash('Invalid username')
            return redirect('/login')
        #kiem tra password
        password = user.password
        if password != form.password.data:
            flash('Invalid password')
            return redirect('/login')


        flash('login of user {}'.format(form.username.data))
        flash('login success')
        # sử dụng flask_login (Login_user)
        login_user(user)

        return redirect('/index')

    return render_template('login.html', form = form )

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        # thông tin user lấy từ form(nếu user == null thì tiến hành register)
        user = User.query.filter_by(username=form.username.data).first()
        if user is not None:
            flash('Username exists')
            return redirect('/register')
        else:
            if form.password.data != form.password1.data:
                flash('wrong password')
                return redirect('/register')
            u1 = User(username=form.username.data,password=form.password.data)
            db.session.add(u1)
            db.session.commit()
            flash('Sign Up Success')
            flash(f'username : {form.username.data}')
            return redirect('/index')


    return render_template('register.html', form = form )

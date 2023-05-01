from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user
from werkzeug.urls import url_parse

from app.auth import bp
from app.auth.forms import LoginForm, SignUpForm
from app.models import User
from app import database as db


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    
    form = LoginForm()
    
    if form.validate_on_submit():
     
        user = User.query.filter_by(username=form.username.data).first()
        
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('auth.login'))
                            
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get("next")
        
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('main.home')
        return redirect(next_page)
    
    return render_template('login.html', title="Sign In", form=form)


@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.home'))


@bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    
    form = SignUpForm()
    
    if form.validate_on_submit():
        username = User.query.filter_by(username=form.username.data).first()
        email = User.query.filter_by(email=form.email.data).first()
        
        try:
            if username :
                raise Exception('Username already exists, please chose another username')
            elif email :
                raise Exception('A user with that email already exists')
            else :
                user = User(username=form.username.data, email=form.email.data)
                user.set_password(form.password.data)
                db.session.add(user)
                db.session.commit()
                flash('Congratualtions, you are now a registered user')
                return redirect(url_for('auth.login'))
        except Exception as e:
            flash(str(e))
            return render_template('signup.html', title="Sign up", form=form)

    return render_template('signup.html', title="Sign up", form=form)

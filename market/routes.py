from market import app, db
from flask import render_template, redirect, url_for
from market.models import Item, User
from market.forms import RegisterForm


@app.route('/')
def home():
    return render_template('./home.html')


@app.route('/about')
def about_page():
    return 'Hey, it\'s about page!'


@app.route('/about/<user>')
def about_user(user):
    return f'Hey, it\'s about <b>{user}</b> page!'


@app.route('/market')
def market():
    items = Item.query.all()
    return render_template('market.html', items=items)


@app.route('/register', methods=['get', 'post'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        create_user = User(username=form.username.data,
                           email_address=form.email_address.data,
                           password_hash=form.password1.data)
        db.session.add(create_user)
        db.session.commit()
        return redirect(url_for('market'))
    if form.errors != {}:
        for err_msg in form.errors.values():
            print('!', err_msg)
    return render_template('register.html', form=form)

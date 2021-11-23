from market import app
from flask import render_template
from market.models import Item


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

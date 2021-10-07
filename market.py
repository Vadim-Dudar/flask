from flask import Flask, render_template

app = Flask(__name__)



@app.route('/')
def home_page():
    return render_template('home.html')

@app.route('/about')
def about_page():
    return 'Hey, it\'s about page!'

@app.route('/about/<user>')
def about_user(user):
    return f'Hey, it\'s about <b>{user}</b> page!'

@app.route('/market')
def market():
    items = [
        {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500},
        {'id': 2, 'name': 'Laptop', 'barcode': '123985473165', 'price': 900},
        {'id': 3, 'name': 'Keyboard', 'barcode': '231985128446', 'price': 150}
    ]
    return render_template('market.html', items=items)
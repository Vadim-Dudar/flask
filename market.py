from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World</p>"

@app.route('/about')
def about_page():
    return 'Hey, it\'s about page!'
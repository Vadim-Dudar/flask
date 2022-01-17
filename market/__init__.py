# source venv/bin/activate
# export FLASK_APP=market.py
# export FLASK_DEBUG=True
# flask run


from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = '6207f8257d6110f6fbd5d689'
db = SQLAlchemy(app)


from market import routes

from flask import Flask

import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.db')
app.config["SQLALCHAMY_TRACK_MODIFICATIONS"] = False

app.config['SECRET_KEY'] = "you will never guess"


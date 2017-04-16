# all the imports
import os
from flask import Flask, request, session, g, redirect, url_for, \
     render_template, flash
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
db = SQLAlchemy(app)

app.config.from_object(__name__)  # load config from this file , flaskr.py

# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'nolikes.db'),
    SQLALCHEMY_DATABASE_URI='sqlite:////tmp/test.db',
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))
app.config.from_envvar('NOLIKES_SETTINGS', silent=True)


class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(80), unique=True)
    url = db.Column(db.String(120), unique=True)
    caption = db.Column(db.String(480))

    def __init__(self, uuid, url, caption):
        self.uuid = uuid
        self.url = url
        self.caption = caption

    def __repr__(self):
        return '<Image %r>' % self.uuid
# @app.route('/')
# def show_image():
    # db = get_db()
    # cur = db.execute('select title, text from entries order by id desc')
    # entries = cur.fetchall()
    # return render_template('show_entries.html', entries=entries)

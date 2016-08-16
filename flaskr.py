from __future__ import with_statement
import sqlite3

from contextlib import closing
from flask import Flask, request, session, g, redirect, url_for, \
 abort, render_template, flash

app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('FLASKR_SETTINGS', silent=True)


DATABASE = '/tmp/flaskr.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

def connect_db():
    rv =  sqlite3.connect(DATABASE)
    rv.row_factory = sqlite3.Row    
    return rv
def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()
@app.before_request
def before_request():
    g.db = connect_db()
@app.teardown_request
def teardown_request(exception):
    g.db.close()

if __name__ == '__main__':
    app.run()

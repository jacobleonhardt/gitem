from flask import Flask
from flask_github import GitHub
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


@app.route('/')
def greeting():
    return '<h1>Hello</h1>'

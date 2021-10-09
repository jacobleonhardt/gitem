from flask import Flask
from flask_github import GitHub
from flask_sqlalchemy import SQLAlchemy
from .config import Config

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/')
def greeting():
    return '<h1>Hello</h1>'

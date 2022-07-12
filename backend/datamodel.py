from dataclasses import dataclass
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data/main.sqlite3'
db = SQLAlchemy(app)


@dataclass
class User(db.Model):
    id: int
    name: str

    id = db.Column(db.Integer, primary_key=True, auto_increment=True)
    name = db.Column(db.String(200), unique=True)


@dataclass
class Post(db.Model):
    id: int
    user_id: int
    content: str

    id = db.Column(db.Integer, primary_key=True, auto_increment=True)
    user_id = db.Column(db.Integer, ForeignKey("user.id"))
    content = db.Column(db.String(200), unique=True)

    def __repr__(self) -> str:
        return f"Post #{self.id} from user {self.user_id}"

from dataclasses import dataclass
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data/main.sqlite3'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@database/postgres'
db = SQLAlchemy(app)


@dataclass
class User(db.Model):
    id: int = db.Column(db.Integer, primary_key=True, auto_increment=True)
    name: str = db.Column(db.String(200), unique=True)


@dataclass
class Post(db.Model):
    id: int = db.Column(db.Integer, primary_key=True, auto_increment=True)
    user_id: int = db.Column(db.Integer, ForeignKey("user.id"))
    content: str = db.Column(db.String(200), unique=True)

    def __repr__(self) -> str:
        return f"Post #{self.id} from user {self.user_id}"

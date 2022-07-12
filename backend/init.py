from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, ForeignKey, Integer, Table

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////app/data/main.sqlite3'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(160), unique=True, nullable=False)
    surname = db.Column(db.String(160), unique=True, nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = Column(db.Integer)
    content = db.Column(db.String(200), nullable=False)

    def __repr__(self) -> str:
        return f"Post #{self.id} from user {self.user_id}"


# create schema
db.create_all()

# insert data
user1 = User(username="johnd", name="John", surname="Doe")

# add user to register id needed for the posts
# Otherwise, user1 is transient
db.session.add(user1)
db.session.commit()

posts = [
    Post(user_id=user1.id, content="Hello world"),
    Post(user_id=user1.id, content="Hello python"),
    Post(user_id=user1.id, content="Hello flask")
]
db.session.add_all(posts)
db.session.commit()

# update a post
post = db.session.query(Post).filter(Post.user_id == user1.id).first()
post.content = "Hello, world!"
db.session.commit()

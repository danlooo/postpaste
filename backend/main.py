from datamodel import *
from flask import jsonify


@app.route('/posts')
def posts():
    posts = db.session.query(Post).all()
    return jsonify(posts)


@app.route('/users')
def users():
    users = db.session.query(User).all()
    return jsonify(users)


@app.route('/')
def main():
    return {
        "message": "PostPaste backend entry point",
        "links": {
            "posts": "/posts",
            "users": "/users"
        }
    }


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

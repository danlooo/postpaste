from datamodel import *

# create schema
db.create_all()

# insert data
user1 = User(name="john")

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

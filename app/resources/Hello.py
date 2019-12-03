from flask_restful import Resource
from app.database.models import User
from app.database.model_post import Post


class Hello(Resource):

    def get(self):
        john = User(name="abc1234dacxa")
        john.save()

        post = Post(post_string="a12dbc")
        post.save()

        return {"hello": "world"}

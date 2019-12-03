from mongoengine import *


class Post(Document):
    post_string = StringField()
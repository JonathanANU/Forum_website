import datetime
from peewee import *
from Forum1040.data.configuration import database_path


db = SqliteDatabase(database_path)


class User(Model):
    id = PrimaryKeyField()
    username = CharField(unique=True)
    password = CharField()

    class Meta:
        database = db


class Notice(Model):
    id = PrimaryKeyField()
    date = DateTimeField(
        default="{:%Y-%m-%d %H:%M}".format(datetime.datetime.now()))
    title = CharField()
    text = TextField()

    class Meta:
        database = db


class Post(Model):
    id = PrimaryKeyField()
    username = CharField()
    date = DateTimeField(
        default="{:%Y-%m-%d %H:%M}".format(datetime.datetime.now()))
    title = CharField()
    text = TextField()
    about = CharField()
    topic = CharField()

    class Meta:
        database = db
        constraints = [SQL('FOREIGN KEY(username) REFERENCES user(username)')]


class Comment(Model):
    id = PrimaryKeyField()
    date = DateTimeField(
        default="{:%Y-%m-%d %H:%M}".format(datetime.datetime.now()))
    post_id = IntegerField()
    username = CharField()
    text = TextField()

    class Meta:
        database = db
        constraints = [SQL('FOREIGN KEY(post_id) REFERENCES post(id)')]


class Admin(Model):
    id = PrimaryKeyField()
    username = CharField(unique=True)
    password = CharField()

    class Meta:
        database = db


def initialize_db():
    db.connect()
    db.create_tables([User, Notice, Post, Comment, Admin], safe=True)

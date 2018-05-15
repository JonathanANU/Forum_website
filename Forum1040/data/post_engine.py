import radar
from random import randint
from Forum1040.data.models import *

initialize_db()

ABOUT = ["Assignment", "Weekly exercise"]
TOPIC = ["String", "Dictionary", "List", "Function", "Module", "Class"]

count = 0
with open("demo_post.txt", "r") as posts:
    for post in posts:
        post = post.strip()
        username = 'u' + str(randint(1000, 1099))
        random_time = "{:%Y-%m-%d %H:%M}".format(radar.random_datetime(
            start=datetime.datetime(year=2016, month=7, day=1),
            stop=datetime.datetime(year=2016, month=7, day=10)))
        if post is '':
            continue
        else:
            Post.create(
                date=random_time,
                username=username,
                about=ABOUT[randint(0, 1)],
                topic=TOPIC[randint(0, 5)],
                title="Why random title when we all have a dream",
                text=post
            )
            count += 1

with open("demo_comment.txt", "r") as comments:
    for comment in comments:
        comment = comment.strip()
        username = 'u' + str(randint(1000, 1099))
        random_time = "{:%Y-%m-%d %H:%M}".format(radar.random_datetime(
            start=datetime.datetime(year=2016, month=7, day=11),
            stop=datetime.datetime(year=2016, month=7, day=20)))
        if comment is '':
            continue
        else:
            Comment.create(
                date=random_time,
                post_id=randint(1, count),
                username=username,
                text=comment
            )

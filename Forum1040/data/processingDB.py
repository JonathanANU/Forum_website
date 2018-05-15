import matplotlib.pyplot as plt
import peewee
from Forum1040.data.models import *


initialize_db()


def topic_count():
    """This function returns two list, one for topics, one for the total number of each topic"""
    # get the number topics and their counts as tuples: ('Topic', 123)
    query = peewee.RawQuery(Post, "select topic, count(topic) from post group by topic").tuples()

    # turn the result of the query object into a list of tuples
    tuple_result = []
    for each_tuple in query:
        tuple_result.append(each_tuple)

    # sort by the the second element, which is value, of each tuple in the list
    tuple_result = sorted(tuple_result, key=lambda x: x[1], reverse=True)

    # separate the topic and count into two lists for graphing purpose
    topics = []
    counts = []

    for each_tuple in tuple_result:
        topics.append(each_tuple[0])
        counts.append(each_tuple[1])

    return counts, topics


def no_reply():
    """This function returns the IDs of posts with no reply"""
    post_id_with_reply = []
    for i in Post.select().join(Comment, on=(Post.id == Comment.post_id)):
        post_id_with_reply.append(i.id)
        sorted(set(post_id_with_reply))

    post_id = []
    for i in Post.select():
        post_id.append(i.id)

    # utilize the difference operation on sets to find out posts without reply
    post_id_without_reply = list(set(post_id) - set(post_id_with_reply))
    return post_id_without_reply


def average_num_reply():
    """this function returns the average number of replies per post """
    post_count = Post.select().count()
    reply_count = Comment.select().count()
    if post_count == 0:
        return 0
    else:
        average = round(reply_count / post_count, 2)
    return average


def sql(query):
    """This function takes query and return a dictionary from a list of tuples"""
    cursor = db.execute_sql(query)
    list_of_tuples = cursor.fetchall()
    lis = [i[0] for i in list_of_tuples]
    dictionary = {element: lis.count(element) for element in lis}
    return dictionary


def count(query):
    """This function is only used to count the total number of tuple in one attribute"""
    cursor = db.execute_sql(query)
    result = cursor.fetchone()[0]
    return result


def avg_time_to_reply():
    """return the average time for a post to be replied in hours"""
    date_from_post = []
    for record in Post.select().join(Comment, on=(Post.id == Comment.post_id)):
        # record.date refers to the date of each post
        date_from_post.append(record.date)

    date_from_comment = []
    for record in Comment.select().join(Post, on=(Post.id == Comment.post_id)):
        # record.date refers to the date of each comment
        date_from_comment.append(record.date)

    hr = []
    for x, y in zip(date_from_comment, date_from_post):
        time1 = datetime.datetime.strptime(x, "%Y-%m-%d %H:%M")
        time2 = datetime.datetime.strptime(y, "%Y-%m-%d %H:%M")
        d = time1 - time2
        days_in_hours = d.days * 24
        sec_in_hour = d.seconds / 3600
        hr.append(days_in_hours + sec_in_hour)
    if len(hr) == 0:
        return 0
    else:
        avg_time = round(sum(hr)/(len(hr)), 2)
    return avg_time


def topic_graph():
    counts, topics = topic_count()
    plt.bar(range(len(counts)), counts, align='center')
    plt.xticks(range(len(topics)), topics)
    plt.title("Topic Frequency")
    plt.xlabel('Topics')
    plt.ylabel('Frequency')


def category_graph():
    b = sql('select about from post;')
    plt.bar(range(len(b)), b.values(), width=1/2, align='center')
    plt.xticks(range(len(b)), b.keys())
    plt.title('Category Frequency')
    plt.xlabel('Category')
    plt.ylabel('Frequency')


def general_graph():
    result_tuple = [('Avg Replies', average_num_reply()),
                    ('Post without replies', len(no_reply()))]

    plt.title("Reply Statistics")
    result_tuple.sort(key=lambda x: x[1], reverse=True)

    names = []
    values = []
    for each_tuple in result_tuple:
        names.append(each_tuple[0])
        values.append(each_tuple[1])

    plt.bar(range(len(values)), values, width=1/2, align='center')
    plt.xticks(range(len(names)), names)


def graph():
    plt.plot()
    topic_graph()
    plt.savefig("static/images/topic.png")
    plt.close()

    plt.plot()
    category_graph()
    plt.savefig("static/images/category.png")
    plt.close()

    plt.plot()
    general_graph()
    plt.savefig("static/images/reply.png")
    plt.close()

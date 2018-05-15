from flask import Flask, render_template, request, redirect, url_for, \
    session, flash
from functools import wraps
import sqlite3
from Forum1040.data.processingDB import *
from Forum1040.data import configuration

app = Flask(__name__)
# a secret key is used for using "session"
app.secret_key = '\x08v\xf2>,\x0c\x05F/\xc4\xc9\x16\xa10xz\x16,85\x0f\x83%\xbe'


class AdminQuery(object):
    """This class is used to hold strings globally"""
    def __init__(self):
        self.string = ''


class UserQuery(object):
    def __init__(self):
        self.string = None


# an instance of the AdminQuery class to hold query string from admin users
admin_query = AdminQuery()

# an instance of the UserQuery class to hold the selection string from user
# this will be used for displaying topics according to user's click in forum()
user_query = UserQuery()


# prepares the database before request
@app.before_request
def before_request():
    initialize_db()

# ----------------------------------------------------------------------------
# functions related to ordinary users


def login_required(f):
    """This function decorator makes sure that only logged in users can
    visit the content of the forum"""
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            return redirect(url_for('login'))
    return wrap


@app.route('/login', methods=['GET', 'POST'])
def login():
    """The login function checks the login information for users"""
    error = None
    if request.method == 'POST':
        try:
            password = User.get(
                User.username == request.form['username']).password

            if password == request.form['password']:
                session['logged_in'] = True
                session['username'] = request.form['username']
                return redirect(url_for('home'))
            else:
                error = ' Invalid password. Please try again.'

        except DoesNotExist:
            error = 'User does not exist, please register.'

    return render_template('login.html', error=error)


@app.route('/change_password', methods=['GET', 'POST'])
def change_password():
    """This function lets users change their passwords"""
    error = None
    if request.method == 'POST':
        try:
            password = User.get(
                User.username == request.form['username']).password

            if password == request.form['password'] \
                    and request.form['new_pass'] == request.form['new_pass_confirm']:
                q = User.update(password=request.form['new_pass']).where(
                    User.username == request.form['username']
                )
                q.execute()
                return redirect(url_for('login'))
            else:
                error = 'Make sure you input things right : )'

        except DoesNotExist:
            error = 'User does not exist, please register.'

    return render_template("change_password.html", error=error)


@app.route('/')
@login_required
def home():
    return render_template("index.html",
                           notices=Notice.select().order_by(Notice.date.desc()),
                           num=0)


# We want to pass Comment to the forum.html as a relation object
# rather than a variable
# to do that, we need to use context_processor of flask
@app.context_processor
def comment_class():
    return {'Comment': Comment}


@app.route('/forum/')
@login_required
def forum():
    """This function is the core part of the system.
    This function passes posts, comments, and counts associated with each
    topic."""
    counts, topics = topic_count()

    if user_query.string == 'All' or user_query.string is None:
        posts = Post.select().order_by(Post.date.desc())
    else:
        posts = Post.select().where(Post.topic == user_query.string)

    return render_template("forum.html", posts=posts,
                           Comment=Comment,
                           counts=counts, topics=topics,
                           num=0)


@app.route('/select', methods=['GET', 'POST'])
@login_required
def select():
    """Takes the value of selection from forum.html and store it in
    user_query.string in order to be used in forum.html to display
    the posts accordingly"""
    user_query.string = request.form['topic']
    return redirect(url_for('forum'))


@app.route('/post/')
@login_required
def post():
    return render_template('post.html')


@app.route('/create-post', methods=['GET', 'POST'])
@login_required
def create_post():
    Post.create(
        username=session['username'],
        title=request.form['title'],
        text=request.form['text'],
        about=request.form['about'],
        topic=request.form['topic']
    )

    return redirect(url_for('forum'))


@app.route('/create-comment', methods=['GET', 'POST'])
@login_required
def create_comment():
    Comment.create(
        post_id=request.form['post_id'],
        text=request.form['comment_text'],
        username=session['username']
    )
    return redirect(url_for('forum'))


@app.route('/logout/')
@login_required
def logout():
    session.pop('logged_in', None)
    flash("You were just logged out!")
    return redirect(url_for('home'))


# ----------------------------------------------------------------------------
# functions related to admin users


def admin_login_required(f):
    """This function decorator makes ure that only logged in admin user
    can have access to the admin pages of the forum"""
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'admin_logged_in' in session:
            return f(*args, **kwargs)
        else:
            return redirect(url_for('admin_login'))
    return wrap


@app.route('/login-admin', methods=['GET', 'POST'])
def admin_login():
    """This admin_login function checks the login information for
    admin users"""
    error = None
    if request.method == 'POST':
        try:
            password = Admin.get(
                Admin.username == request.form['username']).password

            if password == request.form['password']:
                session['admin_logged_in'] = True
                session['admin_username'] = request.form['username']
                return redirect(url_for('admin'))
            else:
                error = ' Invalid password. Please try again.'
        except DoesNotExist:
            error = 'User does not exist, please register.'

    return render_template('admin_login.html', error=error)


@app.route('/admin/')
@admin_login_required
def admin():
    """This is the home function for admin users, it calls functions imported
    from processingDB.py to get statistics and display them in admin.html"""
    graph()
    avg_time = avg_time_to_reply()
    no_reply_posts = sorted(no_reply())
    notice_count = count('select count(id) from notice;')
    total_user = count('select count(id) from user;')
    message = "Welcome back, {}!".format(session['admin_username'])
    return render_template('admin.html', message=message,
                           avg_time=avg_time, total_user=total_user,
                           no_reply_posts=no_reply_posts,
                           notice_count=notice_count)


@app.route('/admin/notice/')
@admin_login_required
def notice():
    """From notice.html, admin user can submit a form which creates
    a new notice"""
    return render_template('notice.html')


@app.route('/add-notice', methods=['GET', 'POST'])
@admin_login_required
def add_notice():
    """Takes the input from users and create a new tuple in the
    Notice relation"""
    Notice.create(
        title=request.form['title'],
        text=request.form['text'],
    )
    return redirect(url_for('notice'))


@app.route('/admin/query/')
@admin_login_required
def query():
    """Use the string stored in the admin_query instance as the content of the
    query to fetch the corresponding result and display it query.html"""
    conn = sqlite3.connect(configuration.database_path)
    cur = conn.cursor()
    query_result = False
    error = False
    if admin_query.string != 'Clearing...':
        try:
            cur.execute('{}'.format(admin_query.string))
            query_result = cur.fetchall()
            conn.close()
        except sqlite3.Error:
            error = True

    return render_template("query.html", query_result=query_result, error=error)


@app.route('/delete-query', methods=['GET', 'POST'])
@admin_login_required
def delete():
    conn = sqlite3.connect(database_path)
    cur = conn.cursor()
    table = request.form['table']
    id = request.form['id']
    cur.execute('DELETE FROM {tb} where id={id}'.
                format(tb=table,id=id))
    conn.commit()
    conn.close()
    return redirect(url_for('query'))


@app.route('/get-query', methods=['GET', 'POST'])
@admin_login_required
def get_query():
    """This function takes the user input from the form sent from query.html
    User's input is then stored in admin_query.string"""
    admin_query.string = request.form['query']
    return redirect(url_for('query'))


@app.route('/admin/logout/')
@admin_login_required
def admin_logout():
    session.pop('admin_logged_in', None)
    flash("Admin user logged out!")
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)

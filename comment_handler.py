from flask import Blueprint, render_template, redirect, url_for, request

comment_handler_blueprint = Blueprint('comment_handler', __name__)


@comment_handler_blueprint.route('/')
def index():
    return render_template('index.html')


@comment_handler_blueprint.route('/comments')
def comment():
    comments = ""
    try:
        f = open('comments.txt', 'r')
        f.seek(0)
        comments = f.readlines()
        f.close()
    except:
        f = open('comments.txt', 'x')
        f.close()

    return render_template('comments.html', comments=comments)


@comment_handler_blueprint.route('/comments', methods=['POST'])
def comment_post():
    comment = "\n" + request.form.get('txt')

    f = open('comments.txt', 'a')
    f.writelines(comment)
    f.close()

    return redirect(url_for('comment_handler.comment'))

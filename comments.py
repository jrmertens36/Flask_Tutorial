from flask import Blueprint, render_template, current_app, redirect, url_for,request

comments = Blueprint('comments', __name__)

@comments.route('/comments')
def comment():
    f = open('comments.txt', 'r')
    comments = f.readlines()
    f.close()

    return render_template('comments.html', comments=comments)

@comments.route('/comments', methods=['POST'])
def comment_post():
    comment = "\n" + request.form.get('txt')

    f = open('comments.txt', 'a')
    f.writelines(comment)
    f.close()

    return redirect(url_for('comments.comment'))
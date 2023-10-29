import json
from datetime import datetime

from flask import Blueprint, render_template, redirect, url_for, request, current_app

comment_handler_blueprint = Blueprint('comment_handler', __name__)


@comment_handler_blueprint.route('/')
def index():
    return render_template('index.html')


@comment_handler_blueprint.route('/comments')
def comment():
    comments = ""
    try:
        f = open(current_app.config.get('CFILE'), 'r')
        f.seek(0)
        comments = json.load(f)
        f.close()
    except:
        # f = open(current_app.config.get('CFILE'), 'x')
        #f.close()
        pass

    return render_template('comments.html', comments=comments)


@comment_handler_blueprint.route('/comments', methods=['POST'])
def comment_post():

    existing_comments = []
    try:
        with open(current_app.config.get('CFILE'), "r") as json_file:
            existing_comments = json.load(json_file)
    except:
        pass

    text = request.form.get('txt')
    new_comment = {
        "timestamp": str(datetime.now().strftime("%d.%m.%Y %H:%M")),
        "comment": text
    }
    existing_comments.append(new_comment)

    json_data = json.dumps(existing_comments, indent=4)

    with open(current_app.config.get('CFILE'), "w") as json_file:
        json_file.write(json_data)

    return redirect(url_for('comment_handler.comment'))

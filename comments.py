from flask import Blueprint, render_template, current_app, redirect, url_for,request

comments = Blueprint('comments', __name__)

@comments.route('/comments')
def comment():

    comments=""
    try:
        f = open('comments.txt', 'r')
        f.seek(0)
        comments = f.readlines()
        f.close()
    except:
        f = open('comments.txt', 'x')
        f.close()

    return render_template('comments.html', comments=comments)

@comments.route('/comments', methods=['POST'])
def comment_post():
    comment = "\n" + request.form.get('txt')

    f = open('comments.txt', 'a')
    f.writelines(comment)
    f.close()

    return redirect(url_for('comments.comment'))

@comments.route('/insecure')
def insecure():

    comments=""
    try:
        f = open('comments.txt', 'r')
        f.seek(0)
        comments = f.readlines()
        f.close()
    except:
        f = open('comments.txt', 'x')
        f.close()


    document = """<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>HSS Flask Tutorial</title>
    <link rel="stylesheet" href="static/css/commments.css" >
</head>

<body>
        <header class="header">
            <img src="static/HSS Logo.png" class="logo" height='50px' >
        </header>

        <div class="hss-body">
            <div class="container has-text-centered">"""

    for c in comments:
        document = document +"<br>" + c

    document = document + " </div>  </div> </body>"

    return document
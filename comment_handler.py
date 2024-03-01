import sqlite3

from flask import Blueprint, render_template, redirect, url_for, request

comments_blueprint = Blueprint('comments', __name__)


@comments_blueprint.route('/login')
def login():
    return render_template('login.html')


@comments_blueprint.route('/login', methods=["POST"])
def login_post():
    username = request.form.get('username')
    password = request.form.get('password')

    conn = sqlite3.connect('benutzerdatenbank.db')
    cursor = conn.cursor()

    sql = f"SELECT * FROM user WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(sql)

    # Ergebnis abrufen
    ergebnis = cursor.fetchone()

    # Überprüfen, ob ein Benutzer mit den angegebenen Daten gefunden wurde
    if ergebnis:
        msg = f"Hallo {ergebnis[3]}!"
    else:
        msg = "Falscher Benutzername oder falsches Passwort."

    # Verbindung schließen
    conn.close()

    return render_template('login.html', success=msg)


@comments_blueprint.route('/')
def index():
    return render_template('index.html')


@comments_blueprint.route('/comments')
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


@comments_blueprint.route('/comments', methods=['POST'])
def comment_post():
    comments = "\n" + request.form.get('txt')

    f = open('comments.txt', 'a')
    f.writelines(comments)
    f.close()

    return redirect(url_for('comments.comment'))


@comments_blueprint.route('/insecure')
def insecure():
    comments = ""
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
        document = document + "<br>" + c

    document = document + " </div>  </div> </body>"

    return document

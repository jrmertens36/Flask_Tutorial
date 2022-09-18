from flask import Blueprint, render_template
from __init__ import create_app

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

create_app().run()
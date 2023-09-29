from flask import Flask

from comment_handler import comment_handler_blueprint

app = Flask(__name__)

app.config['SECRET_KEY'] = 'xcde234'
app.config['HOST'] = '127.0.0.1'
app.config['DEBUG'] = False
app.config['PORT'] = 5000

app.config.from_pyfile('config.py', silent=True)

app.register_blueprint(comment_handler_blueprint)

if __name__ == '__main__':
    app.run(host=app.config.get('HOST'), debug=app.config.get('DEBUG'))

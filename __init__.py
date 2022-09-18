from flask import Flask


def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'xcde234'

    from main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from comments import comments as comments_blueprint
    app.register_blueprint(comments_blueprint)

    return app

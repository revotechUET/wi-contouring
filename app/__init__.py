from flask import Flask
from flask import request
from flask import jsonify
from .kriging import kriging_fill_grid


def create_app(config_name='production'):
    app = Flask(__name__, instance_relative_config=True)

    @app.route("/")
    def hello():
        return "<h1 style='color:blue'>Hello There!</h1>"

    @app.route("/kriging", methods=['POST'])
    def kriging():
        z = kriging_fill_grid(request.json) 
        return str(z)

    return app

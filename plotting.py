from flask import Blueprint, render_template

plotting_blueprint = Blueprint('plotting', __name__)


@plotting_blueprint.route('/')
def index():
    return render_template('index.html', x_window=100)

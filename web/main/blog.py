from flask import Blueprint, render_template

blog = Blueprint("blog", __name__, template_folder='./templates', static_folder='./static')


@blog.route('/')
def index():
    return render_template('index.html')

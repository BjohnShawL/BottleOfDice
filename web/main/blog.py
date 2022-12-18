from flask import Blueprint, render_template, current_app

blog = Blueprint("blog", __name__, template_folder='./templates', static_folder='./static')


@blog.route('/')
def index():
    return render_template('index.html')


@blog.route('/status')
def status():
    if current_app.config.get('DISCORD_PUBLIC_KEY'):
        p_key = current_app.config.get('DISCORD_PUBLIC_KEY')
    else:
        p_key = "No Discord Key Available"
    c = {"discord_public_key": p_key}
    return render_template('status.html.j2', config=c)

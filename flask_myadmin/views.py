from flask import Blueprint
from flask import render_template
from flask import current_app


blueprint = Blueprint(
    'flask_myadmin', 
    __name__, 
    template_folder="templates", 
    static_folder="static", 
    url_prefix="/flask-myadmin"
)

@blueprint.route('')
def index():
    host = current_app.config.get('FLASK_MYADMIN_HOST', 'localhost')
    return render_template('flask_myadmin/index.html', host=host)
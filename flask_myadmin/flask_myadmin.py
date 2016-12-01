from .views import blueprint

class FlaskMyAdmin(object):
    
    def __init__(self, app=None, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)
        if app is not None:
            self.init_app(app)
    
    def init_app(app=None):
        host = getattr(self, 'host', 'localhost')
        app.config['FLASK_MYADMIN_HOST'] = host
        app.register_blueprint(blueprint)
        
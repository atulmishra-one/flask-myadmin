from .views import blueprint

class FlaskMyAdmin(object):
    
    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)
    
    def init_app(self, app=None):
        app.register_blueprint(blueprint)
        
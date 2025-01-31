if __name__ == '__main__':
    from gunicorn.app.base import BaseApplication
    from gunicorn.six import iteritems

    class GunicornApplication(BaseApplication):
        def __init__(self, app, options=None):
            self.options = options or {}
            self.application = app
            super(GunicornApplication, self).__init__()

        def load_config(self):
            config = self.config
            for key, value in iteritems(self.options):
                config.set(key, value)

        def load(self):
            return self.application

    options = {
        'bind': '0.0.0.0:5000',  # écoute sur tous les ports disponibles
        'workers': 4,             # nombre de workers pour gérer les requêtes
    }

    GunicornApplication(app, options).run()


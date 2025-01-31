if __name__ == '__main__':
    from gunicorn.app.base import BaseApplication
    # Supprimez l'importation de gunicorn.six

    class GunicornApplication(BaseApplication):
        def __init__(self, app, options=None):
            self.options = options or {}
            self.application = app
            super(GunicornApplication, self).__init__()

        def load_config(self):
            config = self.cfg  # Notez que c'est 'cfg' et non 'config'
            for key, value in self.options.items():  # Utilisez items() au lieu de iteritems()
                if key in config.settings and value is not None:
                    config.set(key, value)

        def load(self):
            return self.application

    options = {
        'bind': '0.0.0.0:5000',  # écoute sur tous les ports disponibles
        'workers': 4,             # nombre de workers pour gérer les requêtes
    }

    # Ici, vous devriez instancier votre application Flask (ou autre) et la passer à GunicornApplication
    # Exemple :
    # from myapp import app  # Assurez-vous d'importer votre application ici
    # GunicornApplication(app, options).run()

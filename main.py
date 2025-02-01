from generate_audio import app
from gunicorn.app.base import BaseApplication

class GunicornApplication(BaseApplication):
    def __init__(self, app, options=None):
        self.options = options or {}
        self.application = app
        super(GunicornApplication, self).__init__()

    def load_config(self):
        config = self.cfg
        for key, value in self.options.items():
            if key in config.settings and value is not None:
                config.set(key, value)

    def load(self):
        return self.application

if __name__ == '__main__':
    options = {
        'bind': '0.0.0.0:5000',  # écoute sur tous les ports disponibles
        'workers': 1,             # Utilisez un seul worker pour éviter les doublons
    }
    
    # Instanciez et exécutez GunicornApplication avec votre application Flask
    GunicornApplication(app, options).run()

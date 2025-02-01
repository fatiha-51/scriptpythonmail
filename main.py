import os
import sys

# Ajoutez le répertoire racine du projet au PYTHONPATH (si nécessaire)
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from generate_audio import app  # Assurez-vous que generate_audio.py est dans le même répertoire
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
    # Récupérez le port depuis la variable d'environnement (Render utilise $PORT)
    port = int(os.environ.get("PORT", 5000))

    options = {
        'bind': f"0.0.0.0:{port}",  # Utilisez le port fourni par Render
        'workers': 1,               # Utilisez un seul worker pour éviter les doublons
    }

    # Instanciez et exécutez GunicornApplication avec votre application Flask
    GunicornApplication(app, options).run()

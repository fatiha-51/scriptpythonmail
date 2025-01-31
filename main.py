from flask import Flask, request, jsonify
from gtts import gTTS
import os
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

app = Flask(__name__)

@app.route('/generate-audio', methods=['POST'])
def generate_audio():
    try:
        # Récupérer les données envoyées par n8n
        data = request.json
        nom = data.get('nom', 'Expéditeur inconnu')
        sujet = data.get('sujet', 'Sans sujet')
        contenu = data.get('contenu', 'Aucun message')
        # Construire le message audio
        texte_email = f"Vous avez reçu un mail de {nom}. Sujet : {sujet}. Voici le message : {contenu}."
        # Convertir le texte en audio
        tts = gTTS(texte_email, lang='fr')
        audio_filename = "email_audio.mp3"
        tts.save(audio_filename)
        return jsonify({"message": "✅ Audio généré avec succès", "filename": audio_filename})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    options = {
        'bind': '0.0.0.0:5000',  # écoute sur tous les ports disponibles
        'workers': 4,             # nombre de workers pour gérer les requêtes
    }
    
    # Instanciez et exécutez GunicornApplication avec votre application Flask
    GunicornApplication(app, options).run()

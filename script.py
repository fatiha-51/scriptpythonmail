from flask import Flask, request, jsonify
from gtts import gTTS
import os

app = Flask(__name__)

@app.route('/generate-audio', methods=['POST'])
def generate_audio():
    data = request.get_json()  # Récupère le JSON envoyé dans le body
    nom = data.get('nom')
    sujet = data.get('sujet')
    contenu = data.get('contenu')

    # Exemple pour générer l'audio avec gTTS
    message = f"Vous avez reçu un mail de {nom}, sujet : {sujet}, voici le message : {contenu}"
    tts = gTTS(message, lang='fr')
    file_path = '/tmp/message.mp3'  # Enregistrer dans un fichier temporaire

    tts.save(file_path)

    # Retourner le fichier audio ou un message de confirmation
    return jsonify({"message": "Audio généré avec succès", "audio_url": file_path}), 200

@app.route('/')
def home():
    return "L'API fonctionne ! 🚀"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

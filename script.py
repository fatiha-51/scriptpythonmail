from flask import Flask, request, jsonify
from gtts import gTTS
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "L'API fonctionne ! 🚀"

@app.route('/generate-audio', methods=['POST'])
def generate_audio():
    try:
        data = request.get_json()  # Récupère les données envoyées
        nom = data.get('nom')
        sujet = data.get('sujet')
        contenu = data.get('contenu')

        # Créer le texte à convertir en audio
        text = f"Vous avez reçu un mail de {nom}, sujet {sujet}, voici le message : {contenu}"

        # Utilisation de gTTS pour convertir le texte en audio
        tts = gTTS(text)
        tts.save("message.mp3")  # Sauvegarde l'audio dans un fichier

        return jsonify({"message": "Audio généré avec succès"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, request, jsonify
from gtts import gTTS
import os
import uuid
import logging

# Configurez le logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialiser l'application Flask
app = Flask(__name__)

@app.route('/generate-audio', methods=['POST'])
def generate_audio():
    try:
        # Vérifiez si la requête est au format JSON
        if not request.is_json:
            return jsonify({"error": "Request must be JSON"}), 400
        
        # Récupérez les données envoyées dans la requête
        data = request.json
        nom = data.get('nom', 'Expéditeur inconnu')
        sujet = data.get('sujet', 'Sans sujet')
        contenu = data.get('contenu', 'Aucun message')

        logger.info(f"Received request with data: {data}")

        # Construire le texte pour la synthèse vocale
        texte_email = f"Vous avez reçu un mail de {nom}. Sujet : {sujet}. Voici le message : {contenu}."

        # Générer un nom unique pour le fichier audio
        audio_filename = f"{uuid.uuid4()}_email_audio.mp3"

        # Convertir le texte en audio avec gTTS
        tts = gTTS(texte_email, lang='fr')
        tts.save(audio_filename)

        logger.info(f"Audio generated and saved as {audio_filename}")

        # Retournez une réponse JSON indiquant le succès
        return jsonify({
            "message": "✅ Audio généré avec succès",
            "filename": audio_filename
        })
    except Exception as e:
        logger.error(f"Error generating audio: {str(e)}")
        return jsonify({"error": str(e)}), 500

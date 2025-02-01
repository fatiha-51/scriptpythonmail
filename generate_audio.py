from flask import Flask, request, jsonify, send_file
from gtts import gTTS
import io
import logging
import uuid

# Configurez le logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

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

        # Assurez-vous que chaque champ est utilisé pour construire le texte
        texte_email = f"Vous avez reçu un mail de {nom}. Sujet : {sujet}. Voici le message : {contenu}."

        # Ajoutez un identifiant unique pour garantir que chaque texte est différent
        texte_email += f" ID de requête : {uuid.uuid4()}"

        logger.info(f"Generated text for TTS: {texte_email}")

        # Générer l'audio en mémoire avec gTTS
        tts = gTTS(texte_email, lang='fr')

        # Utiliser un tampon en mémoire pour stocker l'audio
        audio_buffer = io.BytesIO()
        tts.write_to_fp(audio_buffer)
        audio_buffer.seek(0)  # Remettre le curseur au début du tampon

        logger.info("Audio generated successfully")

        # Retournez le fichier audio en tant qu'attachement
        return send_file(
            audio_buffer,
            mimetype="audio/mp3",
            as_attachment=True,
            download_name=f"{nom.replace(' ', '_')}_audio.mp3"
        )
    except Exception as e:
        logger.error(f"Error generating audio: {str(e)}")
        return jsonify({"error": str(e)}), 500

from flask import Flask, request, jsonify, send_file
import pyttsx3
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

        # Ajoutez un UUID dans le contenu principal
        unique_id = str(uuid.uuid4())[:8]
        texte_email = (
            f"Vous avez reçu un mail de {nom}. "
            f"Sujet : {sujet}. "
            f"Voici le message avec ID unique : {contenu} ({unique_id})."
        )

        logger.info(f"Generated text for TTS: {texte_email}")

        # Initialiser le moteur de synthèse vocale
        engine = pyttsx3.init()

        # Générer l'audio en mémoire
        audio_buffer = io.BytesIO()
        engine.save_to_file(texte_email, audio_buffer)
        engine.runAndWait()
        audio_buffer.seek(0)

        logger.info("Audio generated successfully")

        # Retournez le fichier audio en tant qu'attachement
        return send_file(
            audio_buffer,
            mimetype="audio/wav",  # pytttsx3 génère des fichiers WAV par défaut
            as_attachment=True,
            download_name=f"{nom.replace(' ', '_')}_audio.wav"
        )
    except Exception as e:
        logger.error(f"Error generating audio: {str(e)}")
        return jsonify({"error": str(e)}), 500

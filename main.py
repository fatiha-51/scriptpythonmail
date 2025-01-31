@app.route('/generate-audio', methods=['POST'])
def generate_audio():
    data = request.get_json()  # Récupère le JSON envoyé dans le body
    nom = data.get('nom')
    sujet = data.get('sujet')
    contenu = data.get('contenu')

    # Code pour générer l'audio ici (par exemple, avec gTTS)

    return jsonify({"message": "Audio généré avec succès"}), 200


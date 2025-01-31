@app.route('/generate-audio', methods=['POST'])
def generate_audio():
    data = request.get_json()
    nom = data.get('nom')
    sujet = data.get('sujet')
    contenu = data.get('contenu')
    # Gérer la génération d'audio ici
    return jsonify({"message": "Audio généré avec succès"}), 200

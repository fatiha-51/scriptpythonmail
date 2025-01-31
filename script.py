from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/generate-audio', methods=['POST'])
def generate_audio():
    # Ton code pour générer l'audio
    data = request.get_json()  # Récupère le JSON envoyé dans le body
    nom = data.get('nom')
    sujet = data.get('sujet')
    contenu = data.get('contenu')

    # Exemple d'action pour générer l'audio
    # Utilise gTTS ou une autre bibliothèque ici pour transformer le texte en audio

    return jsonify({"message": "Audio généré avec succès"}), 200

@app.route('/')
def home():
    return "L'API fonctionne ! 🚀"

if __name__ == '__main__':
    app.run(debug=True)



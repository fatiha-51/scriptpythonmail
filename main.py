from flask import Flask, request, jsonify
import subprocess
import os

app = Flask(__name__)

# Route pour vérifier si l'API fonctionne
@app.route('/')
def home():
    return "L'API fonctionne ! 🚀"

# Route pour exécuter un script Python
@app.route('/run-script', methods=['POST'])
def run_script():
    try:
        output = subprocess.run(["python3", "script.py"], capture_output=True, text=True)
        return jsonify({"message": "Script exécuté", "output": output.stdout})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Lancer l'application sur le port défini par Render
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))  # Render fournit un port spécifique
    app.run(host='0.0.0.0', port=port)

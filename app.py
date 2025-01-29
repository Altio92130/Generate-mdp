from flask import Flask, request, jsonify
from mdp import generate

app = Flask(__name__)

@app.route('/generate', methods=['POST'])
def generate_password():
    data = request.json
    length = data.get("length", 0)  # Longueur par défaut : 0 (pour appliquer ta logique)
    password = generate(length)  # Utiliser ton code Python
    return jsonify({"password": password})

if __name__ == '__main__':
    app.run(debug=True)  # Lancer le serveur en mode développement
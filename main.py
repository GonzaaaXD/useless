from flask import Flask, jsonify, render_template
import random
from datetime import datetime, timedelta

app = Flask(__name__)

# Lista de frases inútiles
useless_phrases = [
    "Tu fortuna: Serás pobre pero feliz.",
    "Dato inútil: Los caracoles pueden dormir hasta 3 años.",
    "La probabilidad de que te caiga un rayo es menor que la de ganar la lotería.",
    "No puedes silbar mientras comes galletas de soda.",
    f"En Marte, la fecha es: {(datetime.utcnow() + timedelta(days=687)).strftime('%Y-%m-%d')}",
    "Si pones una cuchara en la nevera, seguirá siendo una cuchara.",
    "Tu horóscopo: Hoy no pasará nada interesante.",
    "Si gritas durante 8 años, 7 meses y 6 días, generarás suficiente energía para calentar una taza de café.",
    "Hola pepe",
    "En la antartida hace mucho frio",
    "Cristiano Ronaldo, el camello del futbol",
    "Tres de pesos de a peso"
]

# Ruta principal que renderiza la página web
@app.route('/')
def home():
    phrase = random.choice(useless_phrases)
    return render_template('index.html', phrase=phrase)

# Ruta para obtener una frase en formato JSON
@app.route('/useless', methods=['GET'])
def useless_endpoint():
    response = {
        "message": random.choice(useless_phrases)
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(port=5001, debug=True)  # Ejecutar en localhost por defecto

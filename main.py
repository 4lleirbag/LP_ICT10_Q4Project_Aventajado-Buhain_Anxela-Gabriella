from flask import Flask, jsonify, request, send_from_directory
from pathlib import Path

app = Flask(name, static_folder='.', template_folder='.')

classmates = [
    {"name": "Nathan Abaca", "section": "Ruby", "subject": "Science"},
    {"name": "Anthea Alavado", "section": "Ruby", "subject": "Math"},
    {"name": "Maiah Arenal", "section": "Ruby", "subject": "Music and SS"},
    {"name": "Anxela Aventajado", "section": "Ruby", "subject": "Music and SS"},
    {"name": "Gab Buhain", "section": "Ruby", "subject": "Art"},
    {"name": "Joo Carpio", "section": "Ruby", "subject": "SS"},
    {"name": "Caiomey Cenon", "section": "Ruby", "subject": "Break time"},
    {"name": "Athena Cruz", "section": "Ruby", "subject": "TLE"},
    {"name": "Nikolo De Leon", "section": "Ruby", "subject": "PE"},
    {"name": "Chelsea De Peralta", "section": "Ruby", "subject": "SS"},
    {"name": "Jercey Del Barrio", "section": "Ruby", "subject": "English"},
    {"name": "Sittie Dida-Agun", "section": "Ruby", "subject": "Math"},
    {"name": "Jarett Dumlao", "section": "Ruby", "subject": "Math"},
    {"name": "Jakob Estapia", "section": "Ruby", "subject": "TLE"},
    {"name": "Chloe Galope", "section": "Ruby", "subject": "SS"},
    {"name": "Uriel Galura", "section": "Ruby", "subject": "TLE"}
    {"name": "Aaron Guevarra", "section": "Ruby", "subject": "PE"},
    {"name": "Gelo Gurango", "section": "Ruby", "subject": "English"},
    {"name": "Ezra Lazo", "section": "Ruby", "subject": "SS"},
    {"name": "Jakob Liwag", "section": "Ruby", "subject": "SS and PE"},
    {"name": "Anika Magpantay", "section": "Ruby", "subject": "English and SS"},
    {"name": "Kaila Moyaen", "section": "Ruby", "subject": "Music"},
    {"name": "Xander Panuncialman", "section": "Ruby", "subject": "Math"},
    {"name": "Sam Prowel", "section": "Ruby", "subject": "SS"}
    {"name": "Pio Ramos", "section": "Ruby", "subject": "PE"},
    {"name": "Katelyn Sannino", "section": "Ruby", "subject": "SS"},
    {"name": "Andrei Tecson", "section": "Ruby", "subject": "Dismissal"},
    {"name": "Hans Ulit", "section": "Ruby", "subject": "PE and SS"},
    ]


@app.route('/')
def index():
    return send_from_directory('.', 'photo.html')

@app.route('/api/classmates', methods=['GET'])
def get_classmates():
    return jsonify(classmates)

@app.route('/api/classmates', methods=['POST'])
def add_classmate():
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "Invalid JSON payload."}), 400

    name = str(data.get('name', '')).strip()
    section = str(data.get('section', '')).strip()
    subject = str(data.get('subject', '')).strip()

    if not name or not section or not subject:
        return jsonify({"error": "Name, section, and subject are required."}), 400

    new_classmate = {"name": name, "section": section, "subject": subject}
    classmates.append(new_classmate)
    return jsonify(new_classmate), 201

@app.route('/<path:path>')
def static_proxy(path):
    target = Path(path)
    if target.exists():
        return send_from_directory('.', path)
    return jsonify({"error": "Not found."}), 404

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
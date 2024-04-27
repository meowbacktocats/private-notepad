from flask import Flask, request

app = Flask(__name__)

@app.get('/')
def index():
    return '<p>Hello, world!</p>'

@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        ... # Validate details.
    return '' # Render Login template.

@app.get('/note/<int:note_id>')
def notes(note_id: int):
    return f'Note ID: {note_id}'
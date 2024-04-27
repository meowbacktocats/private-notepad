from flask import Flask

app = Flask(__name__)

@app.get('/')
def index():
    return '<p>Hello, world!</p>'

@app.get('/note/<int:note_id>')
def notes(note_id: int):
    return f'Note ID: {note_id}'
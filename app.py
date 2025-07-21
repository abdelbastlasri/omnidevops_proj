from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_cors import CORS
import uuid
from datetime import datetime

app = Flask(__name__)
CORS(app)

# Stockage en mémoire des todos
todos = [
    {"id": str(uuid.uuid4()), "content": "Have fun with htmx", "created_at": datetime.now()},
    {"id": str(uuid.uuid4()), "content": "Go to Noth Pole... swimming", "created_at": datetime.now()},
    {"id": str(uuid.uuid4()), "content": "Improve \"strange\" chords on guitar", "created_at": datetime.now()},
    {"id": str(uuid.uuid4()), "content": "Be amazed by DMVCFramework power", "created_at": datetime.now()}
]

@app.route('/')
def home():
    return render_template('home.html', todos=todos, ispage=True, version="DMVCFramework 3.4.3-aluminium-rc1")

@app.route('/add', methods=['POST'])
def add_todo():
    content = request.form.get('content', '').strip()
    if content:
        new_todo = {
            "id": str(uuid.uuid4()),
            "content": content,
            "created_at": datetime.now()
        }
        todos.append(new_todo)
        return render_template('todo/_item.html', todo=new_todo)
    return '', 204

@app.route('/delete/<todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    global todos
    todos = [todo for todo in todos if todo['id'] != todo_id]
    return '', 204

@app.route('/edit/<todo_id>', methods=['GET'])
def edit_todo_form(todo_id):
    todo = next((t for t in todos if t['id'] == todo_id), None)
    if todo:
        return render_template('_form.html', todo=todo)
    return '', 404

@app.route('/edit/<todo_id>', methods=['PUT'])
def update_todo(todo_id):
    content = request.form.get('content', '').strip()
    todo = next((t for t in todos if t['id'] == todo_id), None)
    if todo and content:
        todo['content'] = content
        return render_template('todo/_item.html', todo=todo)
    return '', 404

@app.route('/todos/<todo_id>')
def get_todo(todo_id):
    todo = next((t for t in todos if t['id'] == todo_id), None)
    if todo:
        return render_template('todo/_item.html', todo=todo)
    return '', 404

@app.route('/cancel')
def cancel():
    return '', 204

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8090, debug=True)


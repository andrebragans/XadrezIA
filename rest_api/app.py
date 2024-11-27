from flask import Flask, request, jsonify

app = Flask(__name__)

# Lista de tarefas
tasks = []

# Rota para criar uma nova tarefa
@app.route('/tasks', methods=['POST'])
def create_task():
    new_task = request.get_json()
    tasks.append(new_task)
    return jsonify(new_task), 201

# Rota para obter todas as tarefas
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

# Rota para obter uma tarefa específica
@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task:
        return jsonify(task)
    else:
        return jsonify({'error': 'Task not found'}), 404

# Rota para atualizar uma tarefa
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    updated_task = request.get_json()
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task:
        task.update(updated_task)
        return jsonify(task)
    else:
        return jsonify({'error': 'Task not found'}), 404

# Rota para excluir uma tarefa
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)

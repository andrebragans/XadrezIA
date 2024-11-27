import requests

BASE_URL = 'http://127.0.0.1:5000/tasks'

# Função para criar uma nova tarefa
def create_task(task):
    response = requests.post(BASE_URL, json=task)
    return response.json()

# Função para obter todas as tarefas
def get_tasks():
    response = requests.get(BASE_URL)
    return response.json()

# Função para obter uma tarefa específica
def get_task(task_id):
    response = requests.get(f"{BASE_URL}/{task_id}")
    return response.json()

# Função para atualizar uma tarefa
def update_task(task_id, task):
    response = requests.put(f"{BASE_URL}/{task_id}", json=task)
    return response.json()

# Função para excluir uma tarefa
def delete_task(task_id):
    response = requests.delete(f"{BASE_URL}/{task_id}")
    return response.status_code

# Teste das funções
if __name__ == '__main__':
    # Criar uma nova tarefa
    new_task = {'id': 1, 'title': 'Aprender API REST', 'description': 'Estudar e implementar um exemplo de API REST.'}
    print('Criar tarefa:', create_task(new_task))

    # Obter todas as tarefas
    print('Tarefas:', get_tasks())

    # Obter uma tarefa específica
    print('Obter tarefa:', get_task(1))

    # Atualizar uma tarefa
    updated_task = {'title': 'Aprender API REST', 'description': 'Estudar e implementar um exemplo completo de API REST.'}
    print('Atualizar tarefa:', update_task(1, updated_task))

    # Excluir uma tarefa
    print('Excluir tarefa:', delete_task(1))

    # Verificar tarefas após exclusão
    print('Tarefas:', get_tasks())

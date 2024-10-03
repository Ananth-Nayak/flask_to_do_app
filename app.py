from flask import Flask, request,redirect, render_template

app = Flask(__name__)

tasks = []

task_id_counter = 1

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route("/add", methods = ['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']

        global task_id_counter
        new_task = {'id': task_id_counter, 'title': title, 'description':description, 'completed': False}
        tasks.append(new_task)
        task_id_counter += 1
        return redirect("/")
    return render_template('add_task.html')

@app.route('/edit/<int:task_id>', methods=['GET', 'POST'])
def edit_task(task_id):
    task = next((t for t in tasks if t['id'] == task_id), None)
    if task:
        if request.method == 'POST':
            task['title'] = request.form['title']
            task['description'] = request.form['description']
            return redirect('/')
        return render_template('edit_task.html', task=task)
    return 'Task not found', 404

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    task = next((t for t in tasks if t['id'] == task_id), None)
    if task:
        tasks.remove(task)
        return redirect('/')
    return 'Task not found', 404

@app.route('/complete/<int:task_id>')
def complete_task(task_id):
    task = next((t for t in tasks if t['id'] == task_id), None)
    if task:
        task['completed'] = True
        return redirect('/')
    return 'Task not found', 404

if __name__ == '__main__':
    app.run(debug=True)
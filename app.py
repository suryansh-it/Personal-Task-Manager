from flask import Flask, render_template , redirect
from flask import request
from flask import url_for

app = Flask(__name__)


tasks = []


@app.route("/")
def index():
    return render_template('index.html')



@app.route("/create_task",methods = ['POST', 'GET'])
def create_task():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        tasks.append({'title': title, 'description': description, 'done': False})  #append tasks in lists
        return redirect(url_for('index'))
    return render_template('create_task.html') #renders updated html



@app.route("/edit_task/<task_id>"  , methods=['POST' , 'GET'])
def edit_task(task_id):
    task = tasks[task_id]               #task from list
    if request.method == 'POST':
        task['title'] = request.form['title']
        task['description'] = request.form['description']
        task['done'] = 'done' in request.form
        return redirect(url_for('index'))
    return render_template('edit_task.html')

@app.route("/toggle_task/<task_id>", methods=['POST' , 'GET'])
def toggle_task(task_id):
    task= tasks[task_id]
    if request.method == 'POST':
        task['done'] = not task['done']
        return redirect(url_for('index'))
    return render_template('toggle_task.html')

@app.route("/delete_task/<task_id>", methods=['POST'])
def delete_task(task_id):
    task = tasks[task_id]
    if request.method == 'POST':
        tasks.remove(task)
        return redirect(url_for('index'))  # Redirect to the home page after editing , client side , It changes the URL in the browser and prevents form resubmission on refresh.


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
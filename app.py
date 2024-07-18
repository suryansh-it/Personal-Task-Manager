from flask import Flask, render_template , redirect , url_for,request, jsonify
from datetime import datetime


app = Flask(__name__)

# In-memory storage for tasks
tasks = []
tasks_done =[]

@app.route("/")
def index():
    return render_template('index.html', tasks= tasks)
#assign value of local variable task to the var task in templates context
#the template will have acces to var task




@app.route("/create_task",methods = ['POST', 'GET'])
def create_task():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S') #date created

        task = {'title': title, 'description': description, 'done': False , 'date_created': current_date }
        tasks.append(task)  #append tasks in lists
        return redirect(url_for('index'))
    return render_template('create_task.html') #renders updated html



@app.route("/edit_task/<int:task_id>"  , methods=['POST' , 'GET']) #type to be specified
def edit_task(task_id):
    task = tasks[task_id]               #task from list
    if request.method == 'POST':
        task['title'] = request.form['title']
        task['description'] = request.form['description']
        return redirect(url_for('index'))
    return render_template('edit_task.html' , task = task , task_id =task_id)



@app.route("/delete_task/<int:task_id>", methods=['POST'])
def delete_task(task_id):
    task = tasks[task_id]
    if request.method == 'POST':
        tasks.pop(task)
        return redirect(url_for('index'))  
    # Redirect to the home page after editing , client side , 
    # It changes the URL in the browser and prevents form resubmission on refresh.


@app.route("/tasks_completed/<int:task_id>" , methods=['POST' , 'GET'])
def tasks_completed(task_id):
    # if request.method == 'POST':  
        task = tasks[task_id]  
        
        task['done'] = True
        task['date_completed'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S') #date completed

        tasks_done.append(task)#append tasks in lists
        tasks.pop(task_id)  
        # return redirect(url_for('index'))
        return render_template('tasks_completed.html', tasks_done=tasks_done, task_id= task_id) #renders updated html
    
    


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
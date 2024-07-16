from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/create_task")
def create_task():
    return render_template('create_task.html')

@app.route("/edit_task/<task_id>"  , methods=['POST'])
def edit_task(task_id):
    return render_template('edit_task.html')



@app.route("/delete_task/<task_id>", methods=['POST'])
def delete_task(task_id):
    return render_template('delete_task.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
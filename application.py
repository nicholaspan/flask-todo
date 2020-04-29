from flask import Flask, render_template, redirect, request

# Initialize the app Flask object
app = Flask(__name__)

todos = []

@app.route("/")
def tasks():
    return render_template("todo.html", todos = todos)

# Allow both GET and POST HTTP requests
@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "GET":
        return render_template("add.html")
    else: 
        new_todo = request.form.get("todo")
        todos.append(new_todo)
        return redirect("/")

@app.route("/remove", methods=["GET", "POST"])
def remove():
    if request.method == "GET":
        return render_template("remove.html")
    else:
        remove_todo = request.form.get("remove-todo")
        if remove_todo in todos:
            todos.remove(remove_todo)
        return redirect("/")


from flask import Flask, render_template, request, redirect, url_for


@app.route("/")
def index():
    todo_list = Todo.query.all()
    return render_template("index.html", tasks=todo_list)

@app.route("/add", methods=["POST"])
def add():
    name = request.form.get("name")
    desc = request.form.get("desc")
    new_todo = Todo(name=name, desc=desc)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for("index"))

@app.route("/update/<int:todo_id>", methods=["POST"])
def update(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    todo.name = request.form.get("name")
    todo.desc = request.form.get("desc")
    db.session.commit()
    return redirect(url_for("index"))

@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("index"))
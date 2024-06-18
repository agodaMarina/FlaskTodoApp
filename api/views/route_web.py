from flask import Flask, render_template, request, redirect, url_for
from api import web

from extensions import db
from models import Todo

@web.route("/")
def index():
    todo_list = Todo.query.all()
    return render_template("index.html", tasks=todo_list)

@web.route("/add", methods=["POST"])
def add():
    name = request.form.get("name")
    desc = request.form.get("desc")
    due_date = request.form.get("due_date")
    new_todo = Todo(name=name, desc=desc, due_date=due_date)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for("index"))

@web.route("/update/<int:todo_id>", methods=["POST"])
def update(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    todo.name = request.form.get("name")
    todo.desc = request.form.get("desc")
    todo.due_date = request.form.get("due_date")
    db.session.commit()
    return redirect(url_for("index"))

@web.route("/delete/<int:todo_id>")
def delete(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("index"))
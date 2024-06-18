from flask import request, jsonify
from api import api
from api.Controllers import TodoController

todo_controller = TodoController()
@api.route("/", methods=["GET"])
def index():
    return todo_controller.search()

@api.route("/<int:id>", methods=["GET"])
def getById(id):
    return todo_controller.getById(id)

@api.route("/create",methods=["POST"])
def create():
    return todo_controller.create()

@api.route("/update/<int:id>", methods=["PUT"])
def update(id):
    return todo_controller.update(id)

@api.route("/delete/<int:id>", methods=["DELETE"])
def delete(id):
    return todo_controller.delete(id)

@api.route("/tri", methods=["GET"])
def all():
    return todo_controller.all()
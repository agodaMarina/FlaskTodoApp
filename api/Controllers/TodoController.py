from api.models.Todo import Todo
from flask import jsonify, request
from extensions import db


class TodoController:

    def __int__(self):
        self.todo=Todo

    def getById(self, id):
            try:
                task = Todo.query.get(id)
                if task:
                    return jsonify({'id': task.id, 'name': task.name}), 200
                else:
                    return jsonify({'message': 'tâche non trouvée'}), 404
            except Exception as e:
                return jsonify({'message': e}), 500  
            

    def create(self):
        try:
            data = request.get_json()
            newTask = self.todo(name=data['name'], desc=data['desc'], due_date=data['due_date'])
            db.session.add(newTask)
            db.session.commit()
            return jsonify({'message': 'Nouvelle tache créée avec succès'}), 201
                   
        except KeyError:
            return jsonify({'message': 'Données manquantes'}), 400
        except Exception as e:
            db.session.rollback()
        return jsonify({'message': str(e)}), 500         

    
    def all(self):
        try:
            taks = Todo.query.all()
            result = [{'id': task.id, 'name': task.name, 'description':task.desk, 'duedate':task.due_date} for task in taks]
            return jsonify(result), 200
        except Exception as e:
            return jsonify({'message': e}), 500


    def update(self, id):
        try:
            data = request.get_json()

            task = Todo.query.get(id)
            if task:
                task.name = data['name']
                task.desc = data['desc']
                task.due_date = data['due_date']
                db.session.commit()
                return jsonify({'message': 'tache mise à jour avec succès'}), 200
            else:
                return jsonify({'message': 'tache non trouvée'}), 404
        except KeyError:
            return jsonify({'message': 'Données manquantes'}), 400
        except Exception as e:
            db.session.rollback()
            return jsonify({'message': e}), 500
        

    def delete(self, id):
        try:
            task = Todo.query.get(id)
            if task:
                db.session.delete(task)
                db.session.commit()
                return jsonify({'message': 'tache supprimée avec succès'}), 200
            else:
                return jsonify({'message': 'tache non trouvée'}), 404
        except KeyError:
            return jsonify({'message': 'Données manquantes'}), 400
        except Exception as e:
            db.session.rollback()
            return jsonify({'message': e}), 500
        

    def search(self):
        try:
            
            tasks = Todo.query.filter(Todo.done==False).all()
            result = [{'id': task.id, 'name': task.name, 'description':task.desk, 'duedate':task.due_date} for task in tasks]
            return jsonify(result), 200
        except Exception as e:
            return jsonify({'message': e}), 500
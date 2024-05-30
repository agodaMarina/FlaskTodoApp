from api.models.Todo import Todo
from flask import jsonify, request
from extensions import db


class TodoController:

    def __int__(self):
        self.todo=Todo

    def create(self):

        try:
            data = request.get_json()
            newTask = self.categorie_model(libelle=data['libelle'])
            db.session.add(newTask)
            db.session.commit()
            return jsonify({'message': 'Nouvelle catégorie créée avec succès'}), 201
        except KeyError:
            return jsonify({'message': 'Données manquantes'}), 400
        except Exception as e:
            db.session.rollback()
            return jsonify({'message': e}), 500

    def all(self):
        try:
            taks = Todo.query.all()
            result = [{'id': Todo.id, 'libelle': Todo.libelle} for categorie in categories]
            return jsonify(result), 200
        except Exception as e:
            return jsonify({'message': e}), 500

    def update(self, categorie_id):
        try:
            data = request.get_json()

            categorie = Categorie.query.get(categorie_id)
            if categorie:
                categorie.libelle = data['libelle']
                db.session.commit()
                return jsonify({'message': 'Catégorie mise à jour avec succès'}), 200
            else:
                return jsonify({'message': 'Catégorie non trouvée'}), 404
        except KeyError:
            return jsonify({'message': 'Données manquantes'}), 400
        except Exception as e:
            db.session.rollback()
            return jsonify({'message': e}), 500

    def delete(self, categorie_id):
        try:
            categorie = Categorie.query.get(categorie_id)
            if categorie:
                db.session.delete(categorie)
                db.session.commit()
                return jsonify({'message': 'Catégorie supprimée avec succès'}), 200
            else:
                return jsonify({'message': 'Catégorie non trouvée'}), 404
        except KeyError:
            return jsonify({'message': 'Données manquantes'}), 400
        except Exception as e:
            db.session.rollback()
            return jsonify({'message': e}), 500
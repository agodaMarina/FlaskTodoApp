from extensions import db
from extensions import db

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    desc = db.Column(db.String(200))
    due_date = db.Column(db.DateTime)
    done = db.Column(db.Boolean, default=False)
from flask_sqlalchemy import SQLAlchemy

...
app.config['SQLALCHEMY_DATABASE_URI'] = '[Your database URL]'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    desc = db.Column(db.String(200))

if __name__ == "__main__":
    db.create_all()
    app.run()
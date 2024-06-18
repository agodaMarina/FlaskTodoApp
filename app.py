from flask import Flask
from flask_cors import CORS


from api import api,web
from extensions import db
from flask_migrate import Migrate

app = Flask(__name__)
CORS(app)
app.register_blueprint(api, url_prefix="/api")
app.register_blueprint(web, url_prefix="/web")


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Marina1234@localhost/flaskbd'
app.config['SQLALCHEMY_TRACK_ MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app,db)
'''with app.app_context():
    db.create_all()'''

if __name__ == '__main__':
    app.run()
from flask import Flask
from routes import classroom_blueprint
from models import db, init_app
from flask_migrate import Migrate
app = Flask(__name__)

app.config['SECRET_KEY'] = "pSaOCtBJ90oNkW9nigTXAw"
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:sumit2109@database-1.cmmco8ooibwj.us-east-1.rds.amazonaws.com/classroom'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.register_blueprint(classroom_blueprint)
init_app(app)
migrate = Migrate(app, db)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)
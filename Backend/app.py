from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from Backend.config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Initialize the database
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Import routes
from routes.auth_routes import auth_routes
from routes.timetable_routes import timetable_routes
from Models.user_models import User

# Register blueprints
app.register_blueprint(auth_routes)
app.register_blueprint(timetable_routes)

if __name__ == '__main__':
    app.run(debug=True)
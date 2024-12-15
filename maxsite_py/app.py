from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.template_folder = 'C:\\Users\\truno\\work\\maxsite\\templates'
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:tana_505@localhost/maxsite"
# Add your database URI here
UPLOAD_FOLDER = 'C:\\Users\\truno\\work\\maxsite\\'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
db = SQLAlchemy(app)
log_manager = LoginManager()
log_manager.init_app(app)


#db.init_app(app)


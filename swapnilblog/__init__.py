from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_ckeditor import CKEditor

app = Flask(__name__)


app.config['SECRET_KEY'] = 'c8324c68a2be34541966a70fcd4321a6'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
ckeditor = CKEditor(app)

from swapnilblog import routes
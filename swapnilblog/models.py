from datetime import datetime
from flask_ckeditor import CKEditorField
from swapnilblog import db


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(50), nullable=False)
    category = db.Column(db.String(50), nullable=True, default="other")

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"
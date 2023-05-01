from app import database as db
from app import login
from flask_login import UserMixin

from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(64), index=True, unique=True)
    password = db.Column(db.String(128))
    employees = db.relationship('Employee', backref='coporation', lazy='dynamic')
    
    def __repr__(self) -> str:
        return '<User: {}>'.format(self.username)
    
    def set_password(self, password_):
        self.password = generate_password_hash(password_)
        
    def check_password(self, password_):
        return check_password_hash(self.password, password_)
    

@login.user_loader
def load_user(id):
    return User.query.get(int(id))
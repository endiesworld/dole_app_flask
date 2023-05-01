import uuid
from datetime import datetime
from app import database as db

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    name = db.Column(db.String(140), index=True, nullable=False)
    unit = db.Column(db.String(140), index=True, nullable=False)
    tenure_year = db.Column(db.Integer, index=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    
    
    def __repr__(self) -> str:
        return '<Employee {}>'.format(self.name)
from models import db
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Task(db.Model):
    __tablename__ = "tasks"

    id = id.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False) 
    status = db.Column(db.String(50), default='Pendente')
    user = db.relationship('User', back_populates='tasks')

    def __repr__(self):
        return f"<Task {self.title} - {self.status}>"
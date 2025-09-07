from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

db = SQLAlchemy()

class User(db.Model): 

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True) 
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

    tasks = relationship("Task", backref='users')

    def __repr__(self):
        return f"<User {self.name}>"
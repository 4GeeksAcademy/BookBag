from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Users(db.Model):
    __tablename__="users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=False, nullable=False)
    email = db.Column(db.String(250), unique=True, nullable=False)
    password = db.Column(db.String(250), unique=False, nullable=False)
    #discussions = db.relationship("Discussions", backref="created_by")

    def __repr__(self):
        return f'<Users {self.email}>'

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name, 
            "email": self.email,
            # do not serialize the password, its a security breach
        }
    
class Discussions(db.Model):
    __tablename__="discussions"
    id=db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    created_by = db.relationship("Users", backref="discussions", foreign_keys=[user_id])
    discussion=db.Column(db.String(500), unique=False, nullable=False)

    def __repr__(self):
        return f'<Discussions {self.id}>'

    def serialize(self):
        return {
            "id": self.id,
            "created_by": self.created_by.serialize(), 
            "discussion": self.discussion,
            # do not serialize the password, its a security breach
        }
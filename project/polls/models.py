from app import db
from sqlalchemy.ext.declarative import declarative_base

class Question(db.Model):

    __tablename__ = 'questions'

    id = db.Column(db.Integer, primary_key=True)
    question_text = db.Column(db.String(255))
    pub_date =  db.Column(db.DateTime, default=db.func.current_timestamp())
    choices = db.relationship("Choice", backref='question')

    def save(self):
        db.session.add(self)
        db.session.commit()

class Choice(db.Model):

    __tablename__ = 'choices'

    id = db.Column(db.Integer, primary_key=True)
    choice_text = db.Column(db.String(255))
    votes = db.Column(db.Integer, default=0)
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'))
#    question = db.relationship('Question', back_populates='choices')

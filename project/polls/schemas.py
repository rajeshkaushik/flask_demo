from flask_restplus import fields

from marshmallow_sqlalchemy import ModelSchema

from polls.models import Question, Choice, User
from app import db, api


class QuestionSchema(ModelSchema):
    class Meta:
        model = Question
        sqla_session = db.session


class ChoiceSchema(ModelSchema):
    class Meta:
        model = Choice
        sqla_session = db.session


class UserSchema(ModelSchema):
    class Meta:
        model = User
        sqla_session = db.session


question_schema = QuestionSchema()
questions_schema = QuestionSchema(many=True)
choice_schema = ChoiceSchema()
choices_schema = ChoiceSchema(many=True)

user_schema = UserSchema()
users_schema = UserSchema(many=True)


question_model = api.model('Questions', {
    'id': fields.Integer(readonly=True),
    'question_text': fields.String,
    'pub_date': fields.Date,
})


user_model = api.model('Users', {
    'name': fields.String("User name"),
    'contact_no':fields.Integer(123456),
    'status':fields.Integer(1)
})

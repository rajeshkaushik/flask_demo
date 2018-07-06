from flask_restplus import fields
from polls.models import Question, Choice, Users
from marshmallow_sqlalchemy import ModelSchema
from app import db,api

class QuestionSchema(ModelSchema):
    class Meta:
        model = Question
        sqla_session = db.session

class ChoiceSchema(ModelSchema):
    class Meta:
        model = Choice
        sqla_session = db.session

class ChoiceSchema(ModelSchema):
    class Meta:
        model = Choice
        sqla_session = db.session



class UsersSchema(ModelSchema):
    class Meta:
        model = Users
        sqla_session = db.session

question_schema = QuestionSchema()
questions_schema = QuestionSchema(many=True)
choice_schema = ChoiceSchema()
choices_schema = ChoiceSchema(many=True)

user_schema = UsersSchema()
users_schema = UsersSchema(many=True)


user_model = api.model('Users', {
    'name': fields.String("test_name"),
    'contact_no':fields.Integer(123456),
    'status':fields.Integer(1)

})




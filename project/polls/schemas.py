from polls.models import Question, Choice
from marshmallow_sqlalchemy import ModelSchema
from app import db

class QuestionSchema(ModelSchema):
    class Meta:
        model = Question
        sqla_session = db.session

class ChoiceSchema(ModelSchema):
    class Meta:
        model = Choice
        sqla_session = db.session

question_schema = QuestionSchema()
questions_schema = QuestionSchema(many=True)
choice_schema = ChoiceSchema()
choices_schema = ChoiceSchema(many=True)


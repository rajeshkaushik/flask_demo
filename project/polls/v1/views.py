from flask_restplus import Resource
from flask import request

from polls.models import Question
from polls.schemas import question_schema, questions_schema, question_model

from app import api


class QuestionListApi(Resource):
    def get(self):
        questions = Question.query.all()
        results = questions_schema.dump(questions)
        return results

    @api.expect(question_model)
    def post(self):
        question = question_schema.load(api.payload).data
        question.save()
        return question_schema.dump(question), 201


class QuestionApi(Resource):

    def get(self, id):
        question = Question.query.get(1)
        return question_schema.dump(question)

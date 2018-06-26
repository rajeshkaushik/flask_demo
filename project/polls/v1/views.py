from flask_restful import Resource, reqparse
from flask import request
from polls.models import Question
from polls.schemas import question_schema, questions_schema

class QuestionListApi(Resource):
    def get(self):
        questions = Question.query.all()
        results = []
        #for question in questions:
        #    obj = {
        #        'id' : question.id,
        #        'question_text': question.question_text
        #    }
        #    results.append(obj)
        results = questions_schema.dump(questions)
        return results


    def post(self):
        #parser = reqparse.RequestParser()
        #parser.add_argument('id')
        #parser.add_argument('question_text')
        #question = Question(**parser.parse_args())
        question = question_schema.load(request.get_json()).data
        question.save()
        #return {'id': question.id}, 201
        return question_schema.dump(question), 201

class QuestionApi(Resource):

    def get(self, id):
        question = Question.query.get(1)
        return question_schema.dump(question)
        #return {'id': question.id, 'question_text': question.question_text}

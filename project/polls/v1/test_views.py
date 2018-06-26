import json
from tests.conftest import MyTestCase
from app import create_app, db
from polls.models import Question

class TestQuestionListApi(MyTestCase):


    def setUp(self):
        super().setUp()
        question = Question(**{'question_text': 'This is test question'})
        db.session.add(question)
        db.session.commit()

    def test_valid_response(self):
        resp = self.client.get('/questions')
        self.assertEqual(200, resp.status_code)
        self.assertEqual(1, resp.json[0]['id'])

    def test_create_question(self):
        resp = self.client.post('/questions', data=json.dumps({'question_text': 'Shall we use Flask-Restful?'}), content_type='application/json')
        self.assertEqual(201, resp.status_code)


class TestQuestionApi(MyTestCase):


    def setUp(self):
        super().setUp()
        question = Question(**{'question_text': 'This is test question'})
        db.session.add(question)
        db.session.commit()

    def test_valid_response(self):
        resp = self.client.get('/questions/1')
        self.assertEqual(200, resp.status_code)
        self.assertEqual(1, resp.json['id'])
        self.assertEqual('This is test question', resp.json['question_text'])


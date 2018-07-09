from flask_restplus import Namespace


poll_ns = Namespace('polls', description="Poll APIs")


from polls.v1.views import QuestionListApi, QuestionApi
from polls.v1.restplus_views import UsersApi


poll_ns.add_resource(QuestionListApi, '/questions')
poll_ns.add_resource(QuestionApi, '/questions/<int:id>')
poll_ns.add_resource(UsersApi, '/users')

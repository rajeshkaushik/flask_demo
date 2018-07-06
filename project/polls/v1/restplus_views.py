from flask_restplus import Resource
from flask import request
from polls.models import Users
from polls.schemas import user_schema, users_schema,user_model
from app import api




class UsersApi(Resource):
    def get(self):
        """

        :return:
        """
        print("yes in get function")
        users = Users.query.all()
        user_data = users_schema.dump(users)
        return (user_data)

    @api.expect(user_model)
    def post(self):
        """
        :return:
        """
        try:
            user = user_schema.load(request.get_json()).data
            user.save()
        # except Exception as e:
        except Exception as e:
            print(e,"++++++++++++++++")





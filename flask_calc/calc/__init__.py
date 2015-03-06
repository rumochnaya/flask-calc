__author__ = 'scorpius'


from flask import Blueprint
from flask.ext import restful
from flask.ext.restful import reqparse

url_prefix = '/calc'

bp_app = Blueprint('archive', __name__)

api = restful.Api(bp_app, prefix=url_prefix)


class Calc(restful.Resource):
    def get(self, action):
        return {"result": True}

    def post(self, action):
        parser = reqparse.RequestParser()
        parser.add_argument('one', type=int, location='json', required=True)
        parser.add_argument('two', type=int, location='json', required=True)

        args = parser.parse_args()

        result = getattr(self, "_post_" + action)(args['one'], args['two'])

        return result

    def _post_sum(self, one, two):
        return {"result": one+two}


api.add_resource(Calc, '/<any("", "sum"):action>', methods=['GET', 'POST'])
 

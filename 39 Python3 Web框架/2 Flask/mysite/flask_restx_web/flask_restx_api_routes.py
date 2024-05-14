from flask import Flask
from flask_restx import Api, Resource

app = Flask(__name__)
api = Api(app, version='1.0', title='Multi-level Route API', description='API with multi-level routes')


# 多级路由示例
@api.route('/users')
class UserList(Resource):
    def get(self):
        return {'message': 'GET /users'}

    def post(self):
        return {'message': 'POST /users'}


@api.route('/users/<int:user_id>')
class User(Resource):
    def get(self, user_id):
        return {'message': f'GET /users/{user_id}'}

    def put(self, user_id):
        return {'message': f'PUT /users/{user_id}'}


# 更多级别的路由示例
@api.route('/users/<int:user_id>/posts')
class UserPosts(Resource):
    def get(self, user_id):
        return {'message': f'GET /users/{user_id}/posts'}

    def post(self, user_id):
        return {'message': f'POST /users/{user_id}/posts'}


if __name__ == '__main__':
    app.run()

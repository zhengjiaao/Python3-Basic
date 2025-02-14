from flask import Blueprint, request, jsonify
from flask_restx import Namespace, Resource, fields

user_app = Blueprint('user_app', __name__)
user_namespace = Namespace('users', description='User operations')

# 用户列表
users = []
# 用户模型
user_model = user_namespace.model('User', {
    'name': fields.String(required=True, description='User name'),
    'email': fields.String(required=True, description='User email')
})


# 用户服务管理
@user_namespace.route('/')
class UserList(Resource):

    def get(self):
        """查询全部用户"""
        return {'users': users}
        # return jsonify(users)


@user_namespace.route('/create')
class CreateUser(Resource):
    @user_namespace.expect(user_model, validate=True)  # 使用 expect 装饰器定义请求体模型
    def post(self):
        data = user_namespace.payload  # 使用 api.payload 获取请求体数据
        name = data.get('name')
        email = data.get('email')

        new_user = {'id': len(users) + 1, 'name': name, 'email': email}
        # new_user = {'id': len(users) + 1, 'name': "李四", 'email': "123@.qq.com"}
        users.append(new_user)

        return {'message': 'User created', 'user': new_user}, 201


# 放默认组里面
# @api.route('/users/<int:user_id>')
# 放自定义组里面
@user_namespace.route('/users/<int:user_id>')
class User(Resource):
    def get(self, user_id):
        """查询指定用户"""
        user = next((user for user in users if user['id'] == user_id), None)
        if user:
            return {'user': user}
        else:
            return {'message': 'User not found'}, 404
            # return jsonify({'message': 'User not found'}), 404

    def delete(self, user_id):
        """删除用户"""
        user = next((user for user in users if user['id'] == user_id), None)
        if user:
            del users[user_id]
            return {'message': 'User deleted successfully'}
        else:
            return {'message': 'User not found'}, 404
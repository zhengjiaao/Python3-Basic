from flask import Flask, request, jsonify
from flask_restx import Api, Namespace, Resource, fields

app = Flask(__name__)
# 中问乱码问题
app.json.ensure_ascii = False
app.config['JSON_AS_ASCII'] = False

# swagger API
api = Api(app, version='1.0', title='User and Role API', description='API for user and role management')
# swagger 组
user_namespace = Namespace('users', description='用户服务管理')

# 模拟数据库
users = []


# 用户服务管理
@user_namespace.route('/')
class UserList(Resource):

    def get(self):
        """查询全部用户"""
        return {'users': users}
        # return jsonify(users)


user_model = api.model('User', {
    'name': fields.String(required=True, description='User name'),
    'email': fields.String(required=True, description='User email')
})


@user_namespace.route('/create')
class CreateUser(Resource):
    @api.expect(user_model, validate=True)  # 使用 expect 装饰器定义请求体模型
    def post(self):
        data = api.payload  # 使用 api.payload 获取请求体数据
        name = data.get('name')
        email = data.get('email')

        new_user = {'id': len(users) + 1, 'name': name, 'email': email}
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


# 将命名空间添加到 API
api.add_namespace(user_namespace)

# 运行方式：python3 user.py
# 启动 Flask 服务器 ,
# 默认访问： http://127.0.0.1:5000
# 访问：http://127.0.0.1:5000/users
if __name__ == '__main__':
    app.run(debug=True)

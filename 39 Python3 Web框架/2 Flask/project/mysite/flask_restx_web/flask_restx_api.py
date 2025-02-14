from flask import Flask
from flask_restx import Api, Resource

app = Flask(__name__)
api = Api(app, version='1.0', title='User and Role API', description='API for user and role management')

users = []
roles = []


# 用户服务管理
@api.route('/users')
class UserList(Resource):
    def get(self):
        """GET请求-获取全部用户"""
        return {'users': users}

    def post(self):
        # 在此处处理创建用户的逻辑
        new_user = {'id': len(users) + 1, 'name': 'John Doe'}
        users.append(new_user)
        return {'message': 'User created', 'user': new_user}, 201


@api.route('/users/<int:user_id>')
class User(Resource):
    def get(self, user_id):
        """GET请求-获取指定用户"""
        user = next((user for user in users if user['id'] == user_id), None)
        if user:
            return {'user': user}
        else:
            return {'message': 'User not found'}, 404


# 角色服务管理
@api.route('/roles')
class RoleList(Resource):
    def get(self):
        return {'roles': roles}

    def post(self):
        """POST请求-添加角色"""
        # 在此处处理创建角色的逻辑
        new_role = {'id': len(roles) + 1, 'name': 'admin'}
        roles.append(new_role)
        return {'message': 'Role created', 'role': new_role}, 201


@api.route('/roles/<int:role_id>')
class Role(Resource):
    def get(self, role_id):
        role = next((role for role in roles if role['id'] == role_id), None)
        if role:
            return {'role': role}
        else:
            return {'message': 'Role not found'}, 404


if __name__ == '__main__':
    app.run()

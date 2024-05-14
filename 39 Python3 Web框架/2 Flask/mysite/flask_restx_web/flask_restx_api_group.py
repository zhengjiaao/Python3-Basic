from flask import Flask
from flask_restx import Api, Resource, Namespace

app = Flask(__name__)
api = Api(app, version='1.0', title='User and Role API', description='API for user and role management')

# 创建命名空间
user_namespace = Namespace('users', description='User services')
role_namespace = Namespace('roles', description='Role services')

users = []
roles = []


# 用户服务管理
@user_namespace.route('/')
class UserList(Resource):
    def get(self):
        """GET请求-获取全部用户"""
        return {'users': users}

    def post(self):
        """POST请求-新增用户"""
        # 在此处处理创建用户的逻辑
        new_user = {'id': len(users) + 1, 'name': 'John Doe'}
        users.append(new_user)
        return {'message': 'User created', 'user': new_user}, 201


@user_namespace.route('/<int:user_id>')
class User(Resource):
    def get(self, user_id):
        """GET请求-获取指定用户"""
        user = next((user for user in users if user['id'] == user_id), None)
        if user:
            return {'user': user}
        else:
            return {'message': 'User not found'}, 404


# 角色服务管理
@role_namespace.route('/')
class RoleList(Resource):
    def get(self):
        return {'roles': roles}

    def post(self):
        # 在此处处理创建角色的逻辑
        new_role = {'id': len(roles) + 1, 'name': 'admin'}
        roles.append(new_role)
        return {'message': 'Role created', 'role': new_role}, 201


@role_namespace.route('/<int:role_id>')
class Role(Resource):
    def get(self, role_id):
        role = next((role for role in roles if role['id'] == role_id), None)
        if role:
            return {'role': role}
        else:
            return {'message': 'Role not found'}, 404


# 将命名空间添加到 API
api.add_namespace(user_namespace)
api.add_namespace(role_namespace)

if __name__ == '__main__':
    app.run()

from flask import Blueprint, request, jsonify
from flask import abort
from flask_restx import Namespace, Resource, fields
import logging

role_app = Blueprint('role_app', __name__)
# role_namespace = Namespace('roles', description='Role operations')
ns = Namespace('roles', description='Role operations')

roles = []

# 使用字典优化查找性能
role_dict = {role['id']: role for role in roles if 'id' in role}

# 角色模型
role = ns.model('Role', {
    'id': fields.Integer(required=True, description='The Role identifier'),
    'name': fields.String(required=True, description='Role name')
})


# 角色服务管理
@ns.route('/create')
class RoleCreate(Resource):

    @ns.doc('create_todo')
    @ns.expect(role)  # 请求数据格式(必需的)
    @ns.marshal_with(role, code=201)  # 响应数据格式(推荐)
    def post(self):
        """创建角色"""
        role_data = ns.payload
        id = role_data.get('id')

        if any(role['id'] == id for role in roles):
            ns.abort(400, 'Role already exists')

        roles.append(role_data)
        return role_data, 201
        # return {'message': 'Role created', 'role': role_data}, 201 # 与 @ns.marshal_with 不一致时，无法展示


@ns.route('/update')
class RoleUpdate(Resource):
    @ns.doc('update_role')
    @ns.expect(role)
    @ns.marshal_with(role)
    def put(self):
        """更新角色"""
        role_data = ns.payload
        id = role_data.get('id')
        role = next((role for role in roles if role['id'] == id), None)
        if role:
            role.update(role_data)
            return role
        else:
            ns.abort(404, "Role {} doesn't exist".format(id))


@ns.route('/list')
class RoleList(Resource):
    @ns.doc('list_roles')
    @ns.marshal_list_with(role)
    def get(self):
        """获取所有角色"""
        return roles


@ns.route('/find/<int:id>')
@ns.param('id', 'The Role identifier')
class RoleResource(Resource):
    @ns.doc('get_role')
    @ns.marshal_with(role)
    def get(self, id):
        """获取角色"""
        print(id)
        print("Roles:", roles)

        # 验证ID的合法性（例如避免负数）
        if id < 0:
            abort(400, "Invalid Role ID")

        # 写法1
        role = next((role for role in roles if role['id'] == id), None)
        if role:
            return role
        else:
            logging.warning(f"Role with ID {id} was requested but does not exist.")
            ns.abort(404, "Role {} doesn't exist".format(id))

        # 写法2
        # for role in roles:
        #     if role['id'] == id:
        #         return role
        # ns.abort(404, "Role {} doesn't exist".format(id))

    @ns.doc('delete_role')
    @ns.response(204, 'Role deleted')
    def delete(self, id):
        """删除角色"""
        print(id)
        role = next((role for role in roles if role['id'] == id), None)
        if role:
            roles.remove(role)
            return '', 204
            # return {'message': 'Role deleted'}, 204
        else:
            return {'message': 'Role not found'}, 404

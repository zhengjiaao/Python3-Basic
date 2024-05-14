from flask import Blueprint, request, jsonify

role_app = Blueprint('role_app', __name__)

roles = {
    1: {'name': '管理员'},
    2: {'name': '普通用户'}
}


@role_app.route('/roles', methods=['POST'])
def create_role():
    # 处理创建角色的逻辑
    role_data = request.get_json()
    role_id = role_data.get('id')
    if role_id in roles:
        return jsonify({'message': 'Role already exists'}), 400
    roles[role_id] = role_data
    return jsonify({'message': 'Role created successfully'}), 201


@role_app.route('/roles/<role_id>', methods=['GET'])
def get_role(role_id):
    # 处理获取角色信息的逻辑
    if role_id not in roles:
        return jsonify({'message': 'Role not found'}), 404
    return jsonify(roles[role_id])


@role_app.route('/roles/<role_id>', methods=['DELETE'])
def delete_role(role_id):
    # 处理删除角色的逻辑
    if role_id not in roles:
        return jsonify({'message': 'Role not found'}), 404
    del roles[role_id]
    return jsonify({'message': 'Role deleted successfully'})


# 获取所有角色信息
@role_app.route('/roles', methods=['GET'])
def get_all_roles():
    return jsonify(roles), 200, {'Content-Type': 'application/json; charset=utf-8'}

# if __name__ == '__main__':
#     role_app.run()

from flask import Blueprint, request, jsonify

user_app = Blueprint('user_app', __name__)

users = {
    1: {
        'name': 'John Doe',
        'email': 'johndoe@example.com',
        'password': 'password'
    },
    2: {
        'name': '李四',
        'email': 'lisi@example.com',
        'password': 'password'
    }
}


# 创建用户
@user_app.route('/users', methods=['POST'])
def create_user():
    # 处理创建用户的逻辑
    user_data = request.get_json()
    user_id = user_data.get('id')
    if user_id in users:
        return jsonify({'message': 'User already exists'}), 400
    users[user_id] = user_data
    return jsonify({'message': 'User created successfully'}), 201


# 获取用户信息
@user_app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    # 处理获取用户信息的逻辑
    if user_id not in users:
        return jsonify({'message': 'User not found'}), 404
    return jsonify(users[user_id])


# 删除用户
@user_app.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    # 处理删除用户的逻辑
    if user_id not in users:
        return jsonify({'message': 'User not found'}), 404
    del users[user_id]
    return jsonify({'message': 'User deleted successfully'})


# 获取所有用户信息
@user_app.route('/users', methods=['GET'])
def get_all_users():
    return jsonify(users)

# if __name__ == '__main__':
#     user_app.run()

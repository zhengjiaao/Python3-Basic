from flask import Flask, request, jsonify

app = Flask(__name__)

# 中问乱码
app.json.ensure_ascii = False
app.config['JSON_AS_ASCII'] = False

app.config['DEBUG'] = True

# 字典来存储用户信息
users = []


@app.route('/users', methods=['POST'])
def create_user():
    user_data = request.get_json()
    user_id = user_data.get('id')
    if user_id in users:
        return jsonify({'message': 'User already exists'}), 400
    users[user_id] = user_data
    return jsonify({'message': 'User created successfully'}), 201


@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    if user_id not in users:
        return jsonify({'message': 'User not found'}), 404
    return jsonify(users[user_id])


@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id not in users:
        return jsonify({'message': 'User not found'}), 404
    del users[user_id]
    return jsonify({'message': 'User deleted successfully'})


@app.route('/users', methods=['GET'])
def get_all_users():
    return jsonify(users)


# 运行方式：python3 user.py
# 启动 Flask 服务器 , 默认访问： http://127.0.0.1:5000
if __name__ == '__main__':
    app.run()
    # app.run(port=5000) # 默认端口号设置为 5000

# 访问：http://127.0.0.1:5000/users

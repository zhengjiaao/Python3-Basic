import yaml

# 读取配置文件
with open('config/config.yaml', 'r') as f:
    config = yaml.safe_load(f)

# 从配置中获取参数
app_name = config['app']['name']
debug_mode = config['app']['debug']
api_version = config['api']['version']
api_title = config['api']['title']
api_description = config['api']['description']
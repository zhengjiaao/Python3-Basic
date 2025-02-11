import redis
import uuid
import time

# 创建Redis连接
# redis_client = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)
redis_client = redis.StrictRedis(host='192.168.1.60', port=31398, db=8, password='r0&3o6^NtJOZ', decode_responses=True)


# 增加（Set）
def set_key(key, value):
    """
    设置键值对
    :param key: 键
    :param value: 值
    """
    redis_client.set(key, value)


# 查询（Get）
def get_key(key):
    """
    获取键值
    :param key: 键
    :return: 值
    """
    return redis_client.get(key)


# 修改（Set）
def update_key(key, value):
    """
    修改键值对
    :param key: 键
    :param value: 新值
    """
    redis_client.set(key, value)


# 删除（Delete）
def delete_key(key):
    """
    删除键值对
    :param key: 键
    """
    redis_client.delete(key)


# 获取锁
def acquire_lock(lock_name, acquire_timeout=10):
    """
    获取分布式锁
    :param lock_name: 锁名称
    :param acquire_timeout: 尝试获取锁的超时时间
    :return: 锁标识符或False
    """
    identifier = str(uuid.uuid4())
    end = time.time() + acquire_timeout
    while time.time() < end:
        if redis_client.setnx(lock_name, identifier):
            return identifier
        time.sleep(0.001)
    return False


# 释放锁
def release_lock(lock_name, identifier):
    """
    释放分布式锁
    :param lock_name: 锁名称
    :param identifier: 锁标识符
    :return: 是否成功释放锁
    """
    pipe = redis_client.pipeline(True)
    while True:
        try:
            pipe.watch(lock_name)
            if pipe.get(lock_name) == identifier:
                pipe.multi()
                pipe.delete(lock_name)
                pipe.execute()
                return True
            pipe.unwatch()
            break
        except redis.WatchError:
            pass
    return False


# 示例：使用分布式锁保护资源
def example_protected_resource():
    lock_name = 'my_resource_lock'
    identifier = acquire_lock(lock_name)

    if identifier:
        try:
            # 在这里执行需要保护的操作
            print("Lock acquired, performing protected operation...")
        finally:
            release_lock(lock_name, identifier)
    else:
        print("Failed to acquire lock")


# 示例调用
if __name__ == "__main__":
    # CRUD操作示例
    set_key('test_key', 'test_value')
    print(get_key('test_key'))  # 输出: test_value
    update_key('test_key', 'new_value')
    print(get_key('test_key'))  # 输出: new_value
    delete_key('test_key')
    print(get_key('test_key'))  # 输出: None

    # 分布式锁示例
    example_protected_resource()

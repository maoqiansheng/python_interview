from redis import StrictRedis

redis_conn = StrictRedis(host='localhost', port=6379)
redis_conn.set('name', 'maoqiansheng')
name = redis_conn.get('name').decode()
print(name)
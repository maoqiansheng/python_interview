# 导⼊模块
import multiprocessing

# 定义消息队列
# 如果不指定队列⻓度，则默认为最⼤，如果指定了消息队列的⼤⼩，则消息队列就有上限控制
# 此处的 Queue(3) 指的是放⼊3条消息
queue = multiprocessing.Queue(3)
# queue.put(值) 向消息队列中放⼊内容
# put的值⼏乎可以是任意类型
queue.put(1)  # 放⼊第⼀个值
queue.put("hello")  # 放⼊第⼆个值
queue.put([1, 2, 3])  # 放⼊第三个值
# 打印队列对象
print(queue.full())
print(queue)
# 获取第⼀个值
value1 = queue.get()
print(value1)

# 获取第⼆个值
value2 = queue.get()
print(value2)
# 获取第三个值
value3 = queue.get()
print(value3)
print(queue.empty())

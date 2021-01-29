"""
序列化：  模型（对象）和 原始数据（json，dict, xml）之间的相互转化， 数据的校验

创建序列化器：字段，类型要和对应的模型保持一致
        read_only = True, 表示只读， 只在序列化时候使用

"""
# 序列化的接口中使用

# 1、获取对象
# book = BookInfo.objects.get(id=1)
# 2、生成序列化器
# serializer = BooKSerializer(isinstance=book)
# 3、获取json数据
# data = serilizer.data

# 多个对象序列化的时候，需要告诉序列化器：many=True
# books = BookInfo.objects.all()
# serializer = BookSerializer(books, many=True)
# serializer.data


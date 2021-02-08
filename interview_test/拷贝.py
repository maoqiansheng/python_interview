# import copy
# a = [1, 2, 3, 4, ['a', 'b']]  #原始对象
#
# b = a  #赋值，传对象的引用
# c = copy.copy(a)  #对象拷贝，浅拷贝
# d = copy.deepcopy(a)  #对象拷贝，深拷贝
#
# a.append(5)  #修改对象a
# a[4].append('c')  #修改对象a中的['a', 'b']数组对象
#
# print(b)
# print(c)
# print(d)


import copy
# 浅拷贝可以分四种
a = [1, 2, 3, [4, 5], 6]
b = a[:]  # 切片操作

c = copy.copy(a)  # 拷贝函数
d = list(a)  # 工厂函数
e = [x for x in a]  # 推到式
f = copy.deepcopy(a)
e[3].append(7)
print('a', id(a), a)
print('b', id(b), b)
print('c', id(c), c)
print('d', id(d), d)
print('e', id(e), e)
print('f', id(f), f)
a_id_list = [id(x) for x in a]
b_id_list = [id(x) for x in b]
f_id_list = [id(x) for x in f]
print(a_id_list)
print(b_id_list)
print(f_id_list)

# 总结：浅拷贝虽然会开辟新的内存空间，但是拷贝容器内元素的id是一样的（是对对象内的元素的引用），
# 如果容器内元素发生改变，新的浅拷贝对象的元素也会发生改变

# 深拷贝则是拷贝对象内的所有元素，
# 对于非容器类型，如数字、字符，以及其他的“原子”类型，没有拷贝一说，产生的都是原对象的引用，例如a中的整型元素，无论深拷贝还是浅拷贝，都只是对元素内存
# 空间的引用
# 如果元组变量值包含原子类型对象，即使采用了深拷贝，也只能得到浅拷贝。

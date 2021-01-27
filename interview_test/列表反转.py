# 1、reversed

l1 = ['a', 'b', 'c']
l2 = list(reversed(l1))
print(l2)

t1 = ('a', 'b', 'c')
t2 = tuple(reversed(t1))
print(t2)

s1 = 'abc'
s2 = ''.join(reversed(s1))
print(s2)
# 2、切片[::-1]

l3 = l1[::-1]
print(l3)
t3 = t1[::-1]
print(t3)
s3 = s1[::-1]
print(s3)
# 列表的原地反转
l1.reverse()
print(l1)
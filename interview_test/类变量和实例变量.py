class Person:
    name = "aaa"


p1 = Person()
p2 = Person()
p1.name = "bbb"
print(p1.name)  # bbb
print(p2.name)  # aaa
print(Person.name)  # aaa



# class Person:
#     name=[]
#
# p1=Person()
# p2=Person()
# p1.name.append(1)
# print(p1.name)  # [1]
# print(p2.name)  # [1]
# print(Person.nam)  # [1]
obj ={"name":"ayyoob",'age':20}
str = "my name is {} and age is {}".format(obj['name'],obj['age'])
print(str)
list = [1,2,3,4,5,6,7,8,9,5,2,0,36,5]
lenth = len(list)
# for i in list:
#     print(i)
#
# for i in str:
#     print(i)

list2 =[45,6,2]

for a,b in zip(list,list2):
    print(a,b,"haha")

for n in obj:
    print(n, obj[n])


# dictionary function
# obj.get('key')
# del obj['key']
# keys()
# values()
# items()
# pop()
# dict()
# update()
# clear()
# dict() to create dictionary
# example
# d = dict(name = 1,b = 3)
# print(d)

nasteddist = {'php':{'name':"abb"},'php2':{'name':"abb2"},'php3':{'name':"abb3"},'php4':{'name':"abb4"},}

# for key in nasteddist:
#     print(nasteddist[key]['name'])
# del nasteddist['php4']['name']
# print(nasteddist)

#tuple=(1,2,3,4,5,6,7,8,9) immutable nochanges tuple[0] access value
# min() max() count() index() sum()

# tuple=(11,20,30,40,50,6,7,8,9)
#
# for t in tuple:
#     print(t)
# print(sum(tuple))
# print(max(tuple))
# print(tuple.index(50))

# set = {1,2,3,4,5} unordered unique
# for s in set:
#     print(s)
# set() add() pop() remove() clear() discard() update()
# s.pop() pop delete randomly any element of set and return that value
# s.remove(element)
# list to set conversion
# l = [1,2,3,4,5,6,6,6,6,6]
# s = set(l)
# print(s)


#function
# def abc(abc):
#     return abc
#
# print(abc(15))

# random module
# random() return a float random number bw 0 - 1
# shuffle() takes a sequence and return it random order
# uniform() return a random float number bw to given parameter
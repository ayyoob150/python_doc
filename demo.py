import datetime
import json
import pickle
import random

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
# choice() return a random element from a list
# random() return a float random number bw 0 - 1
# shuffle() takes a sequence and return it random order
# uniform() return a random float number bw to given parameter
# random.randrange(1,101)  return a random number bw to given parameter


# r = random.random()
# print(r)
#
# time = datetime.datetime.now()
# print(time)

# pickle module is use for read and write
# dump() to write, wb - write binary and load() to read , rb readbinary ,

# l2 = [525,64564,54,54,4,52,]
#
# file = open('write.txt','wb')
# pickle.dump(l2,file)
# file.close()

# file = open('write.txt','rb')
# print(pickle.load(file))

# to convert dictionary to json json.dumps(dictionary)
#  convert json to python json.loads(jsonData)


# read a json file in python
# file = open('file.json','r')
# read = file.read()
# dictfile = json.loads(read)
# print(dictfile)

# Class
# class AddAll:
#     y=100
#     def abcd(self):
#         print(self.y)
#         b=10+self.y
#         print(b)
# abc = AddAll()
# print(abc.y)
# abc.abcd()

# constructor
# class Constructors:
#     def __init__(self):
#         print("hey there how are you")
# constr = Constructors()




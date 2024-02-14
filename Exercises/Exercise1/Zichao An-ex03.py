#ex03-o1
from functools import reduce

text = {1: "welcome to the World", 2: "of Big Big Data", 3: "welcome world Bye"}

print(text.values())

tempList = reduce(lambda x, y: x + " " + y, text.values()).split(" ")
print(tempList)


def map_func(t):
    return (len(t), 1)
shuffle = list(map(map_func, tempList))
print(shuffle)


def map2_func(s):
    d = {}
    for k,v in s:
        if d.keys().__contains__(k):
            d[k] +=v
        else:
            d[k]=v
    return d
shuffleDic = map2_func(shuffle)
print(shuffleDic)

def convertList(dic):
    lis=[]
    for k,v in dic.items():

        lis.append((k,v))
    return lis

shuffleList=convertList(shuffleDic)
print(shuffleList)

def reduce_func(x, y):
    total_length = x[0] + y[0]
    total_words = x[1] + y[1]
    return (total_length, total_words)


output = list(reduce(reduce_func,map(lambda x:(x[0]*x[1],x[1]),shuffleList)))
print(output)


#ex03-o2
input=[(2,2),(3,4),(4,1),(5,2),(7,2)]

convertInput=list(map(lambda x:(x[1],x[0]),input))
print(convertInput)

shuffle2=list(map(lambda x:(x[0],x[0]*x[1]),convertInput))
print(shuffle2)

output2 = list(reduce(reduce_func, shuffle2))
print(output2)
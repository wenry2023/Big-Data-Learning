from functools import reduce

text = {1: "Welcome to the World", 2: "of Big Big Data", 3: "Welcome World Bye"}

def modi1(ls):
    lst = []
    for item in ls:
        lst.append([item, len(item)] + [[1]])
    return lst

text = list(map(modi1, list(map(lambda s: s.split(" "), text.values()))))
# print(text)
new_dic = {}
for item in text:
    for item1 in item:
        if item1[1] in new_dic.keys():
            val = new_dic.get(item1[1])
            val += item1[2]
            new_dic[item1[1]] = val
        else:
            new_dic[item1[1]] = item1[2]
# print(new_dic)
for item in new_dic.items():
    new_dic[item[0]] = reduce(lambda x, y: x + y, item[1])
    
new_lst = []
for item in new_dic.items():
    new_lst.append([item[0] * item[1], item[1]])
#print(new_lst)
def reduce_fun(f, s):
    total_word_length = f[0] + s[0]
    total_word_number = f[1] + s[1]
    return [total_word_length, total_word_number]
changed1_lst = reduce(reduce_fun, new_lst)

print(reduce(lambda x, y: int(x / y), changed1_lst))



### Exercise 3 - 2

ls = [[2, 2], [3, 4], [4, 1], [5, 2], [7, 2]]

def modi(s):
    return [s[0] * s[1], s[1]]

def reduce_fun(f, s):
    total_word_length = f[0] + s[0]
    total_word_number = f[1] + s[1]
    return [total_word_length, total_word_number]

print(reduce(lambda x, y: int(x / y), reduce(reduce_fun, list(map(modi, ls)))))

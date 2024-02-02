# Title 1
## Title 2
### Title 3
#### Title 4
##### Title 5


> This is a reference


ordered list:
* 1
* 2
* 3

___

unordered list:
- 1
- 2
- 3

___
check box:
- [ ] book
- [ ] cat
- [x] dog

___

~~delete line~~

___


link：
<br><b>[Baidu](https://www.baidu.com)</b>

___

table:

|Name|Gender|Age|
|----|------|---|
|Tom|M|18|
|Mary|F|20|
|Jack|M|22|

___


code blocks:
```python

print('hello')

```

---
Mathematical Formula:
$$
\frac{\partial f}{\partial x} = 2\sqrt{a}x
$$

$$
\theta=x^2
$$
---




# 总结

## 数据结构


### 列表(list)

>是一种有序的、可变的数据结构，可以存储任意类型的数据，并且可以通过索引来访问和修改其中的元素。列表的创建方法是用方括号（[]）把元素用逗号隔开，或者用list()函数把一个可迭代对象转换为列表。列表的常用操作有添加、删除、修改、排序、反转、切片、合并等

<br>

---

Python:

```python

# 创建一个列表
my_list = [1, 2, 3, "hello", True]
print(my_list) # [1, 2, 3, 'hello', True]

# 访问列表中的元素
print(my_list[0]) # 1
print(my_list[-1]) # True

# 修改列表中的元素
my_list[1] = 4
print(my_list) # [1, 4, 3, 'hello', True]

# 添加元素到列表末尾
my_list.append(6)
print(my_list) # [1, 4, 3, 'hello', True, 6]

# 删除列表中的元素
my_list.pop() # 返回并删除最后一个元素
print(my_list) # [1, 4, 3, 'hello', True]
my_list.remove(3) # 删除第一个出现的指定元素
print(my_list) # [1, 4, 'hello', True]
del my_list[1] # 删除指定索引的元素
print(my_list) # [1, 'hello', True]

# 排序列表
my_list = [5, 2, 4, 1, 3]
my_list.sort() # 对列表进行升序排序
print(my_list) # [1, 2, 3, 4, 5]
my_list.sort(reverse=True) # 对列表进行降序排序
print(my_list) # [5, 4, 3, 2, 1]

# 反转列表
my_list = [1, 2, 3, 4, 5]
my_list.reverse() # 将列表中的元素反向排列
print(my_list) # [5, 4, 3, 2, 1]

# 切片列表
my_list = [1, 2, 3, 4, 5]
print(my_list[1:3]) # 返回列表中索引1到2的元素，不包括3，即[2, 3]
print(my_list[:3]) # 返回列表中索引0到2的元素，不包括3，即[1, 2, 3]
print(my_list[3:]) # 返回列表中索引3到最后的元素，即[4, 5]
print(my_list[::2]) # 返回列表中每隔一个元素的元素，即[1, 3, 5]

# 合并列表
my_list1 = [1, 2, 3]
my_list2 = [4, 5, 6]
my_list3 = my_list1 + my_list2 # 用加号连接两个列表
print(my_list3) # [1, 2, 3, 4, 5, 6]
my_list1.extend(my_list2) # 用extend()方法将一个列表添加到另一个列表的末尾
print(my_list1) # [1, 2, 3, 4, 5, 6]

```

<br>

---

### 元组(tuple)

> 是一种有序的、不可变的数据结构，可以存储任意类型的数据，并且可以通过索引来访问其中的元素。元组的创建方法是用圆括号（()）把元素用逗号隔开，或者用tuple()函数把一个可迭代对象转换为元组。元组的常用操作有访问、切片、合并等。由于元组是不可变的，所以不能对元组中的元素进行添加、删除或修改

<br>

---

Python:

```python

# 创建一个元组
my_tuple = (1, 2, 3, "hello", True)
print(my_tuple) # (1, 2, 3, 'hello', True)

# 访问元组中的元素
print(my_tuple[0]) # 1
print(my_tuple[-1]) # True

# 切片元组
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[1:3]) # 返回元组中索引1到2的元素，不包括3，即(2, 3)
print(my_tuple[:3]) # 返回元组中索引0到2的元素，不包括3，即(1, 2, 3)
print(my_tuple[3:]) # 返回元组中索引3到最后的元素，即(4, 5)
print(my_tuple[::2]) # 返回元组中每隔一个元素的元素，即(1, 3, 5)

# 合并元组
my_tuple1 = (1, 2, 3)
my_tuple2 = (4, 5, 6)
my_tuple3 = my_tuple1 + my_tuple2 # 用加号连接两个元组
print(my_tuple3) # (1, 2, 3, 4, 5, 6)

```
<br>

---

### 字典(dict)

>是一种无序的、可变的数据结构，可以存储键值对（key-value pair）的数据，并且可以通过键来访问和修改其中的值。字典的创建方法是用花括号（{}）把键值对用逗号隔开，或者用dict()函数把一个可迭代对象转换为字典。字典的常用操作有添加、删除、修改、获取、遍历等。字典的键必须是可哈希的，即不可变的类型，如整数、字符串、元组等，而字典的值可以是任意类型的数据

<br>

---

Python:

```python

# 创建一个字典
my_dict = {"name": "Alice", "age": 18, "gender": "female"}
print(my_dict) # {'name': 'Alice', 'age': 18, 'gender': 'female'}

# 访问字典中的值
print(my_dict["name"]) # Alice
print(my_dict.get("age")) # 18

# 修改字典中的值
my_dict["name"] = "Bob"
print(my_dict) # {'name': 'Bob', 'age': 18, 'gender': 'female'}

# 添加键值对到字典
my_dict["hobby"] = "reading"
print(my_dict) # {'name': 'Bob', 'age': 18, 'gender': 'female', 'hobby': 'reading'}

# 删除字典中的键值对
my_dict.pop("hobby") # 返回并删除指定键的值
print(my_dict) # {'name': 'Bob', 'age': 18, 'gender': 'female'}
my_dict.popitem() # 返回并删除最后一个键值对
print(my_dict) # {'name': 'Bob', 'age': 18}
del my_dict["name"] # 删除指定键的键值对
print(my_dict) # {'age': 18}

# 遍历字典
my_dict = {"name": "Alice", "age": 18, "gender": "female"}
for key in my_dict: # 遍历字典中的键
    print(key) # name age gender
for value in my_dict.values(): # 遍历字典中的值
    print(value) # Alice 18 female
for key, value in my_dict.items(): # 遍历字典中的键值对
    print(key, value) # name Alice age 18 gender female

```

<br>

---

### 集合(set)

>是一种无序的、可变的数据结构，可以存储不重复的任意类型的数据，并且可以进行集合运算，如并集、交集、差集、对称差等。集合的创建方法是用花括号（{}）把元素用逗号隔开，或者用set()函数把一个可迭代对象转换为集合。集合的常用操作有添加、删除、获取、遍历等。由于集合是无序的，所以不能通过索引来访问其中的元素

<br>

---

Python:
```python

# 创建一个集合
my_set = {1, 2, 3, "hello", True}
print(my_set) # {1, 2, 3, 'hello'}

# 添加元素到集合
my_set.add(4)
print(my_set) # {1, 2, 3, 4, 'hello'}

# 删除集合中的元素
my_set.discard(3) # 删除指定元素，如果不存在则不报错
print(my_set) # {1, 2, 4, 'hello'}
my_set.remove(2) # 删除指定元素，如果不存在则报错
print(my_set) # {1, 4, 'hello'}
my_set.pop() # 返回并删除一个随机元素
print(my_set) # {4, 'hello'}

# 遍历集合
my_set = {1, 2, 3, "hello", True}
for item in my_set: # 遍历集合中的元素
    print(item) # 1 2 3 hello

# 集合运算
my_set1 = {1, 2, 3, 4}
my_set2 = {3, 4, 5, 6}
print(my_set1 | my_set2) # 返回两个集合的并集，即{1, 2, 3, 4, 5, 6}
print(my_set1 & my_set2) # 返回两个集合的交集，即{3, 4}
print(my_set1 - my_set2) # 返回两个集合的差集，即{1, 2}
print(my_set1 ^ my_set2) # 返回两个集合的对称差，即{1, 2, 5, 6}

```

<br>

---

### 冻结集合

>是一种无序的、不可变的数据结构，可以存储不重复的任意类型的数据，并且可以进行集合运算，如并集、交集、差集、对称差等。冻结集合的创建方法是用frozenset()函数把一个可迭代对象转换为冻结集合。冻结集合的常用操作有访问、获取、遍历等。由于冻结集合是不可变的，所以不能对冻结集合中的元素进行添加、删除或修改

<br>

---

Python:
```python

# 创建一个冻结集合
my_frozenset = frozenset([1, 2, 3, "hello", True])
print(my_frozenset) # frozenset({1, 2, 3, 'hello'})

# 访问冻结集合中的元素
print(1 in my_frozenset) # True
print(4 in my_frozenset) # False

# 遍历冻结集合
my_frozenset = frozenset([1, 2, 3, "hello", True])
for item in my_frozenset: # 遍历冻结集合中的元素
    print(item) # 1 2 3 hello

# 集合运算
my_frozenset1 = frozenset([1, 2, 3, 4])
my_frozenset2 = frozenset([3, 4, 5, 6])
print(my_frozenset1 | my_frozenset2) # 返回两个冻结集合的并集，即frozenset({1, 2, 3, 4, 5, 6})
print(my_frozenset1 & my_frozenset2) # 返回两个冻结集合的交集，即frozenset({3, 4})
print(my_frozenset1 - my_frozenset2) # 返回两个冻结集合的差集，即frozenset({1, 2})
print(my_frozenset1 ^ my_frozenset2) # 返回两个冻结集合的对称差，即frozenset({1, 2, 5, 6})

```

<br>

---


### 栈(stack)

>是一种后进先出（LIFO）的数据结构，也就是说，最后添加的元素会最先被移除。栈的常用操作有压栈（push）和弹栈（pop），分别表示在栈顶添加和移除元素。栈可以用Python的列表来实现，利用列表的append()和pop()方法

<br>

---

Python:
```python

# 创建一个空栈
my_stack = []
print(my_stack) # []

# 压栈
my_stack.append(1)
my_stack.append(2)
my_stack.append(3)
print(my_stack) # [1, 2, 3]

# 弹栈
my_stack.pop() # 返回并移除栈顶元素
print(my_stack) # [1, 2]
my_stack.pop() # 返回并移除栈顶元素
print(my_stack) # [1]

```

<br>

---

### 堆(heap)

>是一种特殊的树形数据结构，它满足堆的性质，即每个节点的值都不大于（或不小于）其子节点的值。堆可以用来实现优先队列（priority queue），也就是说，每次从堆中取出的元素都是最小（或最大）的。堆的常用操作有插入（insert）和删除最小（或最大）元素（delete min/max）。Python的标准库中有一个heapq模块，可以用来操作堆

<br>

---

Python:
```python

# 导入heapq模块
import heapq

# 创建一个空堆
my_heap = []
print(my_heap) # []

# 插入元素
heapq.heappush(my_heap, 1) # 在堆中插入一个元素
heapq.heappush(my_heap, 2)
heapq.heappush(my_heap, 3)
print(my_heap) # [1, 2, 3]

# 删除最小元素
heapq.heappop(my_heap) # 返回并删除堆中最小的元素
print(my_heap) # [2, 3]
heapq.heappop(my_heap) # 返回并删除堆中最小的元素
print(my_heap) # [3]

```

<br>

---


### 队列(queue)

>是一种先进先出（FIFO）的数据结构，也就是说，最先添加的元素会最先被移除。队列的常用操作有入队（enqueue）和出队（dequeue），分别表示在队尾添加和在队首移除元素。队列可以用Python的collections模块中的deque类来实现，利用deque的append()和popleft()方法。

<br>

---

Python:
```python

# 导入collections模块
import collections

# 创建一个空队列
my_queue = collections.deque()
print(my_queue) # deque([])

# 入队
my_queue.append(1) # 在队尾添加一个元素
my_queue.append(2)
my_queue.append(3)
print(my_queue) # deque([1, 2, 3])

# 出队
my_queue.popleft() # 返回并删除队首元素
print(my_queue) # deque([2, 3])
my_queue.popleft() # 返回并删除队首元素
print(my_queue) # deque([3])

```

<br>

---


## lambda表达式

>lambda表达式是一种创建匿名函数的简洁方式，它可以用来表示一些简单的表达式，而不需要定义一个完整的函数。lambda表达式的语法如下：

`lambda 参数列表: 表达式`

<br>
    
>lambda是一个关键字，用来表示创建一个匿名函数。参数列表是一个可选的部分，可以有一个或多个参数，也可以没有参数。表达式是一个单行的代码，用来返回一个值。注意，lambda表达式不需要return语句，它会自动返回表达式的结果。下面我会用一些代码例子和运行结果来展示lambda表达式的用法。

<br>

---

### 创建和调用lambda表达式

>我们可以直接在代码中创建和调用一个lambda表达式，也可以将它赋值给一个变量，然后再调用它

Python:
```python

# 直接创建和调用一个lambda表达式，计算两个数的和
print((lambda x, y: x + y)(3, 4)) # 7

# 将一个lambda表达式赋值给一个变量，计算一个数的平方
square = lambda x: x ** 2
print(square(5)) # 25

```

<br>

---

### 使用lambda表达式作为函数的参数

>我们可以使用lambda表达式作为一些内置函数或自定义函数的参数，这样可以简化代码的编写


Python:
```python

# 使用lambda表达式作为sorted函数的参数，按照字符串的长度排序
my_list = ["apple", "banana", "cherry", "orange"]
my_list = sorted(my_list, key=lambda x: len(x))
print(my_list) # ['apple', 'banana', 'cherry', 'orange']

# 使用lambda表达式作为map函数的参数，对列表中的每个元素进行操作
my_list = [1, 2, 3, 4, 5]
my_list = list(map(lambda x: x * 2, my_list))
print(my_list) # [2, 4, 6, 8, 10]

# 使用lambda表达式作为filter函数的参数，筛选出列表中的偶数
my_list = [1, 2, 3, 4, 5]
my_list = list(filter(lambda x: x % 2 == 0, my_list))
print(my_list) # [2, 4]

```

<br>

---

### 使用lambda表达式实现闭包

>我们可以使用lambda表达式实现闭包，也就是在一个函数中返回另一个函数。这样可以保留外部函数的局部变量，使得内部函数可以访问它们

Python:
```python

# 使用lambda表达式实现闭包，返回一个计数器函数
def make_counter():
    count = 0 # 外部函数的局部变量
    return lambda: count + 1 # 内部函数，可以访问count

counter = make_counter() # 创建一个计数器函数
print(counter()) # 1
print(counter()) # 2
print(counter()) # 3

```

<br>

---


## 迭代器(Iterator)

>Iterator是一种可以被迭代的对象，也就是说，它可以按照一定的顺序返回其中的元素
>>iter()是一个内置函数，可以用来从一个可迭代的对象（如列表、元组、字符串等）创建一个Iterator对象
>>
>>next()是一个内置函数，可以用来获取Iterator对象的下一个元素。如果Iterator对象已经没有更多的元素，next()会抛出StopIteration异常

<br>

---

### 创建Iterator对象

>我们可以使用iter()函数来从一个可迭代的对象创建一个Iterator对象

<br>

Python:

```python

# 创建一个列表
my_list = [1, 2, 3, 4, 5]
# 使用iter()函数从列表创建一个Iterator对象
my_iter = iter(my_list)
# 打印Iterator对象的类型
print(type(my_iter)) # <class 'list_iterator'>

```

<br>

---

### 获取Iterator对象的元素

>我们可以使用next()函数来获取Iterator对象的下一个元素。每次调用next()函数，Iterator对象都会记录当前的位置，并返回下一个元素。如果Iterator对象已经没有更多的元素，next()函数会抛出StopIteration异常

<br>
Python:

```python

# 创建一个列表
my_list = [1, 2, 3, 4, 5]
# 使用iter()函数从列表创建一个Iterator对象
my_iter = iter(my_list)
# 使用next()函数获取Iterator对象的下一个元素
print(next(my_iter)) # 1
print(next(my_iter)) # 2
print(next(my_iter)) # 3
print(next(my_iter)) # 4
print(next(my_iter)) # 5
# 再次使用next()函数，抛出StopIteration异常
print(next(my_iter)) # StopIteration

```
<br>

---


### 遍历Iterator对象

>我们可以使用for循环来遍历Iterator对象的所有元素，直到遇到StopIteration异常为止。for循环会自动处理StopIteration异常，所以我们不需要显式地调用next()函数。

<br>

Python:
```python
# 创建一个列表
my_list = [1, 2, 3, 4, 5]
# 使用iter()函数从列表创建一个Iterator对象
my_iter = iter(my_list)
# 使用for循环遍历Iterator对象的所有元素
for item in my_iter:
    print(item) # 1 2 3 4 5
```

<br>

---

### 自定义Iterator对象

>我们也可以自定义一个类来实现Iterator对象，只需要实现两个特殊的方法：iter()和__next__()。iter()方法返回Iterator对象本身，如果需要的话，可以进行一些初始化操作。next()方法返回Iterator对象的下一个元素，如果没有更多的元素，就抛出StopIteration异常。例如，我们可以自定义一个类来实现一个斐波那契数列的Iterator对象，

<br>

Python:
```python
# 定义一个类来实现一个斐波那契数列的Iterator对象
class Fibonacci:
    """Class to implement an iterator of powers of two"""
    def __init__(self, max=0):
        self.max = max # 设置最大值
        self.a = 0 # 初始化第一个数
        self.b = 1 # 初始化第二个数

    def __iter__(self):
        return self # 返回Iterator对象本身

    def __next__(self):
        if self.a > self.max: # 如果超过最大值，抛出StopIteration异常
            raise StopIteration
        else: # 否则，返回下一个斐波那契数
            result = self.a # 保存当前的数
            self.a, self.b = self.b, self.a + self.b # 更新下一个数和下下一个数
            return result # 返回当前的数

# 创建一个斐波那契数列的Iterator对象，最大值为10
fib = Fibonacci(10)
# 使用for循环遍历Iterator对象的所有元素
for num in fib:
    print(num) # 0 1 1 2 3 5 8
```


### filter

> filter是一个内置函数，可以用来从一个可迭代的对象中筛选出满足一定条件的元素，并返回一个新的可迭代的对象。filter的语法如下：
>
> `filter(函数, 可迭代对象)`

>filter的第一个参数是一个函数，它接受一个参数，并返回一个布尔值。这个函数用来判断每个元素是否符合筛选的条件。
>
>filter的第二个参数是一个可迭代的对象，如列表、元组、字符串等。
>
>filter会遍历这个可迭代的对象，对每个元素调用第一个参数的函数，如果函数返回True，就保留这个元素，否则就丢弃这个元素。
>
>filter的返回值是一个filter对象，它也是一个可迭代的对象，可以用list()或其他方法转换为具体的数据类型。

<br>

---

#### 使用自定义函数作为filter的参数

> 我们可以使用自定义函数作为filter的参数，来实现一些复杂的筛选逻辑。例如，我们可以定义一个函数来判断一个数是否是偶数，然后用filter来筛选出一个列表中的所有偶数。

<br>

Python:
```python

# 定义一个函数，判断一个数是否是偶数
def is_even(x):
    return x % 2 == 0

# 创建一个列表
my_list = [1, 2, 3, 4, 5, 6]
# 使用filter和自定义函数，筛选出列表中的偶数
filtered_list = filter(is_even, my_list)
# 将filter对象转换为列表
filtered_list = list(filtered_list)
# 打印筛选后的列表
print(filtered_list) # [2, 4, 6]

```

<br>

---

#### 使用lambda表达式作为filter的参数

> 我们也可以使用lambda表达式作为filter的参数，来实现一些简单的筛选逻辑。lambda表达式是一种匿名函数，可以用来表示一些简单的表达式，而不需要定义一个完整的函数。
>
>(回顾)lambda是一个关键字，用来表示创建一个匿名函数。
>
>参数列表是一个可选的部分，可以有一个或多个参数，也可以没有参数。
>
>表达式是一个单行的代码，用来返回一个值。注意，lambda表达式不需要return语句，它会自动返回表达式的结果。
>
>例如，我们可以使用lambda表达式来判断一个字符串是否以字母a开头，然后用filter来筛选出一个列表中的所有以a开头的字符串。

<br>

---

Python:
```python
# 创建一个列表
my_list = ["apple", "banana", "cherry", "orange"]
# 使用filter和lambda表达式，筛选出列表中以a开头的字符串
filtered_list = filter(lambda x: x.startswith("a"), my_list)
# 将filter对象转换为列表
filtered_list = list(filtered_list)
# 打印筛选后的列表
print(filtered_list) # ["apple"]
```

<br>

---

#### 使用None作为filter的参数

> 我们还可以使用None作为filter的参数，来实现一些特殊的筛选逻辑。当filter的第一个参数是None时，它会默认使用bool()函数来判断每个元素是否为真值，也就是说，它会筛选出所有非空、非零、非False的元素。例如，我们可以使用None来筛选出一个列表中的所有非空字符串。

<br>

---

Python:
```python
# 创建一个列表
my_list = ["apple", "", "banana", "", "cherry", ""]
# 使用filter和None，筛选出列表中的非空字符串
filtered_list = filter(None, my_list)
# 将filter对象转换为列表
filtered_list = list(filtered_list)
# 打印筛选后的列表
print(filtered_list) # ["apple", "banana", "cherry"]

```

<br>

---


### map

>map是一个内置函数，可以用来对一个可迭代的对象中的每个元素应用一个函数，并返回一个新的可迭代的对象。map的语法如下：
>
> `map(函数, 可迭代对象)`

>map的第一个参数是一个函数，它接受一个参数，并返回一个值。这个函数用来定义对每个元素的操作。
>
>map的第二个参数是一个可迭代的对象，如列表、元组、字符串等。
>
>map会遍历这个可迭代的对象，对每个元素调用第一个参数的函数，并将结果放入一个新的可迭代的对象中。
>
>map的返回值是一个map对象，它也是一个可迭代的对象，可以用list()或其他方法转换为具体的数据类型。

<br>

---

#### 使用自定义函数作为map的参数

>我们可以使用自定义函数作为map的参数，来实现一些复杂的操作。例如，我们可以定义一个函数来计算一个数的平方，然后用map来对一个列表中的每个数求平方。

<br>

Python:
```python
# 定义一个函数，计算一个数的平方
def square(x):
    return x ** 2

# 创建一个列表
my_list = [1, 2, 3, 4, 5]
# 使用map和自定义函数，对列表中的每个数求平方
squared_list = map(square, my_list)
# 将map对象转换为列表
squared_list = list(squared_list)
# 打印转换后的列表
print(squared_list) # [1, 4, 9, 16, 25]
```

<br>

---

#### 使用lambda表达式作为map的参数

>我们也可以使用lambda表达式作为map的参数，来实现一些简单的操作。lambda表达式是一种匿名函数，可以用来表示一些简单的表达式，而不需要定义一个完整的函数。lambda表达式的语法如下：
>
> `lambda 参数列表: 表达式`

> lambda是一个关键字，用来表示创建一个匿名函数。参数列表是一个可选的部分，可以有一个或多个参数，也可以没有参数。表达式是一个单行的代码，用来返回一个值。注意，lambda表达式不需要return语句，它会自动返回表达式的结果。例如，我们可以使用lambda表达式来计算一个数的立方，然后用map来对一个列表中的每个数求立方。

<br>

---

Python:
```python
# 创建一个列表
my_list = [1, 2, 3, 4, 5]
# 使用map和lambda表达式，对列表中的每个数求立方
cubed_list = map(lambda x: x ** 3, my_list)
# 将map对象转换为列表
cubed_list = list(cubed_list)
# 打印转换后的列表
print(cubed_list) # [1, 8, 27, 64, 125]
```

<br>

---

#### 使用内置函数作为map的参数

> 我们还可以使用内置函数作为map的参数，来实现一些常见的操作。例如，我们可以使用str()函数来将一个列表中的每个数转换为字符串，然后用map来对一个列表中的每个数进行转换。

<br>

Python:
```python
# 创建一个列表
my_list = [1, 2, 3, 4, 5]
# 使用map和str()函数，对列表中的每个数转换为字符串
string_list = map(str, my_list)
# 将map对象转换为列表
string_list = list(string_list)
# 打印转换后的列表
print(string_list) # ['1', '2', '3', '4', '5']
```

<br>

---


### reduce

>reduce是一个内置函数，可以用来对一个可迭代的对象中的所有元素应用一个函数，并将结果累积为一个单一的值。reduce的语法如下：
>
> `reduce(函数, 可迭代对象, 初始值)`

> reduce的第一个参数是一个函数，它接受两个参数，并返回一个值。这个函数用来定义对两个元素的操作。
>
>reduce的第二个参数是一个可迭代的对象，如列表、元组、字符串等。reduce会从左到右遍历这个可迭代的对象，对每两个元素调用第一个参数的函数，并将结果作为下一次调用的第一个参数。>
>
>reduce的第三个参数是一个可选的初始值，它会作为第一次调用的第一个参数。如果可迭代对象为空，且没有提供初始值，reduce会抛出TypeError异常。
>
>reduce的返回值是一个单一的值，它是最后一次调用函数的结果。

<br>

---

#### 使用自定义函数作为reduce的参数

>我们可以使用自定义函数作为reduce的参数，来实现一些复杂的操作。例如，我们可以定义一个函数来计算两个数的最大公约数，然后用reduce来计算一个列表中所有数的最大公约数。

Python:
```python
# 定义一个函数，计算两个数的最大公约数
def gcd(x, y):
    # 使用辗转相除法
    while y != 0:
        x, y = y, x % y
    return x

# 创建一个列表
my_list = [12, 18, 24, 30]
# 使用reduce和自定义函数，计算列表中所有数的最大公约数
result = reduce(gcd, my_list)
# 打印结果
print(result) # 6

```

<br>

---

#### 使用lambda表达式作为reduce的参数

>我们也可以使用lambda表达式作为reduce的参数，来实现一些简单的操作。lambda表达式是一种匿名函数，可以用来表示一些简单的表达式，而不需要定义一个完整的函数。

>lambda是一个关键字，用来表示创建一个匿名函数。参数列表是一个可选的部分，可以有一个或多个参数，也可以没有参数。表达式是一个单行的代码，用来返回一个值。注意，lambda表达式不需要return语句，它会自动返回表达式的结果。例如，我们可以使用lambda表达式来计算两个数的和，然后用reduce来计算一个列表中所有数的和。

<br>

Python:
```python
# 创建一个列表
my_list = [1, 2, 3, 4, 5]
# 使用reduce和lambda表达式，计算列表中所有数的和
result = reduce(lambda x, y: x + y, my_list)
# 打印结果
print(result) # 15

```

<br>

---

#### 使用内置函数作为reduce的参数

> 我们还可以使用内置函数作为reduce的参数，来实现一些常见的操作。例如，我们可以使用max()函数来找出一个列表中的最大值，然后用reduce来实现这个功能。

Python:
```python
# 创建一个列表
my_list = [1, 2, 3, 4, 5]
# 使用reduce和max()函数，找出列表中的最大值
result = reduce(max, my_list)
# 打印结果
print(result) # 5
```

<br>

---

#### 使用初始值作为reduce的参数

> 我们还可以使用初始值作为reduce的参数，来改变reduce的行为。初始值会作为第一次调用函数的第一个参数，而可迭代对象的第一个元素会作为第二个参数。这样可以避免可迭代对象为空时的异常，或者实现一些特殊的功能。例如，我们可以使用初始值为1来计算一个列表中所有数的乘积，即使列表为空。

Python:
```python
# 创建一个列表
my_list = [1, 2, 3, 4, 5]
# 使用reduce和lambda表达式，计算列表中所有数的乘积，初始值为1
result = reduce(lambda x, y: x * y, my_list, 1)
# 打印结果
print(result) # 120
```



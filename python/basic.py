# 1.标准数据类型
# Number(数字)
def fun1():
    a = 1
    b = 1.11
    c = True
    d = 4 + 3j
    # 支持int float bool complex(复数)
    print(type(a), type(b), type(c), type(d))
    print(isinstance(a, int))


# String(字符串)
def fun2():
    a = 'python'
    # 截取
    print(a[0:])

    # 转义
    print('py\nthon', r'py\nthon')

    # 连接
    print(a + 'test')

    # 返回字符串长度
    print(len(a))

    # 查找
    print(a.find('n'))

    # 替换
    print(a.replace('python', 'hello'))

    # 分割
    print(a.split('h'))


# List(列表)
def fun3():
    a = ['python', 1, True, 11.9]
    b = [1, 2, 3]
    # 连接
    print(a + b)

    # 删
    del a[2]
    print(a)

    # 改
    a[0] = 'hello'
    print(a)

    # 截取
    print(a[0:])

    # 返回个数，最大值，最小值
    print(len(a), max(b), min(b))

    # 在列表末尾添加新的对象
    a.append(1)
    print(a)

    # 统计某个元素在列表中出现的次数
    print(a.count(11.9))

    # 在列表末尾一次性追加另一个序列中的多个值
    b.extend([4, 5, 6])
    print(b)

    # 从列表中找出某个值第一个匹配项的索引位置
    print(a.index('hello'))

    # 插入列表
    a.insert(1, 'python')
    print(a)

    # 移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
    a.pop(-1)
    print(a)

    # 移除列表中某个值的第一个匹配项
    a.remove('hello')
    print(a)

    # 反向列表中元素
    a.reverse()
    print(a)

    # 对原列表进行排序
    b.sort(reverse=True)
    print(b)


# Tuple(元组)
def fun4():
    a = ('java', 'python', 'c')
    b = 1, 2, 3, 4, 5
    print(a, b)


# Dictionary(字典)
def fun5():
    a = {'a': 1, 'b': 2, 'c': 3}
    # 增
    a.update({'d': '4'})
    print(a)

    # 删
    del a['a']
    print(a)

    # 改
    a['b'] = 1
    print(a)

    # 查
    print(a['b'])

    # 返回指定键的值，如果键不在字典中返回default设置的默认值
    print(a.get('c'))

    # 删除字典给定键key所对应的值，返回值为被删除的值
    print(a.pop('d'))


# set(集合)
# 无序的不重复元素序列
def fun6():
    a = {'apple', 'banana', 'cherry'}
    b = {'google', 'runoob', 'apple'}
    # 增
    a.add('orange')
    a.update(b)
    print(a)

    # 删
    a.remove('orange')
    print(a)

    # 元素包含在集合a但不在集合b
    print(a.difference(b))

    # 移除两个集合都包含的元素
    a.difference_update(b)
    print(a)

    # 元素既包含在集合a又包含在集合b中
    print(a.intersection(b))

    # 移除a集合中不存在于b集合中的元素
    print(a.intersection_update(b))

    # 判断集合a中是否有包含集合b的元素
    print(a.isdisjoint(b))

    # 判断集合a的所有元素是否都包含在集合b中
    print(a.issubset(b))

    # 判断指定集合a的所有元素是否都包含在集合b中,集合b的所有元素也包含在集合a中
    print(a.issuperset(b))


# 循环语句
def fun7():
    a = 0
    while a < 5:
        print(a, '小于5')
        a = a + 1
    else:
        print(a, '大于或等于 5')

    # 在字典中遍历时，关键字和对应的值可以使用items()方法同时解读出来
    b = {'a': 1, 'b': 2, 'c': 3}
    for x, y in b.items():
        print(x, y)

    # 同时遍历两个或更多的序列，可以使用zip()组合
    c = ['a', 'b', 'c']
    d = ['d', 'e', 'f']
    for x, y in zip(c, d):
        print('{0}{1}'.format(x, y))

    # 反向遍历一个序列
    for i in reversed(range(1, 10)):
        print(i)

    # 按顺序遍历一个序列，使用sorted()函数返回一个已排序的序列，并不修改原值
    e = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
    for x in sorted(set(e)):
        print(x)


# 迭代器
def fun8():
    a = ['apple', 'banana', 'cherry']
    b = iter(a)
    print(next(b))
    print(next(b))
    for x in b:
        print(x)


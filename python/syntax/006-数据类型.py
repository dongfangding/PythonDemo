"""
演示python中数据类型的基本使用
"""


def main():
    string()
    my_list()
    my_tuple()
    my_set()
    my_dict()
    pass


"""
基本类型
    1. 整型，所有的整型都使用int来表示， 在python3以后long不再继续存在
    2. 浮点数
    3. 字符串与字节
    4. 布尔值 True False 注意大小写
    5. 空    空使用None来标识
"""


"""
字符串的基本使用
1. 创建 使用''引号包括
2. 访问 使用[0]角标访问
3. 切片 [:::]
4. 单个字符与整型的转换
5. 字符串与字节之间的转换
"""


def string():
    print('=====================================字符串================================================')
    # 字符串字面值可以跨行连续输入。一种方式是用三重引号："""...""" 或 '''...'''。
    # 字符串中的回车换行会自动包含到字符串中，如果不想包含，在行尾添加一个 \ 即可。如下例:
    print("""\
        Usage: thingy [OPTIONS]
            -h              Display this usage message
            -H hostname 	Hostname to connect to		
    """)

    # 字符串太长可以使用''，引号相连的字符串将会自动连接在一起
    print('我这一行源码部分占据的长度太长了，我想写到下一行，但是不能影响实际输出还是在同一行，'
          '没事直接用引号接着连起来就可以了')
    print()
    msg = 'hello world!'
    # 可以使用内置函数len直接返回字符串的长度
    length = len(msg)
    print('%s的长度是: %d' % (msg, length))
    # 使用下标可以直接访问字符串，下标从0开始
    print('%s的第1个字符是: %s, 最后一个字符是: %s' % (msg, msg[0], msg[length - 1]))

    # 也可以从后往前数，-0 和 0 是一样的，所以负数索引从 -1 开始。
    print('%s的倒数第一个字符是: %s, 倒数第五个字符是: %s，倒数最后一个字符是: %s' % (msg, msg[-1], msg[-5], msg[-length]))

    # 切片
    # 从0切到2，0包括在内，切片的结尾2不包括在内
    print()
    print(msg)
    print('0:2 === ', msg[0:2])
    print('2:5 === ', msg[2:5])
    # 开始位置如果不指定默认为0
    print('0:5 === ', msg[:5])
    # 结束位置不指定，默认为字符串结束
    print("2:最后 ==== ", msg[2:])
    # 也可以支持负数索引，从倒数第二个切到最后
    print("-2：最后 ==== ", msg[-2:])
    # 开可以指定切片的步长,没两个切分一次
    print("0:最后，没隔两个切一次: ", msg[::2])
    # 从最后往前切，每1个切一次
    print("从最后往前切，每1个切一次", msg[::-1])

    print()
    # ord()函数获取字符的整数
    print('A字符对应的整型数字是: ', ord('A'))
    # chr()函数把编码转换为对应的字符
    print('整数66对应的字符是: ', chr(66))

    print()
    # 定义一个bytes类型的变量，使用b标识
    bytes_word = b'abc'
    print(bytes_word)
    chinese_world = "我是中国人"
    bytes_word = chinese_world.encode("utf-8")
    print('%s转换为UTF-8编码的字节为： %s' % (chinese_world, bytes_word))
    chinese_world = bytes_word.decode("utf-8")
    print("将%s转换为UTF-8的字符串为: %s" % (bytes_word, chinese_world))

    print('=====================================字符串================================================')


"""
列表的使用， 有序且元素内容可更改
1. 定义 使用[]包括，元素之间用,隔开
2. 访问 使用[索引]访问
3. 修改 + 或append 或[索引] = 新值 || del || remove
4. 作为栈使用
5. 切片 [:::]
6. 常用方法 append | insert | remove | pop | clear | index| count | sort | reverse | copy
7. 循环的技巧
"""


def my_list():
    print()
    print('=======================================列表==============================================')
    # 定义
    numbers = [1, 3, 5, 7, 9]
    print(numbers, ',长度为: ', len(numbers))
    print("访问列表第一个元素: ", numbers[0])

    # 连接列表
    numbers += [11, 13]
    print("连接后新列表: ", numbers)

    # 修改指定位置的列表
    numbers[0] = 0
    print("将列表第一个元素改为0, ", numbers)

    # 通过方法在列表末尾添加元素
    numbers.append(15)
    numbers.append(17)
    print("使用append添加元素后: ", numbers)
    # 调用insert可以在指定位置插入元素，而且list中可以包含任意类型的数据，再包含一个list
    numbers.insert(1, [100, 200, 300])
    print('在[1]位置插入新的列表之后: ', numbers)
    print()

    # 删除第一个符合该元素位置的数据
    numbers.append(17)
    print("删除17前: ", numbers)
    numbers.remove(17)
    print("删除17后: ", numbers)
    # 根据索引删除, 删除列表的最后一个元素
    del numbers[(len(numbers) - 1)]
    print("删除最后一个元素后: ", numbers)

    # 也可以直接弹出元素末尾的元素,这一特性使得列表可以作为栈来使用
    print('弹出末尾元素: ', numbers.pop())
    # 当然也可以弹出指定位置
    print('弹出指定位置元素: ', numbers.pop(1))
    print("剩余列表元素: ", numbers)
    # 清空列表
    numbers.clear()
    print("使用clear清空列表: ", numbers)
    print()

    # 切片
    numbers = [1, 3, 5, 7, 9]
    numbers1 = numbers[0:4]
    print("切片后0:4", numbers1)
    print("切片后0:4,每两个切一次", numbers[0:4:2])
    # 可以通过切片的方式重新赋值，截取三个位置，然后使用三个值进行覆盖
    numbers[0:3] = [-2, -1, 0]
    print(numbers)
    # 甚至可以清空列表
    numbers[:] = []
    print("使用切片清空列表: ", numbers)

    # 常用方法测试
    numbers2 = [0, 0, 2, 2, 5, 6, 7]
    numbers3 = numbers2.copy()
    numbers3.append(9)
    print(numbers3)
    print("0是否在列表中存在: ", numbers3.index(0))
    print("0在列表中出现的次数是: ", numbers3.count(0))
    # 翻转列表
    numbers3.reverse()
    print("翻转后列表元素: ", numbers3)

    print('=======================================列表==============================================')
    print()


"""
元组，可以看做列表的特殊形式，只是元素内容不可更改；用在数据内容不可变的情景下，可防止程序操作不当
1. 定义 使用()包括，多个元素之间用,隔开
2. 访问方法与列表相同
3. 与列表之间的互相转换
4. 循环的技巧
"""


def my_tuple():
    print('=======================================元组==============================================')
    tuple1 = ('jack', 'michal', 'jane', 'sine')
    print(tuple1)
    print(tuple1[0])
    # 如下是不允许的操作
    # tuple1[0] = 'jack1'
    # 将元组转换为列表
    list1 = list(tuple1)
    list1[0] = 'jack1'
    print(list1)
    print(tuple1)
    print('=======================================元组==============================================')
    print()


"""
set 对象是由具有唯一性的 hashable 对象所组成的无序多项集。 常见的用途包括成员检测、从序列中去除重复项以及数学中的集合类计算，例如交集、并集、差集与对称差集等等。 
1. 定义 使用{}标识
2. 更新、元素判断与存取
3. 集合计算 交集、并集、差集与对称差集
4. 子集与超集
5. 循环的技巧
"""


def my_set():
    print('=======================================集合==============================================')
    set1 = {1, 1, 3, 3, 5, 6, 8, 8}
    # 最终只能添加进去1,3,5,6,7
    print(set1)
    # 添加元素
    set1.add(9)
    # 将列表中的元素添加集合
    set1.update([10, 11])
    print(set1)
    # x in set 判断元素在集合中是否存在
    if 10 in set1:
        # remove如果元素不存在会出错
        set1.remove(10)
    # discard 移除元素，如果元素不存在不会报错
    set1.discard(10)

    # 弹出头部元素
    set1.pop()
    print(set1)
    print()

    set2 = set1.copy()
    set2.update([15, 19, 20])
    print('集合1：', set1)
    print('集合2: ', set2)
    # 计算交集
    print('集合1与集合2交集: ', set1 & set2)
    print('集合1与集合2并集: ', set1 | set2)
    print('集合1与集合2差集: ', set1 - set2)
    print('集合1与集合2对称差集: ', set1 ^ set2)

    print()
    print('集合1：', set1)
    print('集合2: ', set2)
    print("set2是否是set1的超集: ", set2 >= set1)
    print("set1是否是set2的子集", set1 <= set2)
    print('=======================================集合==============================================')
    print()


"""
字典（Dict） 键值对， 字典可以通过将以逗号分隔的 键: 值 对列表包含于花括号之内来创建，
例如: {'jack': 4098, 'sjoerd': 4127} 或 {4098: 'jack', 4127: 'sjoerd'}，也可以通过 dict 构造器来创建。
1. 定义 使用{}包括，键值对之间使用:隔开，两个元素之间使用,隔开
2. 访问与更新
3. 循环的技巧
"""


def my_dict():
    print('=======================================字典==============================================')
    dict1 = {'dongfang.ding': '18356785555', 'ddf': '13155556666'}

    # 循环的技巧,使用items可同时去除键和值
    for k, v in dict1.items():
        print(k, v, end="\t\t")
    print()
    # x in dict 是否存在
    if 'dongfang.ding' in dict1:
        dict1['dongfang.ding'] = '00000000000'
        print('修改dongfang.ding的电话号码: ', dict1)
    print('获取到dongfang.ding的电话号码: ', dict1.get('dongfang.ding'))
    print('可获取的时候指定默认值: ', dict1.get("ddd", '这是个默认值'))

    # 添加元素
    print()
    dict1.update(yichen=110, dy=120)
    print('添加元素: ', dict1)

    # 弹出指定元素，会被删除掉
    print()
    dict1.pop('yichen')
    print('弹出指定元素yichen: ', dict1)
    # 后进先出，弹出元素
    print("后进先出弹出元素: ", dict1.popitem())
    print("后进先出弹出元素: ", dict1.popitem())
    print('剩余元素: ', dict1)

    # 清空元素
    dict1.clear()
    print('清空字典', dict1)
    print('=======================================字典==============================================')
    print()


if __name__ == '__main__':
    main()

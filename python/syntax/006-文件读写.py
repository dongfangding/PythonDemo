#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, json


def main():
    # 如何有java的user.dir属性的效果？
    root_dir = os.path.dirname(os.path.dirname(os.getcwd()))
    read_write_file(root_dir + '/file/006-文件读写测试专用.txt', 'r+')
    serial_json(root_dir + '/file/006-文件读写之序列化json.txt')
    pass


"""
第一个参数是包含文件名的字符串。第二个参数是另一个字符串，其中包含一些描述文件使用方式的字符。mode 可以是 'r' ，
表示文件只能读取，'w' 表示只能写入（已存在的同名文件会被删除），还有 'a' 表示打开文件以追加内容；任何写入的数据会自动添加到文件的末尾。'
r+' 表示打开文件进行读写。mode 参数是可选的；省略时默认为 'r'。

在处理文件对象时，最好使用 with 关键字。 优点是当子句体结束后文件会正确关闭，即使在某个时刻引发了异常。
而且使用 with 相比等效的 try-finally 代码块要简短得多:如果你没有使用 with 关键字，那么你应该调用 f.close() 来关闭文件并立即释放它使用的所有系统资源

通常文件是以 text mode 打开的，这意味着从文件中读取或写入字符串时，都会以指定的编码方式进行编码。
如果未指定编码格式，默认值与平台相关 (参见 open())。
在mode 中追加的 'b' 则以 binary mode 打开文件：现在数据是以字节对象的形式进行读写的。这个模式应该用于所有不包含文本的文件。
1. with as 
2. mode
3. read 
4. 转换
5. seek
"""


def read_write_file(path, mode, encoding='utf-8'):
    # 以中文编码读取
    with open(path, mode, encoding=encoding) as file:
        # 读取一行
        print(file.readline())
        print("=========================")
        # read如不指定大小，则是直接读取文件内容全部，如果没有值了就是一个空的字符串,指定大小就是读取10个字符
        print(file.read(10))
        print("=========================")
        # 循环读取一行
        for line in file:
            print(line, end='')
        print("========================")
        # 把文件内容读取到列表中
        list(file)
        # 把文件内容读取到列表中的另一种写法
        file.readlines()
        print(file.read())
        print("=====================")

    # 以字节对象方式读取，不能指定编码
    with open(path, mode + 'b') as file:
        """
        把文件的起始点设置为500个字节，只有字节模式下有效,
        第二个参数from_what有效值 0 从文件其实位置作为参考点， 1 当前位置 2 文件末尾，默认0，可以省略
        """
        file.seek(500, 0)
        file.write('我们都有一个家，名字叫中国'.encode('utf-8'))


"""
将复杂数据类型序列化成json存储到文件中，然后再反序列化回来
"""


def serial_json(path, mode='r+', encoding='utf-8'):
    print("====================json序列化==================")
    # 将复杂的格式dump到text file对象中去,mode='r+'标识以追加的方式往里面写内容，也就是写到最后
    with open(path, mode=mode, encoding=encoding) as file:
        dict1 = {1: 'ali', 2: 'baidu', 3: 'tencent'}
        # 将字典转换为json
        print(json.dumps(dict1))
        # 将字典转换成json并序列化到text file对象中
        json.dump(dict1, file)
    with open(path, mode='r+', encoding=encoding) as file:
        str1 = json.load(file)
        rec_dict = dict(str1)
        print(rec_dict)
        print(rec_dict.popitem())
    print("====================json序列化==================")


if __name__ == '__main__':
    main()

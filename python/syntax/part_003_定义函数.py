#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
在标准文件写法里，其实我们已经看到了定义标准函数的雏形,
使用def来定义函数，空格后紧跟函数名，之后跟一个:
调用的时候函数名+括号
"""


def main():
    print(add(1, 3, 5, 7, 9))
    print(divide())
    print(1, 3, 5)


def add(*args):
    """
    定义一个可变参数的函数
    :param args:
    :return:
    """
    total = 0
    for arg in args:
        total += arg
    return total


def divide(a=0, b=0, c=0):
    """
    定义一个含有默认值的函数，可以直接传参，如果不传使用默认值
    :param a:
    :param b:
    :param c:
    :return:
    """
    return a * b * c


if __name__ == '__main__':
    main()

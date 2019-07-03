#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
类的定义语法,类是对函数和属性的封装，用来描述世间万物的一个具化，比如我要描述一个人，人会有属性，姓名，生日，地址等，人会有各种各样的
方法，比如吃饭，睡觉，打豆豆；而这显然不是前面接触的数据类型所能描述的；所以我们可以定义一个类，用来描述人，包含我们需要的与人相关的各种标签和动作；
标签就是属性，动作就是函数;
1. 定义一个类的表现形式为

# object 为定义该类想要继承哪个类，这牵扯到更高级的特性；一般如果不存在继承关系，写object即可
class ClassName(object):
    # 属性
    name = ''
    age = ''

    # 类有一个特殊的函数，固定写法，可以作为构造类的初始化函数即构造函数，这样初始化ClassName(name, age)即可给类初始化赋值
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 定义函数，类的函数的第一个参数都是self，代表类实例本身，但是调用的时候不需要传入，如果有别的参数，直接传别的参数就可以
    def eat(self, something):
        print('吃', something)


2. 访问权限,python并没有严格意义上的控制属性的私有或者公开，但是可以通过在属性前加两个下划线__，那么在类的外部则无法访问到该属性
"""


class Person(object):
    """
    描述一个人的类
    """
    def __init__(self, name, age):
        """
        __init__ 固定为构造方法，一旦指定构造方法，创建类就必须按照构造方法的参数形式来传递调用
        __name 两个下划线开头，将属性设置为私有，外部不可访问
        :param name:
        :param age:
        """
        print('init class...........')
        self.__name = name
        self.age = age

    def eat(self, something):
        """
        吃东西的方法
        :param something:
        :return:
        """
        print('%s在吃%s' % (self.__name, something))

    def __str__(self):
        """
        类似java的toString()方法，直接打印对象，可以定制打印哪些信息, 如果不定制打印的是类的内存地址
        :return:
        """
        return 'name={0}, age={1}'.format(self.__name, self.age)

    def get_name(self):
        return self.__name


def main():
    # 由于定义了构造函数，因此创建类必须传入对应需要的参数
    p = Person('jack', 15)
    print(p)
    p.eat('fruit')
    # age属性并没有设置为私有，因此外部可以直接通过对象.属性名来访问
    print(p.age)
    # name属性设置了私有，外部无法直接访问。但是类内部对属性进行的封装，提供方法将name返回给调用方
    print(p.get_name())
    # 可以返回类的注释信息
    print(p.__doc__)


if __name__ == '__main__':
    main()


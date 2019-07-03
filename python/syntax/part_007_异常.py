#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
即使语句或表达式在语法上是正确的，但在尝试执行时，它仍可能会引发错误。 在执行时检测到的错误被称为*异常";
异常一旦发生，就会跳出try方法体，如果
异常被捕捉，那么跳出异常处理之后，后面的方法依然会继续执行；而如果不予处理，跳出异常之后，整个程序结束，后面的代码便不再执行；
异常的语法为
try:
    # 包括可能出现异常的方法体，一旦发生异常，便会跳出该方法体
    ....
except 异常类:
    # 出现的异常如果与这里定义用来捕获的异常类匹配，则这里会执行，如果发生的异常是这里用来参与捕获的类的基类，也会被成功捕获；异常可以有多个except，但只会有有一个被执行
    ...
else:
    # 必须放到except后面，如果try方法体内没有发生异常，则这一段会被执行
    ....
finally: # finally 子句 总会在离开 try 语句前被执行，无论是否发生了异常
    ...
"""


def main():
    demo_1()
    print("=======================")
    demo_2()
    print("================================")
    demo_3()


def demo_1():
    try:
        1 / 0
    except Exception as e:
        print(e)
    finally:
        print('虽然发生了异常，但是我还是能执行')


def demo_2():
    try:
        1 / 1
    except Exception as e:
        print(e)
    else:
        print('没有发生异常，我就会执行..')
    finally:
        print('管你有没有异常，我就是要执行')


def demo_3():
    """
    抛出异常
    :return:
    """
    try:
        # raise 紧跟异常类，抛出一个异常
        raise ValueError
    except Exception as e:
        print('我捕获到了异常，但是我还是要把你抛出去, ', e)
        # 如果异常被捕捉到了，还可以选择继续抛出去，也可以不抛出去，但是如果抛出去就可以简写，直接写raise
        raise
    finally:
        print('还是我，谁都不都阻止我的执行。。。')


if __name__ == '__main__':
    main()

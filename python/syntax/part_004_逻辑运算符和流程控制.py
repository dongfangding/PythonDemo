#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random

"""
条件判断的格式为

if else
或者
if elif else
每个语句之后紧跟: 然后另起一行，采用缩进格式编写，具有相同缩进格式的被视为同一个代码体

运算符

运算符	描述
[] [:]	            下标，切片
**	                指数
~ + -	            按位取反, 正负号
* / % //	        乘，除，模，整除
+ -	                加，减
>> <<	            右移，左移
&	                按位与
^ |	                按位异或，按位或
<= < > >=	        小于等于，小于，大于，大于等于
== !=	            等于，不等于
is is not	        身份运算符
in not in	        成员运算符
not or and	        逻辑运算符
= += -= *= /= %= //= **= &= |= ^= >>= <<=	（复合）赋值运算符
"""


def main():
    demo_1()
    demo_2()
    loop()


def demo_1():
    print("=======================运算符===============================")
    print('1 > 2: ', 1 > 2)
    print('1 < 2 并且 3 < 4', 1 < 2 and 3 < 4)
    print('1 < 2 或者 3 > 4', 1 < 2 or 3 > 4)
    # 在python中/的结果是有小数位的
    print('10 / 3 = ', 10 / 3)
    # 如果想要获得整数位的结果则需要//
    print('10 // 3 = ', 10 // 3)
    # 获得余数
    print('10 % 3 = ', 10 % 3)
    print("=======================运算符===============================")
    print()


def demo_2():
    print("=======================条件判断===============================")
    username = input('请输入用户名: ')
    password = input('请输入密码: ')
    if username == 'admin' and password == '123456':
        print('验证成功')
        print('进入系统')
    elif username == 'admin':
        print('密码不正确')
        print('正确密码为: 123456')
    else:
        print('用户名不存在')
        print('正确用户名为: admin')
    print("=======================条件判断===============================")
    print()


def loop():
    """
    循环控制语句

    语句表现形式为
    1. for x in y:
        .....

    2. while(逻辑值):
        ...
    """
    print("=======================循环===============================")
    # 计算从1+2+3+...+100的值
    # range(:::)，第一个参数表示起始值，第二个参数表示终止值（不包含），第三个参数表示步长，默认为1
    count = 0
    for x in range(1, 101):
        count += x
    print('1+2+3+...+100 = ', count)

    # 计算 1+3+5+5+...99，也就是1到100之间的奇数和
    count = 0
    for x in range(1, 101, 2):
        count += x
    print('1+3+5+5+...99 = ', count)
    print()

    count = 3
    # 产生一个1到10之间的随机数
    answer = random.randint(1, 10)
    while count > 0:
        number = int(input('请猜测计算机产生的一个10以内的数'))
        if number > answer:
            print('再小一点')
        elif number < answer:
            print('再大一点')
        else:
            print('猜对了')
            break
        count -= 1
    if count == 0:
        print("告诉你最后的答案吧，这个值是: ", answer)

    print()

    # 寻找水仙花数
    narcissistic_number()

    # 打印图形
    print_pic()

    print("=======================循环===============================")
    print()


"""
打印星号
*
**
***
****
*****

    *
   **
  ***
 ****
*****
"""


def print_pic():
    row = int(input('请输入要生成多少行的三角形: '))
    for x in range(1, row + 1):
        print('*' * x)
    print()

    for x in range(1, row + 1):
        print('%s%s' % (' ' * (row - x), '*' * x))
    print()


"""
水仙花数 编辑 讨论
水仙花数（Narcissistic number）也被称为超完全数字不变数（pluperfect digital invariant, PPDI）、
自恋数、自幂数、阿姆斯壮数或阿姆斯特朗数（Armstrong number），水仙花数是指一个 3 位数，
它的每个位上的数字的 3次幂之和等于它本身（例如：1^3 + 5^3+ 3^3 = 153）。

"""


def narcissistic_number():
    result = []
    # 求1000以内的水仙花数
    for x in range(100, 1000, 1):
        # 获得百位数的个位数
        ge = x % 100 % 10
        # 获得百位数的十位数
        shi = x % 100 // 10
        # 获得百位数的百位数
        bai = int(x / 100)
        if ge * ge * ge + shi * shi * shi + bai * bai * bai == x:
            result.append(x)
    print('找到1000以内的水仙花数: ', result)
    print()
    return result


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from python.oop.part_001_类的定义基本形式 import Person

"""
继承使我们可以复用类，比如前面我们定义了一个类Person,
每个人都有名字，年龄，都会有吃饭的动作，但是有的人就比较牛逼，
他会飞，这种人叫飞人，但不是每个人都是飞人，所以不能把飞的动作放到Person类上，因为这是不合适的，这是个例；
人不一定会飞，但是飞人一定是人，他有人类所共有的特性，那么我们就可以定义一个飞人继承人，那么人所共有的属性和方法就没必要
重新定义一遍了，它会从父类继承所有的属性和函数

"""


class FlyMan(Person):

    def fly(self):
        """
        定义父类不存在的方法，这里可以看到一个问题，子类也无法访问父类的私有属性
        :return:
        """
        print('看%s在飞' % self.get_name())

    def __str__(self):
        return '子类可以复写父类的方法，那么再调用方法的时候就是执行子类自己的方法, {0}'.format(self.__dict__)


def main():
    # 继承了父类的构造方法
    fly_man = FlyMan('刘翔', 35)
    # 子类覆盖了父类的方法，所以这里没有按照父类的方法打印
    print(fly_man)
    # 可以定义父类中不存在的方法，作为子类对父类的扩展
    fly_man.fly()
    # 检查一个实例的类型
    print('isinstance(fly_man, Person): ', isinstance(fly_man, Person))
    # 检查类的继承关系
    print('issubclass(FlyMan, Person): ', issubclass(FlyMan, Person))
    print('issubclass(Person, FlyMan): ', issubclass(Person, FlyMan))


if __name__ == '__main__':
    main()

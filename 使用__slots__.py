#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2017-12-2 13：28
# @Version : $Id$
# @des : 使用slots对添加属性进行限制

class Student(object):
    pass

#给实例绑定一个属性
s=Student()

s.name='Michael'

print(s.name)

#给实例绑定一个方法

def set_age(self,age):
    self.age=age

from types import MethodType      #给实例绑定一个方法

s.setage=MethodType(set_age,s)

s.setage(25)

print(s.age)

class Worker(object):
    __slots__ = ('name','age')         #slots会限制属性，只有添加进tuple的才是能够更改的属性
    pass

class Debuger(Worker):
    __slots__ = ('like','boring')
    pass

if __name__ == '__main__':
    w = Worker()
    d = Debuger()
    w.name = 'alex'
    w.age = 25
    # w.score = 99                       #若声明了slots，且内部不包含score这个属性就会报错，只对当前的实例限制
    d.age=23
    d.name='apple'                      #父类定义的slots属性，子类具有这个属性，但是不会进行限制，这对父类的实例进行限制
    # d.bu='ddd'                          #子类的属性包含父类的slots属性和自身的所有属性,当定义这些属性以外的属性时会报错
    print(w.name)
    print(w.age)
    # print(w.score)
    print(d.age)
    print(d.name)


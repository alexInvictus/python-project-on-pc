#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2017-12-2 13：28
# @Version : $Id$
# @des : 实例属性和类属性

class Student(object):
    name='student'

class Answer(object):
    count=0                    #类属性count  不属于变量赋值。所以不会每次都赋值0来初始化

    def __init__(self,name):
        self.name=name
        Answer.count +=1         #类属性，相当于静态变量。可以改变不会没调用一次类都会重新赋值

s=Student()            #实例化对象S

print(s.name)         #打印实例化的对象s的name属性  所以会继续查找class的name属性

print(Student.name)   #打印出Student类的name类属性

s.name='Michael'       #给实例绑定name属性

print(s.name)          #实例s的name属性更改

print(Student.name)    #类属性name没有变化

del s.name

print(s.name)          #当删除掉实例属性后，实例属性会打印类属性的属性

if __name__ == '__main__':
    # 测试:
    if Answer.count != 0:
        print('测试失败1!')
    else:
        bart = Answer('Bart')
        if Answer.count != 1:
            print(Answer.count)
            print('测试失败2!')
        else:
            lisa = Answer('Bart')
            if Answer.count != 2:
                print('测试失败3!')
            else:
                print('Students:', Answer.count)
                print('测试通过!')
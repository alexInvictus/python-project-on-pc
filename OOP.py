#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2017-12-2 13：28
# @Version : $Id$
# @des : 面向对象编程知识点学习

class Student(object):
    def __init__(self,name,score):    #__开头定义为私有变量   __name不能直接访问
        self.name=name                #__name__为特殊变量，特别变量可以直接访问
        self.score=score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

    def just_Try(self,lis):         #定义在类里面的函数必须包含self位置参数，也可以添加其他位置参数
        print("1123")

    def get_grade(self):
        if(self.score>80):
            return 'A'
        else:
            return 'B'

class Work(object):
    def __init__(self, name, gender):
        self.__name = name
        self.__gender = gender

    def get_gender(self):
        return self.__gender

    def set_gender(self,new_gender):
        self.__gender=new_gender
        return self.__gender

if __name__ == '__main__':
    # 测试forwork:
    bart = Work('Bart', 'male')
    if bart.get_gender() != 'male':
        print('测试失败1!')
    else:
        bart.set_gender('female')
        if bart.get_gender() != 'female':
            print('测试失败2!')
        else:
            print('测试成功!')
#if __name__ == '__main__':
#bart=Student('Bart',78)
#lisa=Student('Lisa',89)
#bart.print_score()
#lisa.print_score()
#bart.just_Try(23)

#print(bart.get_grade())
#print(lisa.get_grade())

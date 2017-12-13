#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2017-12-2 13：28
# @Version : $Id$
# @des : decorator


class MyObject(object):
    def __init__(self):
        self.x=9
    def power(self):
        return self.x*self.x

#dir（obj）

if __name__ == '__main__':
    obj=MyObject()

    print(hasattr(obj,'x'))              #obj有没有属性X

    setattr(obj,'y',19)                  #obj设置属性y  值为19

    print(hasattr(obj,'y'))

    print(getattr(obj,'z',404))          #查看提取z属性的值，正常反馈z的值，不正常反馈404 404是默认的值

    print(dir(obj))                      #查看obj对象有哪些属性

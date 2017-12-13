#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2017-11-27 20:12:56
# @Version : $Id$
# @des : 利用闭包返回一个计数器函数，每次调用它返回递增整数：
#an=0
def createCounter():
    an=0
    def counter():
        nonlocal an          #在nonlo  内层函数对外层作用或的变量只有读访问权限
        an+=1
        return an
    return counter             #闭包返回一个函数   而不是返回一个函数的返回值。
if __name__ == '__main__':
    # 测试:
#    i=0
#    counterA = createCounter()
#    while i<10:
#        print(next(counterA))
#        i=i+1
# 测试:
    counterA = createCounter()
    print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
    counterB = createCounter()
    if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
        print('测试通过!')
    else:
        print('测试失败!')

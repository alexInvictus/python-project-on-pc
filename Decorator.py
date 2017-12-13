#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2017-12-2 13：28
# @Version : $Id$
# @des : decorator

#装饰器基本例子
def log(func):
    def wrapper(*args,**kw):
        print('call %s():' % func.__name__)
        return func(*args,**kw)
    return wrapper

@log
def now():                        #借助python语法@log 相当于执行了语句now=log(now)
    print('2013-12-25')

def log(text):
    def decorator(func):
        def wrapper(*args,**kw):
            print('%s %s():' % (text,func.__name__))
            return func(*args,**kw)
        return wrapper
    return decorator
@log('execute')
def now():
    print('2015-3-25')

import time

def metric(fn):
    start = time.time()
    def wrapper(*args,**kw):
        print('{0} executed in {1} ms'.format(fn.__name__,time.time() - start))
        return fn(*args,**kw)
    return wrapper

# 测试
@metric
def fast(x, y):                       #自己的理解：装饰器只是在运行函数前加一段自定义的log
    time.sleep(0.0012)
    print('123')
    return x + y+1

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z

if __name__ == '__main__':
    f=fast(11,22)               #先执行decorator里面的数据  在执行函数里面内容
    s = slow(11, 22, 33)
    if f != 33:
        print('测试失败!')
    elif s != 7986:
        print('测试失败!')




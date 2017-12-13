#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2017-12-2 13：28
# @Version : $Id$
# @des : 用匿名函数改造下面的函数

def is_odd(n):
    return n % 2 == 1

L = list(filter(is_odd, range(1, 20)))

A = list(filter(lambda a: a and a%2==1,range(1,20)))

if __name__ == '__main__':
    print(L)

    print(A)

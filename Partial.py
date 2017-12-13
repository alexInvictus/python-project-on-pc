#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2017-12-2 13：28
# @Version : $Id$
# @des : 偏函数，
import functools
int2 = functools.partial(int, base=2)

def intT(x):
    return int(x,2)

def intw(x,base=2):
    return int(x,2)


if __name__ == '__main__':
    print(intT('1000000'))
    print(intw('1000000'))
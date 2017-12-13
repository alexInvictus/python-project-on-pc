#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2017-12-2 13：28
# @Version : $Id$
# @des : 学习模块章节，用pip安装一个pillow。试运行pillow模块

#pillow模块调用open图像  路径为下面格式
from PIL import Image

#im=Image.open("C:\\Users\\alex\Desktop\\abc.jpg")

#im.show()

#调用matplotlib的一个库来绘制图片进行显示
from PIL import Image
import matplotlib.pyplot as plt
img=Image.open("C:\\Users\\alex\Desktop\\abc.jpg")
plt.figure("dog")
plt.imshow(img)
plt.show()
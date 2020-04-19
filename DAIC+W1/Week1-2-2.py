#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 02:28:35 2020

@author: reneelin
"""

name = input("请输入学生姓名：")
list = [name]
while name != '.':
    name = input("请输入学生姓名：")
    list += [name]
list.remove('.')
print(list)
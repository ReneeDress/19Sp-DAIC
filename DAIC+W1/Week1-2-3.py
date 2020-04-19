#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 02:46:26 2020

@author: reneelin
"""

student = {'张三': 170, '李四': 180, '王五': 160, '某六': 165}
print (student)
x = input("请输入学生姓名：")
for name in student:
    if student[x] < student[name]:
        print (name, student[name])
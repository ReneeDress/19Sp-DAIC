import numpy as np
names = np.array(['王微', '肖良英', '方绮雯', '刘旭阳', '钱易铭'])
subjects = np.array(['Math', 'English', 'Python', 'Chinese', 'Art', 'Database', 'Physics'])
scores = np.array([[70, 85, 77, 90, 82, 84, 89],
                   [60, 64, 80, 75, 80, 92, 90],
                   [90, 93, 88, 87, 86, 90, 91],
                   [80, 82, 91, 88, 83, 86, 80],
                   [88, 72, 78, 90, 91, 73, 80]])
# 选择并显示scores数组的1、4行
print("选择并显示scores数组的1、4行")
print(scores[[1,4]])
# 选择并显示scores数组中行序2、4学生的数学和Python成绩
print("选择并显示scores数组中行序2、4学生的数学和Python成绩")
print(scores[[2,4]][ :,(subjects == 'Math') | (subjects == 'Python')])
# 选择并显示scores数组中所有学生的数学和艺术课程成绩
print("选择并显示scores数组中所有学生的数学和艺术成绩")
print(scores[ :,(subjects == 'Math') | (subjects == 'Art')])
# 选择并显示scores数组中"王微"和"刘旭阳"的英语和艺术课程成绩
print("选择并显示scores数组中'王微'和'刘旭阳'的英语和艺术课程成绩")
print(scores[ (names == '王微') | (names == '刘旭阳') ][ :,(subjects == 'English') | (subjects == 'Art')])
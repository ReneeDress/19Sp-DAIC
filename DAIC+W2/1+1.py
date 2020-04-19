import numpy as np
names = np.array(['王微', '肖良英', '方绮雯', '刘旭阳', '钱易铭'])
subjects = np.array(['Math', 'English', 'Python', 'Chinese', 'Art', 'Database', 'Physics'])
# subjects数组中选择并显示序号1、2、4门课的名称
print("subjects数组中选择并显示序号1、2、4门课的名称")
print(subjects[ [1, 2, 4] ])
# 使用倒序索引选择并显示names数组中"方绮雯"
print("使用倒序索引选择并显示names数组中'方绮雯'")
print(names[-3])
# 选择并显示names数组从2到最后的数组元素
print("选择并显示names数组从2到最后的数组元素")
print(names[ 2: : ])
# 选择并显示subjects数组正序2~4的数组元素
print("选择并显示subjects数组正序2~4的数组元素")
print(subjects[ 2:5 ])
# 使用布尔条件选择并显示subjects数组中的英语和物理科目名称
print("使用布尔条件选择并显示subjects数组中的英语和物理科目名称")
print(subjects[ (subjects == 'English') | (subjects == 'Physics')])
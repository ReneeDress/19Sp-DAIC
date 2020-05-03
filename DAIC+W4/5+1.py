import pandas as pd
import numpy as np
# 数据合并
# 从studentsInfo.xlsx的“Group3”页读取数据，将序号、性别、年龄项保存到data1对象
stu = pd.read_excel('studentsInfo.xlsx', 'Group3')
col1 = ['序号', '性别', '年龄']
data1 = stu[col1]
print("从studentsInfo.xlsx的“Group3”页读取数据，将序号、性别、年龄项保存到data1对象")
print(data1)
# 从studentsInfo.xlsx的“Group3”页读取数据，将序号、身高、体重、成绩项保存到data2对象
col2 = ['序号', '身高', '体重', '成绩']
data2 = stu[col2]
print("\n从studentsInfo.xlsx的“Group3”页读取数据，将序号、身高、体重、成绩项保存到data2对象")
print(data2)
# 将data2合并到data1中，连接方式为内连接
print("\n将data2合并到data1中，连接方式为内连接")
print(pd.merge(data1, data2, how='inner'))
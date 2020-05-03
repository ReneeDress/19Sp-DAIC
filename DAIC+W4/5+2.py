import pandas as pd
import numpy as np
# 数据排序和排名
# 使用练习1最后合并的数据
stu = pd.read_excel('studentsInfo.xlsx', 'Group3')
col1 = ['序号', '性别', '年龄']
data1 = stu[col1]
col2 = ['序号', '身高', '体重', '成绩']
data2 = stu[col2]
data = pd.merge(data1, data2, how='inner')
print("使用练习1最后合并的数据")
print(data)
# 按月生活费对数据升序排序
print("\n按体重对数据升序排序")
print(data.sort_values(by=['体重'], ascending=True))
# 按身高对数据降序排名，并列取值方式设置为min
print("\n按身高对数据降序排名，并列取值方式设置为min")
data['身高排名'] = data['身高'].rank(method='min', ascending=False)
print(data)
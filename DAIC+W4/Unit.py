import pandas as pd
import numpy as np
# 根据某系的实验教学计划，完成以下分析：
# 读取DataScience.xls文件数据，创建为data数据对象
print("读取DataScience.xls文件数据，创建为DataFrame数据对象")
df = pd.read_excel('DataScience.xls')
# 查询df的数据量和基本结构（df.index，df.columns）
print("查询df的数据量和基本结构")
print(df.index)
print(df.columns)
# 查询df中是否含有NaN数据？将含有NaN数据的行导出为数据文件pre.csv，判断采用何种数据清洗模式：填充、删除或手工填充
mask = df.isnull().any(axis=1)
nan = df.loc[mask]
nan.to_csv('pre.csv')
print("\n", df.loc[mask])
df.fillna(method='ffill', inplace=True)
# 查询课程名称、实验项目名称、实验类型和二级实验室四列数据内容
print("\n", df[['课程名称', '实验项目名称', '实验类型', '二级实验室名称']])
# 统计每一门课程的实验课时数
classtime = df.groupby(['课程名称']).aggregate({'实验课时数':np.sum})
print("\n", classtime)
# 统计每周开设所有实验课时数
weektime = df.groupby(['周次']).aggregate({'实验课时数':np.sum})
print("\n", weektime)
# 统计每门课程的实验类型分布（crosstab）
print("\n", pd.crosstab(df['课程名称'], df['实验类型']))
# 统计每个班级的实验课课表
exp = df[['周次', '星期', '节次', '班级','实验项目名称']]
set = set(df['班级'])
c = pd.Series(list(set))
for i in range(0, len(c)):
    print("\n", exp.loc[df['班级'] == c[i]])
# 分析各二级实验室承担的实验课时量
exptime = df.groupby(['二级实验室名称']).aggregate({'实验课时数':np.sum})
print("\n", exptime)
# 分析各二级实验室能够支持的实验类型
print("\n", pd.crosstab(df['二级实验室名称'], df['实验类型']))
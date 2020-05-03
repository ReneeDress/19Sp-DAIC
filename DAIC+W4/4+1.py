import pandas as pd
import numpy as np
# 数据清洗
# 从studentsInfo.xlsx 文件的“Group1”表单中读取数据
stu = pd.read_excel('studentsInfo.xlsx', 'Group1', index_col=0)
print("从studentsInfo.xlsx 文件的“Group1”表单中读取数据")
print(stu)
# 将“案例教学”列数据值全改为NaN
stu['案例教学'] = np.nan
print("\n将“案例教学”列数据值全改为NaN")
print(stu)
# 滤除每行数据中缺失3项以上（包括3项）的行
print("\n滤除每行数据中缺失3项以上（包括3项）的行")
print(stu.dropna(thresh=4))
# 滤除值全部为NaN的列
print("\n滤除值全部为NaN的列")
print(stu.dropna(axis=1, how='all'))
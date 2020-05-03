import pandas as pd
import numpy as np
# 数据填充
# 使用习题1的数据
stu = pd.read_excel('studentsInfo.xlsx', 'Group1', index_col=0)
print("使用习题1的数据")
print(stu)
# 使用列的平均值填充“体重”和“成绩”列的NaN数据
print("\n使用列的平均值填充“体重”和“成绩”列的NaN数据")
stu.fillna({'体重':stu['体重'].mean(), '成绩':stu['成绩'].mean()}, inplace=True)
print(stu)
# 使用上一行数据填充“年龄”列的NaN数据
print("\n使用上一行数据填充“年龄”列的NaN数据")
print(stu['年龄'].ffill(inplace=True))
print(stu)
# 使用“中位数”填充“生活费用”NaN数据
print("\n使用“中位数”填充“生活费用”NaN数据")
stu.fillna({'月生活费':stu['月生活费'].median()}, inplace=True)
print(stu)
# 【提示】使用 df[“生活费用”].median() 计算中位数。
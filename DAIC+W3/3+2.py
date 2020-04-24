import numpy as np
import pandas as pd
from pandas import Series, DataFrame
# 从文件中读取有效数据保存到Dataframe对象中，跳过所有文字解释行
# 列索引名设为 ['flymiles','videogame','icecream','type‘]
cols = ['flymiles', 'videogame', 'icecream', 'type']
dating = pd.read_csv('datingTestSet.csv', skiprows=2, names=cols)
# print(dating)
# 显示读取到的前面5条数据
print("显示读取到的前面5条数据")
print(dating[ :5])
# 显示所有'type'为'largeDoses‘的数据
t = dating['type'] == 'largeDoses'
print("显示所有'type'为'largeDoses‘的数据")
print(dating[t])
# 将平均每周玩视频游戏时间超过10的数据都改成10
v = dating['videogame'] > 10
dating[v] = 10
# print(dating)
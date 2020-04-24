# 创建并访问Series对象
import pandas as pd
import numpy as np
from pandas import Series, DataFrame

# 创建Series数据对象，其中a-f为索引
s = Series([30, 25, 27, 41, 25, 34], index = ['a', 'b', 'c', 'd', 'e', 'f'])
print("创建Series数据对象")
print(s)
# 增加数据27，索引为g
ns = Series([27], index = ['g'])
s = s.append(ns)
print("增加数据27，索引为g")
print(s)
# 修改索引d对应的值为40
s['d'] = 40
print("修改索引d对应的值为40")
print(s)
# 查询值大于27的数据
print("查询值大于27的数据")
print(s[s.values > 27])
# 删除位置为1-3的数据
s = s.drop(s.index[1:3])
print("删除位置为1-3的数据")
print(s)

#【提示】位置1-3的索引列表，可以用 series.index[1:3] 来得到。
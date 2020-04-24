# 创建并访问DataFrame对象
import pandas as pd
import numpy as np
from pandas import Series, DataFrame

# 创建3×3DataFrame数据对象：数据内容为1-9；行索引为字符a，b，c；列索引为字符串one，two，three
d = np.random.randint(1, 10, size=(3, 3))
df = DataFrame(d, ['a', 'b', 'c'], ['one', 'two', 'three'])
print(df)
# 查询列索引为two和three两列数据
print("查询列索引为two和three两列数据")
print(df.loc[:, ['two', 'three']])
# 查询第0行、第2行、第0列、第2列数据
print("查询第0行、第2行、第0列、第2列数据")
print(df.iloc[[0, 2], [0, 2]])
# 筛选第1列中值大于2的所有行数据，另存为data1对象
i = df.iloc[:, 0] > 2
data1 = df.iloc[list(i)]
print("筛选第1列中值大于2的所有行数据，另存为data1对象")
print(data1)
# 为data1添加一列数据，列索引为four，值都为10
data1['four'] = 10
print("为data1添加一列数据，列索引为four，值都为10")
print(data1)
# 将data1所有值大于9的数据修改为8
n = data1 > 9
data1[n.reindex(index=data1.index, columns=data1.columns, fill_value=False)] = 8
print("将data1所有值大于9的数据修改为8")
print(data1)
# 删除data1中第0行和第1行数据
print(data1.index)
data1.drop(data1.index[0:2], axis=0, inplace=True)
print("删除data1中第0行和第1行数据")
print(data1)
#【提示】生成数据，使用numpy的arange()函数和reshape()函数；使用 data > 9 生成布尔型的DataFrame，用于整个DataFrame的数据过滤。
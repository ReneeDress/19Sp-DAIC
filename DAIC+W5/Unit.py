import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
# 文件bankpep.csv存放着银行储户的基本信息
# 请通过绘图对这些客户数据进行探索性分析。
data = pd.read_csv('bankpep.csv', index_col='id')
print(data)
# 1）客户年龄分布的直方图和密度图
age = data['age']
age.plot(title='Customer Age', density=True, kind='hist', use_index=True)
age.plot(title='Customer Age', kind='kde', use_index=True, style='k--')
plt.xlabel('Age')
plt.show()
# 2）客户年龄和收入关系的散点图
data.plot(kind='scatter', x='age', y='income', title='Customer Income', marker='*', grid=True, xlim=[0,80], ylim=[0,60000], label='(age,income)')
plt.xlabel('Age')
plt.ylabel('Income')
plt.show()
# 3）绘制散点图观察账户（年龄，收入，孩子数）之间的关系，对角线显示直方图
mat = data[['age', 'income', 'children']]
pd.plotting.scatter_matrix(mat, diagonal='hist', color='k')
plt.xlabel('Age')
plt.ylabel('Income')
plt.show()
# 4）按区域展示平均收入的柱状图，并显示标准差
mean = data.groupby(['region']).aggregate({'income':np.mean})
std = data.groupby(['region']).aggregate({'income':np.std})
mean.plot(kind='bar', y='income', title='Customer Income', yerr=std)
plt.show()
# 5）多子图绘制：账户中性别占比饼图，有车的性别占比饼图，按孩子数的账户占比饼图
fig = plt.figure()
ax1 = fig.add_subplot(2, 2, 1)
sex = data['sex']
sexcnt = pd.DataFrame(sex.value_counts())
sexcnt.plot(kind='pie', subplots=True, autopct='%1.1f%%', ax=ax1, startangle=60, legend=False)
ax1.set_title('Customer Sex')
ax2 = fig.add_subplot(2, 2, 2)
car = data['car']
carcnt = pd.DataFrame(car.value_counts())
carcnt.plot(kind='pie', subplots=True, autopct='%1.1f%%', ax=ax2, startangle=60, legend=False)
ax2.set_title('Customer Car')
ax3 = fig.add_subplot(2, 2, 3)
children = data['children']
childrencnt = pd.DataFrame(children.value_counts())
childrencnt.plot(kind='pie', subplots=True, autopct='%1.1f%%', ax=ax3, startangle=60, legend=False)
ax3.set_title('Customer Children')
plt.show()
# 6）各性别收入的箱须图
genderincome = data[['sex', 'income']]
genderincome.boxplot(by='sex')
plt.show()
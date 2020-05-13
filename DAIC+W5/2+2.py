import matplotlib.pyplot as plt
import pandas as pd
# 数据文件high-speed rail.csv存放着世界各国高速铁路的情况
# 1）各国运营里程对比柱状图， 标注China为“Longest”
data = pd.read_csv('High-speed+rail.csv', index_col='Country')
print(data)
print(data['Operation'])
operation = data['Operation']
operation.plot(title='Operation Mileage', kind='bar', use_index=True, fontsize='small')
plt.xlabel('Country')
plt.ylabel('Mileage(km)')
plt.annotate('Longest', xy=(0, operation['China']), xytext=(2, operation['China']), arrowprops=dict(arrowstyle='->'))
plt.show()
# 2）各国运营里程现状和发展堆叠柱状图
data.plot(title='Global trends of high-speed rail', kind='barh', stacked=True, use_index=True, fontsize='small')
plt.ylabel('Country')
plt.xlabel('Mileage(km)')
plt.show()
# 3）各国运营里程占比饼图，China扇形离开中心点
operation.plot(title='Operation Mileage', kind='pie', use_index=True, fontsize='small', explode=[0.2, 0, 0, 0, 0, 0], autopct='%0.0f%%', startangle=60)
plt.show()
# 【提示】：
# 从文件中读取数据时，使用第一列数据作为index
# data = pd.read_csv(‘High-speed rail.csv’, index_col =‘Country’) ，获取中国对应的数据行，使用data ['China’]
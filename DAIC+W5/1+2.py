import matplotlib.pyplot as plt
from pandas import DataFrame
# 1. 2012~2017年我国人均可支配收入为[1.47, 1.62, 1.78, 1.94, 2.38, 2.60](单位：万元)。按照要求绘制以下图形。
# 1）模仿例4-1和4-3，绘制人均可支配收入折线图。用小矩形标记数据点，红色虚线，
#    用注解标注最高点，图标题“Income chart”，设置坐标轴标题，最后将图形保存为JPG文件。一维数组访问。
income = [1.47, 1.62, 1.78, 1.94, 2.38, 2.60]
data = DataFrame({'Average Income: Ten Thousand': income}, index=['2012', '2013', '2014', '2015', '2016', '2017'])
print(data)
data.plot(title='Income chart', linewidth=2, marker='s', linestyle=':', color='r', grid=True, alpha=0.9, ylim=(1, 3))
plt.annotate('Highest', xy=(5, 2.60), xytext=(3.50, 2.60), arrowprops=dict(arrowstyle='->'))
plt.xlabel('Year', fontsize=12)
plt.ylabel('Average Income', fontsize=12)
plt.savefig('2012-2017AverageIncome.jpg', dpi=400, bbox_inches='tight')
plt.show()
# 2）模仿例4-2，使用多个子图分别绘制人均可支配收入的折线图、箱须图以及柱状图。
# 【提示：】
# 1）创建3个子图分别使用（2,2,1）、（2,2,2）和（2,1,2）作为参数。
# 2）使用plt.subplots_adjust()函数调整子图间距离，以便添加图标题。
from pandas import Series
data2 = Series(income, index=['2012', '2013', '2014', '2015', '2016', '2017'])
fig = plt.figure(figsize=(6, 6))
ax1 = fig.add_subplot(2, 2, 1)
ax1.plot(data2)
plt.title('line chart')
ax2 = fig.add_subplot(2, 1, 2)
data2.plot(title='bar chart', kind='bar', use_index=True, fontsize='small', ax=ax2)
ax3 = fig.add_subplot(2, 2, 2)
data2.plot(title='box-whisker chart', xticks=[], kind='box', fontsize='small', ax=ax3)
plt.xlabel('2012-2017', fontsize=12)
plt.subplots_adjust(hspace=1)
plt.show()


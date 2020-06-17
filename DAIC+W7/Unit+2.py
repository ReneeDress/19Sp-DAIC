# 从互联网上收集上海松江大学城附近房屋的特征数据，以及相应的房价，保存在文件house_price文件中。利用数据集实现以下分析目标。
# 1）使用k - menas算法对房屋进行聚类分析，找出合适的k值，结合房产市场并对聚类结果进行说明。
# 2）使用线性分类器对房产数据进行拟合，并使用模型预测自己希望购买的房屋的价格。
# 【提示】：首先通过统计、可视化等过程对数据集进行探索性分析，然后再使用算法建立分析模型。
# 只做线性回归
# 户型-房间	户型-厅	户型-厨房	户型-卫生	建筑面积	朝向	装修	电梯	总楼层	所处层数	建筑类型	建筑结构	小区	经度	纬度	地址	建筑时间	价格（万）
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_excel('housePrice.xlsx', index_col=0, header=0)
print(list(data))
print(data)
data.drop(['建筑结构', '小区', '地址', '经度', '纬度'], axis=1, inplace=True)
print(data)
# X = data.iloc[:,:-1].values.astype(float)
# X = data.iloc[:,:5].values.astype(float)
X = data.iloc[:, [4]].values.astype(float)
Y = data.iloc[:,-1].values.astype(float)
print(X, Y)
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.35, random_state=1)
from sklearn.linear_model import LinearRegression
linreg = LinearRegression()
linreg.fit(X, Y)
print(linreg.intercept_, linreg.coef_)
from sklearn import metrics
Y_pred = linreg.predict(X)
Y_test_pred = linreg.predict(X_test)
print(Y_pred, Y_test_pred)
err = metrics.mean_squared_error(Y, Y_pred)
test_err = metrics.mean_squared_error(Y_test, Y_test_pred)
print('The mean squar error of train and test are: {:.2f}, {:.2f}'.format(err, test_err))
predict_score = linreg.score(X_test, Y_test)
print('The decision coeficient is: {:.2f} '.format(predict_score))
plt.scatter(X, Y, color='blue')
plt.plot(X, Y_pred, color='red', linewidth=4)
plt.xticks(())
plt.yticks(())
plt.show()
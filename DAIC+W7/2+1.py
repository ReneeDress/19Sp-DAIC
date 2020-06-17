# 延续5.2.3节的回归模型的性能评估，计算使用全部数据学习得到的回归模型linreg在测试集上的性能，与只使用训练集的模型linregTr进行比较，并对结论进行分析。
import pandas as pd
data = pd.read_csv('advertising.csv', index_col=0)
X = data.iloc[:, 0:3].values.astype(float)
Y = data.iloc[:, 3].values.astype(float)
print(X)
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.35, random_state=1)
from sklearn.linear_model import LinearRegression
linreg = LinearRegression()
linregTr = LinearRegression()
linreg.fit(X, Y)
linregTr.fit(X_train, Y_train)
# print(linreg.intercept_, linreg.coef_)
# print(linregTr.intercept_, linregTr.coef_)
from sklearn import metrics
Y_pred = linreg.predict(X)
Y_train_pred = linreg.predict(X_train)
Y_test_pred = linreg.predict(X_test)
err = metrics.mean_squared_error(Y, Y_pred)
train_err = metrics.mean_squared_error(Y_train, Y_train_pred)
test_err = metrics.mean_squared_error(Y_test, Y_test_pred)
print('Linreg\'s mean squar error of train and test are: {:.2f}, {:.2f}'.format(err, test_err))
print('LinregTr\'s mean squar error of train and test are: {:.2f}, {:.2f}'.format(train_err, test_err))
predict_score = linreg.score(X_test, Y_test)
Trpredict_score = linregTr.score(X_test, Y_test)
print('Linreg\'s decision coeficient is: {:.2f} '.format(predict_score))
print('LinregTr\'s decision coeficient is: {:.2f} '.format(Trpredict_score))
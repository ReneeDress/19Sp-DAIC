# 从案例5-1中取出前100条样本，学习回归模型linregHalf；计算模型在练习1的测试集上的预测性能，并与200条样本学习的模型预测性能进行比较
import pandas as pd
data = pd.read_csv('advertising.csv', index_col=0)
X = data.iloc[0:100, 0:3].values.astype(float)
Y = data.iloc[0:100, 3].values.astype(float)
X_2 = data.iloc[0:200, 0:3].values.astype(float)
Y_2 = data.iloc[0:200, 3].values.astype(float)
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.35, random_state=1)
from sklearn.linear_model import LinearRegression
linregHalf = LinearRegression()
linregTwo = LinearRegression()
linregHalf.fit(X, Y)
linregTwo.fit(X_2, Y_2)
# print(linregHalf.intercept_, linreg.coef_)
# print(linregTwo.intercept_, linregTwo.coef_)
from sklearn import metrics
Y_pred = linregHalf.predict(X)
Y_2_pred = linregHalf.predict(X_2)
Y_test_pred = linregHalf.predict(X_test)
err = metrics.mean_squared_error(Y, Y_pred)
two_err = metrics.mean_squared_error(Y_2, Y_2_pred)
test_err = metrics.mean_squared_error(Y_test, Y_test_pred)
print('LinregHalf\'s mean squar error of train and test are: {:.2f}, {:.2f}'.format(err, test_err))
print('LinregTwo\'s mean squar error of train and test are: {:.2f}, {:.2f}'.format(two_err, test_err))
predict_score = linregHalf.score(X_test, Y_test)
Twopredict_score = linregTwo.score(X_test, Y_test)
print('LinregHalf\'s decision coeficient is: {:.2f} '.format(predict_score))
print('LinregTwo\'s decision coeficient is: {:.2f} '.format(Twopredict_score))
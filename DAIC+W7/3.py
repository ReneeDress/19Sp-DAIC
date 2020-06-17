# 数据集bankdebt.csv
# 1. 将数据集划分为训练集和测试集，查看决策树分类器的性能。
# 2. 将例5-3学习的分类器保存到文件中，然后重新加载预测给出的新数据
import pandas as pd
data = pd.read_csv('bankdebt.csv', index_col=0, header=None)
data.loc[data[1] == 'Yes', 1] = 1
data.loc[data[1] == 'No', 1] = 0
data.loc[data[4] == 'Yes', 4] = 1
data.loc[data[4] == 'No', 4] = 0
data.loc[data[2] == 'Single', 2] = 1
data.loc[data[2] == 'Married', 2] = 2
data.loc[data[2] == 'Divorced', 2] = 3
X = data.loc[:, 1:3].values.astype(float)
Y = data.loc[:, 4].values.astype(float)
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.35, random_state=1)
from sklearn import tree
clfTr = tree.DecisionTreeClassifier()
clfTr = clfTr.fit(X_train, Y_train)
clfTr.score(X_train, Y_train)
print('Classifier\'s Score: ', clfTr.score(X_train, Y_train), '\n')
predicted_Y = clfTr.predict(X_train)
from sklearn import metrics
print(metrics.classification_report(Y_train, predicted_Y))
print('Confusion matrix:')
print(metrics.confusion_matrix(Y_train, predicted_Y))
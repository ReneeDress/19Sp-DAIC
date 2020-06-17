# 葡萄酒数据集（wine.data）搜集了法国不同产区葡萄酒的化学指标。试建立决策树、SVM和神经网络3种分类器模型，比较各种分类器在此数据集上的效果。
# 【提示】：每种分类器，需要对参数进行尝试，找出此种分类算法的较优模型，再与其他分类器性能进行比较。
# 只做决策树
import pandas as pd
data = pd.read_csv('wine.data', header=None)
X = data.iloc[:, 0:14].values.astype(float)
Y = data.iloc[:, 13].values.astype(float)
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
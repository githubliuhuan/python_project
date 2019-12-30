# -*- coding: utf-8 -*-
# 转载自https://www.cnblogs.com/wj-1314/p/9628303.html
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data'
url1 = pd.read_csv(r'wine.txt',header=None)
# url1 = pd.DataFrame(url1)
# df = pd.read_csv(url1,header=None)
url1.columns =  ['Class label', 'Alcohol', 'Malic acid', 'Ash',
              'Alcalinity of ash', 'Magnesium', 'Total phenols',
              'Flavanoids', 'Nonflavanoid phenols', 'Proanthocyanins',
              'Color intensity', 'Hue', 'OD280/OD315 of diluted wines', 'Proline']
# print(url1)

# 查看几个标签
# Class_label = np.unique(url1['Class label'])
# print(Class_label)
# 查看数据信息
# info_url = url1.info()
# print(info_url)

# 除去标签之外，共有13个特征，数据集的大小为178，
# 下面将数据集分为训练集和测试集
from sklearn.model_selection import train_test_split
# print(type(url1))
# url1 = url1.values
# x = url1[:,0]
# y = url1[:,1:]
x,y = url1.iloc[:,1:].values,url1.iloc[:,0].values
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3,random_state=0)
feat_labels = url1.columns[1:]

# n_estimators：森林中树的数量
# n_jobs  整数 可选（默认=1） 适合和预测并行运行的作业数，如果为-1，则将作业数设置为核心数
forest = RandomForestClassifier(n_estimators=10000, random_state=0, n_jobs=-1)
forest.fit(x_train, y_train)

# 下面对训练好的随机森林，完成重要性评估
# feature_importances_  可以调取关于特征重要程度
importances = forest.feature_importances_
print("重要性：",importances)
x_columns = url1.columns[1:]
indices = np.argsort(importances)[::-1]
for f in range(x_train.shape[1]):
    # 对于最后需要逆序排序，我认为是做了类似决策树回溯的取值，从叶子收敛
    # 到根，根部重要程度高于叶子。
    print("%2d) %-*s %f" % (f + 1, 30, feat_labels[indices[f]], importances[indices[f]]))


# 筛选变量（选择重要性比较高的变量）
threshold = 0.15
x_selected = x_train[:,importances > threshold]

# 可视化
import matplotlib.pyplot as plt
plt.figure(figsize=(10,6))
plt.title(u'红酒的数据集中各个特征的重要程度',fontsize = 18)
plt.ylabel("import level",fontsize = 15,rotation=90)
plt.rcParams['font.sans-serif'] = ["SimHei"]
plt.rcParams['axes.unicode_minus'] = False
for i in range(x_columns.shape[0]):
    plt.bar(i,importances[indices[i]],color='orange',align='center')
    plt.xticks(np.arange(x_columns.shape[0]),x_columns,rotation=90,fontsize=15)
plt.show()


# 利用SVR进行训练
# from sklearn.svm import SVR  # SVM中的回归算法
# import pandas as pd
# from sklearn.model_selection import train_test_split
# import matplotlib.pyplot as plt
# import numpy as np
# # 数据预处理，使得数据更加有效的被模型或者评估器识别
# from sklearn import preprocessing
# from sklearn.externals import joblib
#
# # 获取数据
# origin_data = pd.read_csv('wine.txt',header=None)
# X = origin_data.iloc[:,1:].values
# Y = origin_data.iloc[:,0].values
# print(type(Y))
# # print(type(Y.values))
# # 总特征  按照特征的重要性排序的所有特征
# all_feature = [ 9, 12,  6, 11,  0, 10,  5,  3,  1,  8,  4,  7,  2]
# # 这里我们选取前三个特征
# topN_feature = all_feature[:3]
# print(topN_feature)
#
# # 获取重要特征的数据
# data_X = X[:,topN_feature]
#
# # 将每个特征值归一化到一个固定范围
# # 原始数据标准化，为了加速收敛
# # 最小最大规范化对原始数据进行线性变换，变换到[0,1]区间
# data_X = preprocessing.MinMaxScaler().fit_transform(data_X)
#
# # 利用train_test_split 进行训练集和测试集进行分开
# X_train,X_test,y_train,y_test  = train_test_split(data_X,Y,test_size=0.3)
#
# # 通过多种模型预测
# model_svr1 = SVR(kernel='rbf',C=50,max_iter=10000)
#
#
# # 训练
# # model_svr1.fit(data_X,Y)
# model_svr1.fit(X_train,y_train)
#
# # 得分
# score = model_svr1.score(X_test,y_test)
# print(score)
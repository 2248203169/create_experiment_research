# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import math
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, recall_score

df = pd.read_csv("D:/创新设计/training.csv",encoding='gbk')
test = pd.read_csv("D:/创新设计/testing.csv",encoding='gbk')

print(df)
print(test)
df.head()
df = df.drop(['url','change','id'],axis=1)
sparse_features = [feat for feat in df.columns if feat not in ['id', 'Label']]
df[sparse_features] = df[sparse_features].fillna(0, )

df.dropna(inplace=True)
print(type(df))
train_inf = np.isinf(df)
df[train_inf] = 0
print("NAN数据已处理完毕")


label = df['label']
df = df.drop(columns=['label'])
test.head()
test = test.drop(['url','change','id'],axis=1)
sparse_features = [feat for feat in test.columns if feat not in ['id', 'label']]
test[sparse_features] = test[sparse_features].fillna(0, )
test.dropna(inplace=True)
train_inf_test = np.isinf(test)
test[train_inf_test] = 0
print("NAN数据已处理完毕")
print(df)
print(test)
test_label = test['label']
test = test.drop(columns=['label'])
clf = RandomForestClassifier(n_estimators=20, criterion='gini', max_features=3, max_depth=60000)
clf.fit(df, label)
y_pred = clf.predict(test)

print(y_pred)
print(confusion_matrix(test_label, y_pred))
print(classification_report(test_label, y_pred))
print('accuracy:', accuracy_score(test_label, y_pred))
print('recall:', recall_score(test_label, y_pred, average=None))
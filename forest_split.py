# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import math
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, recall_score
from sklearn.model_selection import train_test_split

#iris = pd.read_excel('D:/创新设计/B/1.xlsx')
iris = pd.read_excel('D:/2.xlsx')
df,test = train_test_split(iris,test_size=0.2)

print(df)
print(test)
df.head()

df = df.drop(['url'],axis=1)
sparse_features = [feat for feat in df.columns if feat not in ['label']]
df[sparse_features] = df[sparse_features].fillna(0, )

df.dropna(inplace=True)
print(type(df))
train_inf = np.isinf(df)
df[train_inf] = 0
print("NAN数据已处理完毕")


label = df['label']
df = df.drop(columns=['label'])
test.head()
test = test.drop(['url'],axis=1)
sparse_features = [feat for feat in test.columns if feat not in ['label']]
test[sparse_features] = test[sparse_features].fillna(0, )
test.dropna(inplace=True)
train_inf_test = np.isinf(test)
test[train_inf_test] = 0
print("NAN数据已处理完毕")
"""index = []
jindex = []
black1 = df['black_word']
white1 = df['white_word']
black2 = test['black_word']
white2 = test['white_word']
print(black1)
print(white1)
for i in range(len(black1)):
    if black1[i] == 0 and white1[i] == 0:
        index.append(i)
for j in range(len(black2)):
    if black2[j] == 0 and white2[j] == 0:
        jindex.append(j)
for g in index:
    df.pop(g)
for h in jindex:
    test.pop(h)"""
print(df)
print(test)
test_label = test['label']
test = test.drop(columns=['label'])
clf = RandomForestClassifier(n_estimators=20, criterion='gini', max_features=1, max_depth=60000)
clf.fit(df, label)
y_pred = clf.predict(test)

print(y_pred)
print(confusion_matrix(test_label, y_pred))
print(classification_report(test_label, y_pred))
print('accuracy:', accuracy_score(test_label, y_pred))
print('recall:', recall_score(test_label, y_pred, average=None))
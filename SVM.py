from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics
import pandas as pd

iris = pd.read_excel('D:/2.xlsx')
train,test = train_test_split(iris,test_size=0.2)
train_data = train.iloc[:,1:5]
train_label = train['label']
test_data = test.iloc[:,1:5]
test_label = test['label']
model = LogisticRegression()
model.fit(train_data,train_label)

prediction = model.predict(test_data)
print(test_label)
print("Test accuracy:",'%.8f'%(metrics.accuracy_score(prediction,test_label)))
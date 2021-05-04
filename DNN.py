import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense,Activation,Dropout,concatenate
from keras.optimizers import SGD,Adam,RMSprop
from keras.utils import np_utils
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from keras import callbacks
train = pd.read_csv("D:/创新设计/training.csv",encoding='gbk')
test = pd.read_csv("D:/创新设计/testing.csv",encoding='gbk')

train.head()
train = train.drop(['url','change','id'],axis=1)
sparse_features = [feat for feat in train.columns if feat not in ['label']]
train[sparse_features] = train[sparse_features].fillna(0, )
train.dropna(inplace=True)
train_inf = np.isinf(train)
train[train_inf] = 0
print("NAN数据已处理完毕")

test.head()
test = test.drop(['url','change','id'],axis=1)
sparse_features = [feat for feat in test.columns if feat not in ['label']]
test[sparse_features] = test[sparse_features].fillna(0, )
test.dropna(inplace=True)
train_inf_test = np.isinf(test)
test[train_inf_test] = 0
print("NAN数据已处理完毕")

X_train = train.iloc[:, train.columns != 'label']
y_train = train.iloc[:, train.columns == 'label']
X_test = test.iloc[:, test.columns != 'label']
y_test = test.iloc[:, test.columns == 'label']
X_train_undersample, X_test_undersample, y_train_undersample, y_test_undersample = train_test_split(X_train,y_train,test_size = 0.3,random_state = 0)

y_train_undersample=np_utils.to_categorical(y_train_undersample,2)
y_test_undersample=np_utils.to_categorical(y_test_undersample,2)
y_test=np_utils.to_categorical(y_test,2)

scaler = MinMaxScaler(feature_range=(0, 1))
scaler.fit(X_train)
X_train = scaler.transform(X_train)
scaler.fit(X_train_undersample)
X_train_undersample = scaler.transform(X_train_undersample)
scaler.fit(X_test_undersample)
X_test_undersample = scaler.transform(X_test_undersample)

print(X_train)
print(X_train_undersample)
print(X_test_undersample)

NB_EPOCH=30
BATCH_SIZE=3
VERBOSE=1
NB_CLASSES=2
OPTIMIZER=SGD()
N_HIDDEN = 128
VALIDATION_SPLIT=0.2

DROPOUT=0.3

model=Sequential()#序贯模型0

model.add(Dense(N_HIDDEN,input_shape=(5,)))
model.add(Activation('relu'))
model.add(Dropout(DROPOUT))
model.add(Dense(N_HIDDEN))
model.add(Activation('relu'))
model.add(Dropout(DROPOUT))
model.add(Dense(NB_CLASSES))
model.add(Activation('softmax'))
model.summary()
es = callbacks.EarlyStopping(monitor='accuracy', min_delta=0.01, patience=3, mode='max', baseline=None, restore_best_weights=True)

model.compile(loss='binary_crossentropy',optimizer='sgd',metrics=['accuracy'])
#模型编译，损失采用二分对比损失，以优化器SGD梯度下降，并评估模型精度
history=model.fit(X_train_undersample,y_train_undersample,
                 validation_data=(X_train, y_train),
                 batch_size=BATCH_SIZE,epochs=NB_EPOCH,
                 verbose=VERBOSE,validation_split=VALIDATION_SPLIT,
                 callbacks=[es])

plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('Model accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Train', 'Test'], loc='upper left')
plt.show()

plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Model loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train', 'Test'], loc='upper left')
plt.show()

score1=model.evaluate(X_test_undersample,y_test_undersample,verbose=VERBOSE)
print('Test loss:',score1[0])
print('Test accuracy:',score1[1])
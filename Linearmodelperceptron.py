
# coding: utf-8

# In[50]:

# Посмотрим, как меняется качество работы персептрона после нормализации признаков. Увеличилось на 55%.
import pandas
import numpy as np
import sklearn
from sklearn.linear_model import Perceptron
from sklearn.preprocessing import StandardScaler

data_train = pandas.read_csv('C:\\perceptron-train.csv', names = [i for i in range(3)])
data_test = pandas.read_csv('C:\\perceptron-test.csv', names = [i for i in range(3)])
test_aim = data_test[0]
del data_test[0]
train_aim = data_train[0]
del data_train[0]
clf = Perceptron(random_state = 241)
clf.fit(data_train, train_aim)
predict = clf.predict(data_test)

before = sklearn.metrics.accuracy_score(test_aim, predict)


scaler = StandardScaler()

train_scaled = scaler.fit_transform(data_train)
test_scaled = scaler.transform(data_test)

clf_scale = Perceptron(random_state = 241)
clf_scale.fit(train_scaled, train_aim)
predict_scale = clf_scale.predict(test_scaled)

after = sklearn.metrics.accuracy_score(test_aim, predict_scale)

print(after - before)


# In[ ]:




# In[ ]:




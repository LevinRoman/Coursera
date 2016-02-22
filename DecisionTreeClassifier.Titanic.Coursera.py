
# coding: utf-8

# In[ ]:

import pandas
import numpy as np
from sklearn.tree import DecisionTreeClassifier
data_source = pandas.read_csv('C:\\titanic.csv', usecols = ['Age', 'Pclass', 'Fare', 'Sex','Survived'])

Sex_change = (data_source['Sex'] == 'male')
data_source['Sex'] = Sex_change
data = data_source[pandas.notnull(data_source['Age'])]
aim = data['Survived']
del data['Survived']

clf = DecisionTreeClassifier(random_state = 241)
clf.fit(data, aim)
importances = clf.feature_importances_
print(clf.predict([3, 0, 60, 80]))


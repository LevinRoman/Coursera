
# coding: utf-8

# In[ ]:

import pandas
import numpy as np
import sklearn as sk
from sklearn.cross_validation import KFold 
from sklearn.neighbors import KNeighborsClassifier
data = pandas.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data', names = [i for i in range(14)])
Klass = data[0]
del data[0]
kf = KFold(n = len(Klass), n_folds = 5, shuffle = True, random_state = 42)
quality = []
opt = 0
ind = 0
data = sk.preprocessing.scale(data)
for k in range(1,51):
    scores = sk.cross_validation.cross_val_score(KNeighborsClassifier(n_neighbors = k), data, Klass, cv = kf)
    qual = np.mean(scores)
    quality.append(qual)
    if (qual >= opt):
        opt = qual
        ind = k
print(opt, ind)


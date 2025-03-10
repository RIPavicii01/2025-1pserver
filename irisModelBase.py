# 2025_03_10
#프로젝트 2 붓꽃분류기 만들기
from xml.sax.handler import property_interning_dict

import joblib
import numpy as np
import  pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
iris_df = pd.read_csv('iris.csv')

print(iris_df['sepal_length'].mean())
y=iris_df['species']
X=iris_df.drop('species', axis=1)
# print(X)
# print(y)
kn =KNeighborsClassifier()
rfc=RandomForestClassifier()
model_rfc = rfc.fit(X,y)
model_kn = kn.fit(X,y)

joblib.dump(model_rfc,'model_rfc.pkl')

# X_new = np.array([[3,3,3,3]])
# ['versicolor']
# [[0.  0.8 0.2]]
X_new = np.array([[5.0,3.4,1.4,0.2]])
# ['setosa']
# [[1. 0. 0.]]
model_rfc = joblib.load('model_rfc.pkl')
# X_new = np.array([[1,4.2,1.4,7]])
# prediction=model_kn.predict(X_new)
prediction=model_rfc.predict(X_new)
print(prediction)
# probability = model_kn.predict_proba(X_new)
probability = model_rfc.predict_proba(X_new)
print(probability)
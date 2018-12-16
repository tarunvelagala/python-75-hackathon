import sklearn
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score, confusion_matrix
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

df = pd.read_csv('csv/data.csv')

y = df['diagnosis'].apply(lambda x: '1' if x == 'M' else '0')

lst = ['Unnamed: 32', 'id', 'diagnosis']
x = df.drop(lst, axis=1)
print(df.groupby('diagnosis').size())

drop_list1 = ['perimeter_mean', 'radius_mean', 'compactness_mean', 'concave points_mean', 'radius_se', 'perimeter_se',
              'radius_worst', 'perimeter_worst', 'compactness_worst', 'concave points_worst', 'compactness_se',
              'concave points_se', 'texture_worst', 'area_worst']
x_1 = x.drop(drop_list1, axis=1)  # do not modify x, we will use it later
x_1.head()
x_train, x_test, y_train, y_test = train_test_split(
    x_1, y, test_size=0.3, random_state=42)

# random forest classifier with n_estimators=10 (default)
clf_rf = RandomForestClassifier()
clr_rf = clf_rf.fit(x_train, y_train)

ac = accuracy_score(y_test, clf_rf.predict(x_test))
print('Accuracy is: ', ac)
cm = confusion_matrix(y_test, clf_rf.predict(x_test))
print(cm)

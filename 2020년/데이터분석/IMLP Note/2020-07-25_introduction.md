## Introduction

### 붓꽃 데이터로 맛보는 머신러닝



#### Libarary Import

```python
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import mglearn

%matplotlib inline
```



#### Dataset Load

```python
from sklearn.datasets import load_iris
iris_dataset = load_iris()
```



#### 살펴보기

```python
print("Keys of iris_dataset:\n", iris_dataset.keys())
print("Target names : ", iris_dataset['target_names'])
print("Feature names : ", iris_dataset['feature_names'])

print('Types of data : ', type(iris_dataset['data']) )
print('Size of data : ', iris_dataset['data'].shape )
print('Type of target : ', type(iris_dataset['target']))
print('shape : ', iris_dataset['target'].shape)
```



#### 시각화하여 살펴보기

```python
iris_dataframe = pd.DataFrame(X_train, columns=iris_dataset.feature_names)
pd.plotting.scatter_matrix(iris_dataframe, c=y_train, figsize=(15,15), marker='o', 
                          hist_kwds={'bins':20}, s=60, alpha=.8, cmap=mglearn.cm3)
```

<img src="../../../upload/image-20200726122307078.png" alt="image-20200726122307078" style="zoom:80%;" />



#### 트레인셋과 테스트셋 분리하기

```python
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(iris_dataset['data'], iris_dataset['target'], random_state=0)
```



#### KNN 으로 분류하기

```python
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=1)

knn.fit(X_train,  y_train)

f1_score = knn.score(X_test, y_test)
print("테스트셋의 정확도 : {:.2f}".format(f1_score))
```


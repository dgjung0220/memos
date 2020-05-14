##### 정리

[Kaggle](https://www.kaggle.com)

https://www.kaggle.com/daehungwak/guide-kor-dg



1. 데이터셋 확인

   - 데이터 구성 확인
   - 데이터 칼럼 오류 수정이나 null check 등 확인하여 향후 이용시 수정

2. 탐색적 데이터 분석 (EDA, Exploratory Data Analysis)

   - 여러 feature들을 개별적으로 분석하고, feature들 간의 상관관계를 확인

   - 시각화 툴을 사용하여 Insight 찾기

     

3. 특성 공학 (Feature Engineering)

   - 모델의 성능을 높이기 위한 feature engineering
   - one-hot encoding, smoothing, 클래스로 나누기, 구간으로 나누기, 텍스트 데이터 처리 등의 작업

   

4. 모델 개발 및 학습

   - sklearn(머신 러닝), keras, tensorflow, pytorch(딥 러닝) 등을 이용한 모델 개발

     

5. 모델 예측 및 평가

   - Train set 으로 모델 학습 후, Test set를 통한 prediction
   - 예측 성능이 원하는 수준인지 판단 및 위 절차 반복



#### 1. 데이터셋 확인

```python
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import keras
import sklearn

plt.style.use('seaborn')
sns.set(font_scale=2.5)

import missingno as msno

import warnings
warnings.filterwarnings('ignore')

%matplotlib inline
```

```python
os.listdir('../input/2019-1st-ml-month-with-kakr')
# output : ['test.csv', 'sample_submission.csv', 'train.csv']
```

```python
df_train = pd.read_csv('../input/2019-1st-ml-month-with-kakr/train.csv')
df_test = pd.read_csv('../input/2019-1st-ml-month-with-kakr/test.csv')
df_submit = pd.read_csv('../input/2019-1st-ml-month-with-kakr/sample_submission.csv')

df_train.shape, df_test.shape, df_submit.shape
# output : ((891, 12), (418, 11), (418, 2))

df_train.columns
# output : Index(['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp',
#       'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked'],
#      dtype='object')

df_train.dtypes
# output : PassengerId      int64
# Survived         int64
# Pclass           int64
# Name            object
# sex             object
# Age            float64
# SibSp            int64
# Parch            int64
# Ticket          object
# Fare           float64
# Cabin           object
# Embarked        object
# dtype: object

# pandas describe, 각 feature 들의 통계치
df_train.describe()
```

##### 결측치 확인

​	Age, Cabin, Embarked 등에 결측치가 보임 

```python
df_train.isnull().sum() / df_train.shape[0]
# output : PassengerId    0.000000
# Survived       0.000000
# Pclass         0.000000
# Name           0.000000
# Sex            0.000000
# Age            0.198653
# SibSp          0.000000
# Parch          0.000000
# Ticket         0.000000
# Fare           0.000000
# Cabin          0.771044
# Embarked       0.002245
# dtype: float64
```

```python
df_test.isnull().sum() / df_test.shape[0]
# output : PassengerId    0.000000
# Pclass         0.000000
# Name           0.000000
# Sex            0.000000
# Age            0.205742
# SibSp          0.000000
# Parch          0.000000
# Ticket         0.000000
# Fare           0.002392
# Cabin          0.782297
# Embarked       0.000000
dtype: float64
```

##### Target 라벨 확인 (Survived 확인)

​	타겟의 분포를 확인.

```python
f, ax = plt.subplots(1, 2, figsize=(18, 8))

df_train['Survived'].value_counts().plot.pie(explode=[0, 0.1], autopct='%1.1f%%', ax=ax[0], shadow=True)
ax[0].set_title('Pie plot - Survived')
ax[0].set_ylabel('')
sns.countplot('Survived', data=df_train, ax=ax[1])
ax[1].set_title('Count plot - Survived')

plt.show()
```



#### 2. 탐색적 데이터 분석 (EDA, Exploratory Data Analysis)

​	시각화 라이브러리는 matplotlib, seaborn, plotly 등이 있음.


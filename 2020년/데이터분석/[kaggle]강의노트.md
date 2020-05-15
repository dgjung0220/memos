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



##### 2.1 Pclass

- Pclass는 서수형 데이터, 카테고리면서 순서가 있는 데이터 타입
- groupby, pivot 등의 메스드를 이용
- pandas dataframe에서 groupby를 사용 후, count()를 평균하면 각 Pclass 별 생존률 산출 가능
- sum() : 생존한 사람의 총합

```python
# pclass 그룹 별 데이터 카운트
df_train[['Pclass', 'Survived']].groupby(['Pclass'], as_index=True).count()

# pclass 그룹별 생존자 수 합
df_train[['Pclass', 'Survived']].groupby(['Pclass'], as_index=True).sum()

# crosstab을 사용하여 위의 작업 수행
pd.crosstab(df_train['Pclass'], df_train['Survived'], margins=True)

# 생존률 산출 : mean
df_train[['Pclass', 'Survived']].groupby(['Pclass'], as_index=True).mean()

# 생존률 시각화
df_train[['Pclass', 'Survived']].groupby(['Pclass'], as_index=True).mean().plot.bar()
```

##### 2.2 Sex

```python
f, ax = plt.subplots(1, 2, figsize=(18,8))
df_train[['Sex', 'Survived']].groupby(['Sex'], as_index=True).mean().plot().bar(ax=ax[0])
ax[0].set_title('Survived vs Sex')

sns.countplot('Sex', hue='Survived', data=df_train, ax=ax[1])
ax[1].set_title('Sex : Survived vs Dead')
plt.show()
```

##### 2.3 Sex & Pclass

```python
sns.factorplot('Pclass', 'Survived', hue='Sex', data=df_train, size=6, aspect=1.5)
```

##### 2.4 Age

```python
print('제일 나이 많은 탑승객 : {:.1f} Years'.format(df_train['Age'].max()))
print('제일 어린 탑승객 : {:.1f} Years'.format(df_train['Age'].min()))
print('탑승객 평균 나이 : {:.1f} Years'.format(df_train['Age'].mean()))

# output : 제일 나이 많은 탑승객 : 80.0 Years
# 제일 어린 탑승객 : 0.4 Years
# 탑승객 평균 나이 : 29.7 Years
```

```python
fig, ax = plt.subplots(1, 1, figsize=(9, 5))
sns.kdeplot(df_train[df_train['Survived'] == 1]['Age'], ax=ax)
sns.kdeplot(df_train[df_train['Survived'] == 0]['Age'], ax=ax)
plt.legend(['Survived == 1', 'Survived == 0'])
plt.show()
```

```python
plt.figure(figsize=(8,6))
df_train['Age'][df_train['Pclass'] == 1].plot(kind='kde')
df_train['Age'][df_train['Pclass'] == 2].plot(kind='kde')
df_train['Age'][df_train['Pclass'] == 3].plot(kind='kde')

plt.xlabel('Age')
plt.title('Age distribution within classes')
plt.legend(['1st class', '2nd class', '3rd class'])
```



나이대와 따른 생존 확률, 누적확률을 활용한 시각화

```python
cummulate_survival_ratio = []

for i in range(1, 80) :
    cummulate_survival_ratio.append(df_train[df_train['Age'] < i]['Survivied'].sum() / len(df_train[df_train['Age'] < i]['Survived']))  
    
plt.figure(figsize = (7,7))
plt.plot(cummulate_survivial_ratio)
plt.title('Survival rate change depending on range of Age', y=1.02)
plt.ylabel('Survival rate')
plt.xlabel('Range of Age(0~x)')
plt.show()
```



##### 2.5 Embarked

```python
df_train['Embarked'].unique()
# output : array(['S', 'C', 'Q', nan], dtype=object)

f, ax = plt.subplots(1,1, figsize=(7,7))
df_train[['Embarked'],['Survived']].groupby(['Embarked'], as_index=True).mean().sort_values(by='Survived', ascending=False).plot.bar(ax=ax)
```



피쳐들간의 상관관계

```python
f,ax=plt.subplots(2, 2, figsize=(20,15))
sns.countplot('Embarked', data=df_train, ax=ax[0,0])
ax[0,0].set_title('(1) No. Of Passengers Boarded')
sns.countplot('Embarked', hue='Sex', data=df_train, ax=ax[0,1])
ax[0,1].set_title('(2) Male-Female Split for Embarked')
sns.countplot('Embarked', hue='Survived', data=df_train, ax=ax[1,0])
ax[1,0].set_title('(3) Embarked vs Survived')
sns.countplot('Embarked', hue='Pclass', data=df_train, ax=ax[1,1])
ax[1,1].set_title('(4) Embarked vs Pclass')
plt.subplots_adjust(wspace=0.2, hspace=0.5)
plt.show()
```



##### 2.6 Family - SibSp + Parch

SibSp 와 Parch 를 합쳐 함께 탑승한 가족의 수가 만든다. (FamilySize)

```python
df_train['FamilySize'] = df_train['SibSp'] + df_train['Parch'] + 1
df_test['FamilySize'] = df_test['SibSp'] + df_test['Parch'] + 1
```

```python
print('Maximum size of family', df_train['FamilySize'].max())
print('Maximum size of family', df_train['FamilySize'].min())

# Output : Maximum size of family 11
# Maximum size of family 1
```

```python
f,ax=plt.subplots(1, 3, figsize=(40,10))
sns.countplot('FamilySize', data=df_train, ax=ax[0])
ax[0].set_title('(1) No. Of Passengers Boarded', y=1.02)

sns.countplot('FamilySize', hue='Survived', data=df_train, ax=ax[1])
ax[1].set_title('(2) Survived countplot depending on FamilySize',  y=1.02)

df_train[['FamilySize', 'Survived']].groupby(['FamilySize'], as_index=True).mean().sort_values(by='Survived', ascending=False).plot.bar(ax=ax[2])
ax[2].set_title('(3) Survived rate depending on FamilySize',  y=1.02)

plt.subplots_adjust(wspace=0.2, hspace=0.5)
plt.show()
```



##### 2.7 Fare

```python
fig, ax = plt.subplots(1,1, figsize=(8,8))
g = sns.distplot(df_train['Fare'], color='b', label='Skewness : {:.2f}'.format(df_train['Fare'].skew()), ax=ax)
g = g.legend(loc='best')
```

```python
# NaN 값에 mean() 값 입력
df_test.loc[df_test.Fare.isnull(), 'Fare'] = df_test['Fare'].mean()


```





---

#### KDE (Kernel Density Estimation, 커널 밀도 추정)

https://darkpgmr.tistory.com/147

##### 밀도 추정 (Density Estimation)

데이터란 현실에서 측정되는 랜덤 값, 이런 측정값을 이용해 본질적인 특성을 파악해야 하므로, 많은 수의 데이터가 필요하다. 관측된 데이터들의 분포로부터 본래의 변수의 분포 특성을 추정하고자 하는 것이 밀도 추정이다.

```
예를 들어, 어떤 육교 밑을 통과하는 차량의 일일 교통량을 파악하는게 목적이라고 하자. 이 때의 변수(random variable)는 '일일 교통량'이다. 그리고 실제 육교 위에서 매일 매일 관찰한 값이 데이터이다. 어떤 날은 차가 500대 지나가고, 어떤 날은 300대, 450대, ... 매일 매일 서로 다른 데이터가 나올 수 있다. 하루, 이틀의 관측 결과만 가지고 이 육교의 '일일 교통량'이 무어라고 결론을 내리기는 힘들다. 하지만 이러한 데이터가 한달, 두달, 1년 넘게 쌓이게 되면 우리는 '일일 교통량'이란 변수가 어떤 값의 분포 특성을 갖는지 좀더 정확히 파악할 수 있게 된다. 그리고 어떤 변수가 가질 수 있는 값 및 그 값을 가질 가능성의 정도를 추정하는 것이 density estimation이다.
```

밀도(density)는 수학적으로는 mass/volume으로 정의되지만, 밀도추정(density estimation), 기계학습, 확률, 통계 등에서 말하는 밀도(density)는 확률밀도(probability density)를 의미한다 (확률밀도에서 확률을 생략하고 흔히 밀도라고 표현).



##### Skewness (왜도, 비대칭도;)

[확률 이론](https://ko.wikipedia.org/wiki/확률_이론) 및 [통계학](https://ko.wikipedia.org/wiki/통계학)에서, **비대칭도**(非對稱度, skewness) 또는 **왜도**(歪度)는 [실수](https://ko.wikipedia.org/wiki/실수) 값 [확률 변수](https://ko.wikipedia.org/wiki/확률_변수)의 [확률 분포](https://ko.wikipedia.org/wiki/확률_분포) 비대칭성을 나타내는 지표이다. 왜도의 값은 양수나 음수가 될 수 있으며 정의되지 않을 수도 있다. 왜도가 음수일 경우에는 확률밀도함수의 왼쪽 부분에 긴 꼬리를 가지며 중앙값을 포함한 자료가 오른쪽에 더 많이 분포해 있다. 왜도가 양수일 때는 확률밀도함수의 오른쪽 부분에 긴 꼬리를 가지며 자료가 왼쪽에 더 많이 분포해 있다는 것을 나타낸다. 평균과 중앙값이 같으면 왜도는 0이 된다.




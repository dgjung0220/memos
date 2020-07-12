

## Recap of main ML algorithms

### Families of ML algorithms

- Linear
- Tree-based
- kNN
- Neural Networks



#### Linear Model

![image-20200709203630355](../../upload/image-20200709203630355.png)

- Logistic Regression

- Support Vector Machines

- 하지만 항상 저렇게 딱 나눠질 수는 없다...

  ![image-20200709203746049](../../upload/image-20200709203746049.png)

#### Tree-based

- Decision Tree
- Random Forest
- GBDT (Gradient Boost Decision Tree)
- 테이블 형식의 데이터에 적합, 하지만 분할,정복이 반복되기 때문에 선형 종속성을 캡처하는 것은 어렵다.
- scikit learn, XGBoost, LightGBM 등의 라이브러리  이용

![image-20200709203941139](../../upload/image-20200709203941139.png)

분할과 정복의 방법을 사용하여 하위 분할된 공간을 하위 공간으로 재생성.



#### kNN-based methods

- scikit learn 라이브러리에 잘 구현되어 있다.

![image-20200709204427949](../../upload/image-20200709204427949.png)



#### Neural Networks

- 특별한 종류의 기계 학습 모델
- Tensorflow playground 에서 어떻게 작동하는 지 살펴보자.
- Tensorflow, PyTorch, Lasagne, mxnet, keras 등의 라이브러리



#### No Free Lunch Theorem

공짜 점심은 없어요

"Here is no method which outperforms all other for all tasks" or "For every method we can construct a task for which this particular method will not be the best"



#### Conclusion

- There is no 'silver bullet' algorithm
- Linear models split space into 2 subspaces
- Tree-based methods splits space into boxes
- k-NN methods heavy rely on how to measure points 'closeness'
- Feed-forward NNs produce smooth non-linear decision boundary
- The most powerful methods are **Gradient Boosted Decision Trees** and **Neural Networks**. But you shouldn't underestimate the others.


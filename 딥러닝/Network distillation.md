## Network distillation (Knowledge distillation)

> https://arxiv.org/pdf/1503.02531.pdf

- 네트워크 증류, 2014년 제프리 힌튼, 오리올 비니알스, 제프 딘의 논문 "Distilling the Knowledge in a Neural Network" 라는 논문에서 제시된 개념
- 미리 잘 학습된 큰 네트워크(Teacher network)의 지식을 실제로 사용하고자 하는 작은 네트워크(Student network)에게 전달하는 것
- 일반적으로 딥러닝 모델은 보편적으로 넓고 깊어서 파라미터 수가 많고 연산량이 많으면 feature extraction이 더 잘 되고, 그에 따라서 모델의 목적 성능도 좋아진다.
- 일종의 'compression'의 개념

![img](https://post-phinf.pstatic.net/MjAxOTA2MDRfMjYy/MDAxNTU5NjIzMDcwMzA5.E_NI70jIzQ5dXGtqLP9ZXYlvCl7MOd4_LCTkWr40wSkg.ynMV-0F_WF4t6wP0V1ed7Llx_d34ZHmd0xuXadUIDDgg.JPEG/object.jpg?type=w1200)



### 방법론적 접근

---

![Knowledge Distillation](https://nervanasystems.github.io/distiller/imgs/knowledge_distillation.png)

- soft label 쓰는 이유
  - 정보의 손실없이, Teacher network의 분류 결과를 Student network의 분류 결과와 비교시켜서, Student network가 Teacher network를 모방하도록 학습
- Teacher network의 출력을 모방하여 실제 사용하는 작은 모델인 Student network 가 모방하여 학습함으로써, 상대적으로 적은 Parameter를 가지고 있더라도 모델의 성능을 높인다.



### 기타 경량화 종류

---

#### Neural Network Pruning

- 네트워크 가지치기

- 뉴럴넷 파라미터 중에서 중요도가 떨어지는 파라미터를 찾아 제거하는 방법

- 최초, 몇 개의 파라미터를 사용하는 것이 최적인지 알 수 없기 때문에, 충분한 수의 파라미터를 사용할 수 있도록 Neural Network를 구성

- 학습 완료 후, 파라미터 상태를 확인하여 결과에 영향을 주지 않는 파라미터를 확인

- 결과에 영향이 적은 파라미터를 선택하여 Neural Network로부터 제거

- 영향도가 적은 파라미터라도 제거를 하면 이에 따른 정확도 손실이 발생할 수 있는데, 이러한 정확도 손실을 보정하기 위하여 Pruning한 상태에서 다시 추가 학습을 하기도 하며, 적절한 수준에 도달할 때까지 파라미터 제거와 추가 학습을 여러 차례 반복.

- 더 발전된 형태로 파라미터를 적절하게 그룹화한 후 가지치는 방법에 관한 연구도 있음

  ![img](https://post-phinf.pstatic.net/MjAxOTA2MDNfMjIx/MDAxNTU5NTM4MjAzMjAx.9QAmI7_ip4mtBpFjzT6a1NPVMT5KeX9tdKbA75vZMzsg.GAhBPClhuPzBM6hPtU8AtY4etcI_fcLiiEKY2-ZtrPIg.JPEG/database_img02.jpg?type=w1200)



#### Low-Rank Approximation

- Convolution 연산에 비용을 줄이는 것
- 행렬 곱 연산시 Rank를 줄여 연산함으로써 근사해를 구하더라도 더 빠른 속도로 연산
- Rank를 줄이기 위해 사용할 수 있는 대표적인 방법으로 SVD(Singular Vector Decomposition) 등이 있음



#### Quantization

- 파라미터의 Precision을 적절히 줄여서 연산 효율성을 높이는 방법
- 16bit, 8bit Precision을 사용하는 방법의 경우, 비교적 적은 정확도 손실로 고속 연산이 가능한 경우가 많고, 하드웨어 업체에서 관련 라이브러리를 제공하기도 함.
- 좀 더 과감하게 4bit, 2bit, 1bit 를 사용하는 알고리즘도 연구되고 있으며, 이렇게 적은 수의 bit를 사용하는 알고리즘의 경우에는 학습이 완료된 파라미터를 단순 Quantization하는 것에 더해 학습시에도 적은 수의 Bit를 고려하여 학습하도록 하는 알고리즘도 연구되고 있음.



### Neural Network Distiller

---

> https://nervanasystems.github.io/distiller/index.html

- network compression 을 위한 open source python package
- Pruning Filters and Channels
- Pruning a Language Model
- Quantizing a Language Model
- Quantizing GNMT



### 기타 경량화

---

- Tensorflow lite
- Qualcomm SNPE (Snapdragon Neural Processing Engine??)


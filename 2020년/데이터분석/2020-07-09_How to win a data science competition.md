## How to Win a Data Science Competition

> 코세라 강의 참고, How to Win  a Data Science Competition : Learn from Top Kaggler
>
> https://www.coursera.org/learn/competitive-data-science



### Competiton mecahnics

- Competitions’ concepts
  - Data
    - csv, text, file, db dump, image 등으로 제공
    - description을 읽어보면 feature 추출시 유용
  - Model
    - 거대하고 많은 component로 구성된 모델(stacking)
  - Submission
    - 제출해서 점수 확인
  - Evaluation
    - 모델이 좋은지 측정 -> score (Accuracy, Logistic loss, AUC, RMSE, MAE 등)
  - Leaderboard
    - 리더보드의 랭킹 확인
    - 그러나 이 점수가 최종은 아님
    - 대회중엔 Public Test을 사용하고, 최종 랭킹을 산정할 땐 Private Test를 사용



### Hardware

- Competition 적정 사양 : CPU 4+ cores, 16+ gb ram
- Storage : SSD!!
- Cloud resource : AWS, Azure, GCP



### Software

- Language : Numpy, Pandas, Matplotlib, Scikit-learn
- IDE : jupyter
- Special Packages : XGBoost, Keras, Light GBM, Catboost
- External tools
  - Vowpal Wabbit : 거대한 데이터셋을 핸들링할 때 유용
  - libfm, libffm : sparce한 CTR 데이터를 다룰 때 유용
  - fast_rgf : 또 다른 tree-based 방법


## 생일 문제

생일이 같은 2명이 존재할 확률을 구하는 방법

- 대충 생각하면 366명 이상 모이면 생일이 겹치는 사람이 있을 것 같다.
- 컴퓨터를 통해 이런 것들을 통계적으로 정리할 수 있다. (Statistics for Hackers)
- 최초의 컴퓨터 실험은 1976년 4색 정리가 유명하다. (지도에서 인접한 나라끼리 서로 다른 색을 칠하려면 4색이면 충분하다.)
- 사실 생일문제도 23명만 넘어도 생일이 같을 확률이 50%를 넘는다고 한다. 증명해보자



```python
import random

TRIALS = 100000
same_birthdays = 0

for _ in range(TRIALS):
  
  birthdays = []
  
  for i in range(23):
    birthday = random.randint(1, 365)
    
    if birthday in birthdays:
      same_birthdays += 1
      break
      
    birthdays.append(birthday)
    
print(f'{same_birthdays / TRIALS * 100}%')		# 50.624%    
```

​	

​	23명이 모이는 경우를 십만번 시행하여 확인해보니, 50%가 나왔다.
## 카다네 알고리즘 (Kadane's algorithm)

- 최대 연속 부분합을 구하는 문제
- 카다네 알고리즘은 최대 연속 부분합을 O(N) 으로 구하는 알고리즘

> https://degurii.tistory.com/67



```python 
def maxSubArray(self, nums: List[int]) -> int:
  
  best_sum = -sys.maxsize
  current_sum = 0
  
  for num in nums:
    
    current_sum = max(num, current_sum+num)
    max_sum = max(current_sum. max_sum)
    
  return max_sum
```


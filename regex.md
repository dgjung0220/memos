### regex

---

> [https://greeksharifa.github.io/%EC%A0%95%EA%B7%9C%ED%91%9C%ED%98%84%EC%8B%9D(re)/2018/07/20/regex-usage-01-basic/](https://greeksharifa.github.io/정규표현식(re)/2018/07/20/regex-usage-01-basic/)



##### 총 12개의 메타 문자 

- $ () * + . ? [ \ ^ { |
- 위의 문자들을 찾고자 할 경우, \ (백슬래시)를 붙여 주면 일반 문자처럼 매칭된다. ( \\( == '(' )



##### 평소에는 아니었는데... 메타 문자인 척 하는 애들

- ] - )



##### Match

```python
import re

matchObj = re.match('a', 'a') # 'a'가 'a'로 시작하니
print(matchObj)

print(re.match('a', 'aba'))
print(re.match('a', 'bbb'))	# None. 문자열의 시작이 'a' 매치되는지 확인
print(re.match('a', 'baa'))	# None.
```

##### Search

```python
matchObj = re.search('a', 'a')	# (0,1)
print(matchObj)

print(re.search('a', 'aba'))	# (0,1)
print(re.search('a', 'bbb'))	# None
print(re.search('a', 'baa'))	# (1,2)
```

​	최초 일치하는 부분을 인덱스로 넘겨준다.








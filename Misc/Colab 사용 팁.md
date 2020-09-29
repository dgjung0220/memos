### 파일 업로드

#### 방법1. 직접 업로드

```python
from google.colab import files
myfile = files.upload()
```

```python
import io
import pandas as pd
```

```python
data = pd.read_csv(io.BytesIO(myfile['파일이름.csv']))
```



#### 방법2. 드라이브에서 가져오기

```python
from google.colab import drive
drive.mount('/content/drive')
```

```python
filename = 'drive 파일 경로.csv'
data = pd.read_csv(filename)
```



### github 소스 코랩에서 바로 열기

- github.com -> github 으로 변경
- colab.research.google.com 을 제일 앞 도메인에 추가
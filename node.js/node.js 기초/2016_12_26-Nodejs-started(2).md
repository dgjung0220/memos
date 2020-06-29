## Node.js started (2)

---

### NPM을 이용한 모듈 설치

UNDERSCORE.js 를 모듈로 사용하는 것으로 예를 듬. (http://underscorejs.org/)

$npm install underscore 명령어 치기 전에!! 

디렉터리 자체를 일종의 npm 모듈처럼 모듈화 해야 한다. (npm init)

Npm init 하면, 뭐 자질구레한 걸 엄청 물어본다. 영어 읽어보면 다 아니까 대충 적거나 엔터 쳐서 넘어가기..

그러면 디렉터리에 package.json 이 생긴다.

- 결국 npm init 이 하는 역할은, package.json을 자동으로 만들어 주는 것이다. 열어보면 앞서 설정했던 정보들이 써있다. 

  

이제 다시 npm install underscore를 치면,

![underscore  @ LICENSE  package.json  EE README.md  underscore-min.js  underscore-min.map  underscore.js ](../../upload/Sat,%2027%20Jun%202020%20170535.png)

- Node_modules 라는 폴더 생성과 함께, underscore 모듈이 설치되었다. 이 역할을 npm이 한 것!

 

$ npm install underscore --save 

- --save 옵션을 사용하면, 의존성까지 추가해서 설치된다. (package.json을 보면 추가된 것을 확인.)
- 언제든지 의존성 추가된 모듈을 포함할 수 있다는 의미.

---

### 모듈 사용법 (Underscore)

Underscore 에는 상당히 많은 메소드들이 있다. 잘 쓰는 방법을 익혀두자. http://underscorejs.org/

const _= require('underscore');  // underscore 는 보통 상수명을  _로 쓴다. 기능 대박 많다. 제발 정리.

```javascript
const _ = require('underscore')

var arr = [3,6,9,1,12];

console.log(arr[0]);
console.log(_.first(arr));

console.log(arr[arr.length-1]);
console.log(_.last(arr));
```

---

### Callback

JavaScript Sort() method를 예로 들자. 똑똑이들은 보면 콜백에 대해 뭔 말인지 안다.

![Syntax  array. sort ( compareFunction )  Parameter Values  Parameter  compa reFunc tion  Description  Optional. A function that defines an altemative sort order. The function should retum  a negative, zero, or positive value, depending on the arguments, like:  function(a, b){retum a-b}  When the sort() method compares two values, it sends the values to the compare  function, and sorts the values according to the retumed (negative, zero, positive)  value.  Example:  When comparing 40 and 100, the sort() method calls the compare function(40,100).  The function calculates 40-100, and retums -60 (a negative value).  The sort function will sort 40 as a value lower than 100. ](../../upload/Sat,%2027%20Jun%202020%20170818.png)

 

![undef ined  undef ined  undef ined  undef ined  undef ined  console. log(a);  a.sort(); console. log(a);  function b(vl ,  function b(vl ,  v2)freturn v2-v1Y ;  v2)freturn v 1-v2Y ;  a. sort(b);  a. sort(b);  console. log(a);  console. log(a); ](../../upload/Sat,%2027%20Jun%202020%20170821.png)

![funct ion  v2  console.  log  c  return v2-v1  console.  log(a  c  c  c ](../../upload/Sat,%2027%20Jun%202020%20170822.png)

-  익명 함수의 콜백 펑션화

![a.sort(funct ion(vl ,v2){return v2-v1 ; } ) ; console. log(a) ;  undef ined ](../../upload/Sat,%2027%20Jun%202020%20170825.png)

---

### 동기 & 비동기

​	File System 살펴 보기. 보면, 같은 메소드에 뒤에 Sync 라고 붙은 애들이 있다.  아무 것도 안 붙어 있는 애들은 비동기적으로 발생하는 것들이다. (node.js 는 기본적으로 비동기적으로 작동한다! 특별히 동기적으로 사용되고 싶은 경우만, sync 가 붙은 메소드를 사용한다. 근데 비추하고 있다.)

 http://www.nextree.co.kr/p7292/ (비동기 프로그래밍 이해 참고)

![fs.readFile(file[, options], callback)  Added in: vO.1.29  I I filename or file descriptor  • file  (String >  options (Object) I (String>  o encoding < String) I (Null > default = null  o flag (String> default  • callback < Function>  Asynchronously reads the entire contents of a file. Example:  fs. readFi1e  /etc/passwd',  if (err) throw err;  console. log(data) ;  , data)  The callback is passed two arguments (err, data) , where data is the contents of the file.  If no encoding is specified, then the raw buffer is returned.  If options is a string, then it specifies the encoding. Example:  fs. readFi1e  /etc/passwd',  'utf8',  callback) ;  Any specified file descriptor has to support reading.  Note: If a file descriptor is specified as the file , it will not be closed automatically. ](../../upload/Sat,%2027%20Jun%202020%20170950.png)

![const fs  — require('fs');  console. log(l) ;  var data = fs.readFi1eSync( 'data. txt', {encoding: 'utf8'  {encoding: utf8  console. log(data);  Async  console. log(2) ;  fs. readFi1e( 'data. txt',  console. log(3) ;  console. log(data) ;  console. log(4) ;  function (err,  data){ ](../../upload/Sat,%2027%20Jun%202020%20170951.png)

![C: fiworkspacefij s_workspacefiservers de_j avascr ipt>node sync_async js  Hel 10 Sync And ASync  4  Hel 10 Sync And ASync ](../../upload/Sat,%2027%20Jun%202020%20170947.png)
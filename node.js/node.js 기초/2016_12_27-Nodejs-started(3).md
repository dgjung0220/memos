## Node.js started (3)

---

### Express (1)

1. Express 도입

   expressjs.com (들어 가면, Korean 도 있다!)

2. Express 설치

   위의 홈페이지 참조.

   $ npm install --save express

3. Express 사용한 웹앱 만들기.

   Main Application (= entry point), Express 에서 권장하는 entry point 는 App.js

 URL 치고 들어오는 GET 방식

<img src="../../upload/Sat,%2027%20Jun%202020%20171148.png" alt="img" style="zoom:150%;" />

사용자 > 라우터 > 컨트롤러

ex) User -> get.('/') -> send('Hello World')

User -> get.('/login') -> send('login please')

---

### Express(2)

- 1. Express 정적 파일 서비스하는 방법.

     ```javascript
     var express = require('express')
     var app = express();
     
     app.use(express.static('public'))
     ```

     - Public 폴더의 파일들이 정적으로 제공됨. (localhost:3000/test.jpg)

     ```javascript
     var express = require('express')
     var app = express()
     
     app.use(express.static('public'))
     
     app.get('/', function (req, res) {
         res.send('Hello Router, <img src="/test.jpg">')
     }) 
     
     app.get('/login', function(req, res) {
         res.send('Hello Router, <img src="/test.jpg">')
     })
     
     app.get('/login', function(req, res) {
         res.send('<h1> Log in please.</h1>')
     })
     
     app.listen(3000, function(){
         console.log('Example app listening on port 3000!')
     })
     ```

- 2. 웹페이지를 표현하는 방법

     정적 - 한 번 만들면 항상 동일한 웹페이지 (public 안에 html 파일을 제공하는 것.)

     소스가 수정되어도, 해당 소스를 불러오는 형식이기 때문에, 서버 재실행 필요없음.

     

     **동적**

     ```javascript
     app.get('/dynamic', function(req, res) {
         var output = `
     	
     	<!DOCTYPE html>
     	<html>
     		<head>
     			<meta charset="utf-8">
     			<title></title>
     		</head>
     		<body>
     			hello, dynamic!
     		</body>
     	</html>`
         
         res.send(output)
         
     })
     ```

     - 동적으로 만들 경우, 다시 실행되어야 하기 때문에, 서버 자체를 다시 실행해야 함.
     - Output 에 쓰인 `` 는 물결 아래 있는 거임. 그레이브스 악센트!?!?
     - 재실행임에도 동적으로 사용하는 이유? (장,단이 있다.)
     - 템플릿 엔진을 이용하여, 장 단점 모두 합쳐 쓰는 법을 배우자.

     ```javascript
     app.get('/dynamic', function(req, res) {
         
         var lis = ''
         for (var i = 0; i < 5; i++) {
             lis = lis + '<li>coding</li>'
         }
         
         var time = Date()
         var output=`
     		
     		<!DOCTYPE html>
     		<html>
     			<head>
     				<meta charset="utf-8">
     				<title></title>
     			</head>
     			<body>
     				hello, dynamic!
     				<ul>
     					${lis}
     				</ul>
     				${time}
     			</body>
     		</html>`
     
     })
     ```

     ---

     ### Express(3) 템플릿 엔진

     


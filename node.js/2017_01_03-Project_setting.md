## 프로젝트 설정

---

### 프로젝트 --save 모듈

```shell
$ npm install body-parser --save
$ npm install express --save
$ npm install pug --save
$ npm install orientjs --save 
```



### 프로젝트 초기 설정 (Source Base)

```javascript
var express = require('express');
var app = express();
var route = require('./route.js');
var bodyParser = require('body-parser');
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended: true}));
app.use(express.static('semantic'));
app.locals.pretty = true;
app.set('view engine', 'pug');
app.set('views', './views');
app.use('/', route);

app.listen(3000, function() {
  console.log("listening localhost 3000 port");
})
```



### Semantic UI

```shell
$ npm install –g gulp
$ npm install semantic-ui –save
$ cd semantic
$ gulp build
```



### Security

```shell
$ npm install md5 --save
```


### Handlebar View Engine

```shell
$ npm install express-handlebars --save
```



### Directory Structure

```
.
├── app.js
└── views
    ├── home.handlebars
    └── layouts
        └── main.handlebars

2 directories, 3 files
```



### index.js

```javascript
var express = require('express')
var exphs = require('express-handlebars')

var app = express()
app.engine('handlebars', exphs())
app.set('view engine', 'handlebars')

app.get('/', function (req, res) {
    res.render('home')
}) 

app.listen(3000)
```



### views/layouts/main.handlebars

### views/home.handlebars


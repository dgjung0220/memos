## Node.js 에서 MongoDB 사용하기

---

### Mongodb node.js

> http://mongodb.github.io/node-mongodb-native/2.2/quick-start/quick-start/



#### Create the package.json file

```powershell
mkdir mongodbProject
cd mongodbProject

npm init
npm install mongodb@3.5.9 --save
```



#### Connect to MongoDB

```javascript
var MongoClient = require('mongodb').MongoClient
  , assert = require('assert');

// Connection URL
var url = 'mongodb://localhost:27017/myproject';

// Use connect method to connect to the server
MongoClient.connect(url, function(err, db) {
  assert.equal(null, err);
  console.log("Connected successfully to server");

  db.close();
});
```


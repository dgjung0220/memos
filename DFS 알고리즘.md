```javascript
// https://twpower.github.io/151-bfs-dfs-basic-problem
//https://smilerici.tistory.com/71

class Stack {
    constructor() { this._arr = [] }
    push(item) { this._arr.push(item) }
    pop(item) { return this._arr.pop(item) }
    peek() { return this._arr[this._arr.length - 1] }
}

const dx = [-1, 0, 1, 0]
const dy = [0, 1, 0, -1]
const MAX_SIZE = 25

var n   
var group_id
const groups = new Array()
const map = new Array(Array(MAX_SIZE), Array(MAX_SIZE))
const visited = new Array(Array(MAX_SIZE), Array(MAX_SIZE))         // boolean type

function dfs_stack(position) {
    const stack = new Stack()
    stack.push(position)

    // visit first time in position
    //visited[position.x * 1][position.y * 1] = true
    //groups[group_id]++

    console.log(typeof visited)
    console.log(position.x, position.y)
    console.log(stack)
}

dfs_stack({'x' : '2', 'y' : '3'})
```

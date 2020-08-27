### Alexnet parameter count

---

> https://seongkyun.github.io/study/2019/01/25/num_of_parameters/

| Layer Name | Tensor Size         | Weights                       | Biases | Parameters |
| ---------- | ------------------- | ----------------------------- | ------ | ---------- |
| Input      | 224 x 224 x 3       | 0                             | 0      | 0          |
| Conv-1     | (55 x 55 x 48 ) x 2 | (11 x 11 x 3) x 96 = 34,848   | 96     | 34,944     |
| MaxPool-1  | (27 x 27 x 96)      | 0                             | 0      | 0          |
| Conv-2     | (27 x 27 x 128) x 2 | (5 x 5 x 48) x 256 = 307,200  | 256    | 307,456    |
| MaxPool-2  | (13 x 13 x 256)     | 0                             | 0      | 0          |
| Conv-3     | (13 x 13 x 192) x 2 | (3 x 3 x 256) x 384 = 884,736 | 384    | 885,120    |
| Conv-4     | (13 X 13 X 192) X 2 | (3 x 3 x 192) x 384 = 663,552 | 384    | 663,936    |
| Conv-5     | (13 x 13 x 128) x 2 | (3 x 3 x 192) x 256 = 442,368 | 256    | 442,624    |
| MaxPool-3  | (13 x 13 x 2048)    |                               |        |            |
| FC-1       |                     |                               |        |            |
| FC-2       |                     |                               |        |            |
| FC-3       |                     |                               |        |            |
| Output     |                     |                               |        |            |
| Total      |                     |                               |        |            |


## Neural Network Pruning

> https://www.tensorflow.org/model_optimization/guide/pruning?hl=ko

- 중요하지 않은 가중치 다듬기
- tensorflow keras 에서 지원하는 pruning API 사용하기

```
$ pip install -q tensorflow-model-optimization
```

```python
import tempfile
import os

import tensorflow as tf
import numpy as np

from tensorflow import keras

%load_ext tensorboard
```

---



### Pruning 없이 학습하기

- 먼저 MNIST 데이터셋을 이용해서 프루닝없이 딥러닝 학습시킨다.

```python
# MNIST Training without Pruning
mnist = keras.datasets.mnist
(train_X, train_Y), (test_X, test_Y) = mnist.load_data()

train_X = train_X / 255.0
test_X = test_X / 255.0
```

```python
model = keras.Sequential([
                          keras.layers.InputLayer(input_shape=(28,28)),
                          keras.layers.Reshape(target_shape=(28, 28, 1)),
                          keras.layers.Conv2D(filters=12, kernel_size=(3,3), activation='relu'),
                          keras.layers.MaxPooling2D(pool_size=(2,2)),
                          keras.layers.Flatten(),
                          keras.layers.Dense(10)
])

model.compile(optimizer='adam', loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

model.summary()
```

```
Model: "sequential"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
reshape (Reshape)            (None, 28, 28, 1)         0         
_________________________________________________________________
conv2d (Conv2D)              (None, 26, 26, 12)        120       
_________________________________________________________________
max_pooling2d (MaxPooling2D) (None, 13, 13, 12)        0         
_________________________________________________________________
flatten (Flatten)            (None, 2028)              0         
_________________________________________________________________
dense (Dense)                (None, 10)                20290     
=================================================================
Total params: 20,410
Trainable params: 20,410
Non-trainable params: 0
_________________________________________________________________
```

- convolution layer 1개와 maxpooling layer 를 이용하여 특징추출기를 만들고, Dense layer로 결과를 냈다. 간단함

```python
model.fit(train_X, train_Y, epochs=4, validation_split=0.1)

_, baseline_model_accuracy = model.evaluate(
    test_X, test_Y, verbose=0
)

print('Baseline model accuracy: ', baseline_model_accuracy)

_, keras_file = tempfile.mkstemp('.h5')
tf.keras.models.save_model(model, keras_file, include_optimizer=False)
print('Saved baseline model to : ', keras_file)
```

```python
Baseline model accuracy:  0.9768000245094299
Saved baseline model to :  /tmp/tmpoz9xtky7.h5
```

- epoch 4의 학습으로 정확도 98% 모델이 만들어졌다.
- h5로 모델을 저장하고 나중에 크기를 비교해볼 것이다.

---



### Fine-tune with Pruning

```python
import tensorflow_model_optimization as tfmot

prune_low_magnitude = tfmot.sparsity.keras.prune_low_magnitude
batch_size = 128
epochs = 2

validation_split = 0.1
num_images = train_X.shape[0] * (1 - validation_split)
end_step = np.ceil(num_images / batch_size).astype(np.int32) * epochs

# Define model for pruning
pruning_params = {
    'pruning_schedule' : tfmot.sparsity.keras.PolynomialDecay(initial_sparsity=0.50, final_sparsity=0.80, begin_step = 0, end_step=end_step) }

# 기존 model을 파라미터로...
model_for_pruning = prune_low_magnitude(model, **pruning_params)

# recompile
model_for_pruning.compile(optimizer='adam',loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),metrics=['accuracy'])

model_for_pruning.summary()
```

- tfmot

  - Tensorflow model optimization python API
  - ``clustering``, ``quantization``, ``sparsity`` 3가지 모듈이 있다.
- prune_low_magnitude 설정 후, pruning을 위한 모델을 재정의한다.
- 기존 모델에 재정의된 모델로 다시 컴파일한다.
- ``prune_low_magnitude`` : 모델이나 레이어에 프루닝을 적용한다. 예를 들어 50% sparsity를 적용하면 레이어의 가중치에 50%는 0이 되도록 보장한다.
- ``PolynomialDecay`` : 프루닝 스케쥴을 지정한다. 위의 코드에서 프루닝 시작시 50% sparsity, 끝날 때 80%를 설정했고, begin_step, end_step은 프루닝의 시작,종료 시점을 지정할 수 있다.

```
Model: "sequential"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
prune_low_magnitude_reshape  (None, 28, 28, 1)         1         
_________________________________________________________________
prune_low_magnitude_conv2d ( (None, 26, 26, 12)        230       
_________________________________________________________________
prune_low_magnitude_max_pool (None, 13, 13, 12)        1         
_________________________________________________________________
prune_low_magnitude_flatten  (None, 2028)              1         
_________________________________________________________________
prune_low_magnitude_dense (P (None, 10)                40572     
=================================================================
Total params: 40,805
Trainable params: 20,410
Non-trainable params: 20,395
_________________________________________________________________
```

각 레이어들이 pruning 설정한 레이어로 변경되었다. 그러면서 파라미터의 숫자가 왠지 늘었다.

하지만 Trainable params의 갯수는 동일하다.

```python
logdir = tempfile.mkdtemp()

callbacks = [
  tfmot.sparsity.keras.UpdatePruningStep(),
  tfmot.sparsity.keras.PruningSummaries(log_dir=logdir),
]
  
model_for_pruning.fit(train_X, train_Y, batch_size=batch_size, epochs=epochs,
                      validation_split=validation_split,callbacks=callbacks)
```

```python
_, model_for_pruning_accuracy = model_for_pruning.evaluate(test_X, test_Y, verbose=0)

print('Baseline test accuracy:', baseline_model_accuracy) 
print('Pruned test accuracy:', model_for_pruning_accuracy)
```

학습 후 결과를 보면 97.6%, 97.3%로 추론 성능은 크게 차이가 없다. 모델 파일 크기는 각각 78121.00 bytes, 30780.00 bytes 로 약 2배정도 줄어들었다.

---

#### 파일 크기 측정

gzip 압축 후 사이즈를 측정했다.

```python
def get_gzipped_model_size(file):
  # Returns size of gzipped model, in bytes.
  import os
  import zipfile

  _, zipped_file = tempfile.mkstemp('.zip')
  with zipfile.ZipFile(zipped_file, 'w', compression=zipfile.ZIP_DEFLATED) as f:
    f.write(file)

  return os.path.getsize(zipped_file)
```

```python
print("Size of gzipped baseline Keras model: %.2f bytes" % (get_gzipped_model_size(keras_file)))
print("Size of gzipped pruned keras fine_tune model: %.2f bytes" % (get_gzipped_model_size(keras_pruning_file)))
```



---



### 3x smaller model 만들기 (Strip_pruning, TFLiteConverter)

- ``tfmot.sparsity.keras.strip_pruning`` : strip_pruning은 학습 중에만 필요로 하는 모든 tf.Variable 을 제거한다. 
- 표준 압축 알고리즘을 적용

```python
model_for_export = tfmot.sparsity.keras.strip_pruning(model_for_pruning)

_, pruned_keras_file = tempfile.mkstemp('.h5')
tf.keras.models.save_model(model_for_export, pruned_keras_file, include_optimizer=False)
print('Saved pruned Keras model to : ', pruned_keras_file)
```

```python
converter = tf.lite.TFLiteConverter.from_keras_model(model_for_export)
pruned_tflite_model = converter.convert()

_, pruned_tflite_file = tempfile.mkstemp('.tflite')

with open(pruned_tflite_file, 'wb') as f:
  f.write(pruned_tflite_model)

print('Saved pruned TFLite model to : ', pruned_tflite_file )
```

```python
print("Size of gzipped baseline Keras model: %.2f bytes" % (get_gzipped_model_size(keras_file)))
print("Size of gzipped pruned keras fine_tune model: %.2f bytes" % (get_gzipped_model_size(keras_pruning_file)))
print("Size of gzipped pruned Keras model: %.2f bytes" % (get_gzipped_model_size(pruned_keras_file)))
print("Size of gzipped pruned TFlite model: %.2f bytes" % (get_gzipped_model_size(pruned_tflite_file)))
```

```
Size of gzipped baseline Keras model: 78121.00 bytes
Size of gzipped pruned keras fine_tune model: 30780.00 bytes
Size of gzipped pruned Keras model: 25641.00 bytes
Size of gzipped pruned TFlite model: 24991.00 bytes
```

- 기존 모델 78.1kb 에서 24.99kb 로 크게 줄었다.



### 10x smaller model (양자화 적용, quantization)

- post-training quantization 적용하기 (사후 훈련 양자화)

```python
converter = tf.lite.TFLiteConverter.from_keras_model(model_for_export)
converter.optimizations = [tf.lite.Optimize.DEFAULT]
quantized_and_pruned_tflite_model = converter.convert()

_, quantized_and_pruned_tflite_file = tempfile.mkstemp('.tflite')

with open(quantized_and_pruned_tflite_file, 'wb') as f:
  f.write(quantized_and_pruned_tflite_model)

print('Saved quantized and pruned TFLite model to:', quantized_and_pruned_tflite_file)

print("Size of gzipped baseline Keras model: %.2f bytes" % (get_gzipped_model_size(keras_file)))
print("Size of gzipped pruned and quantized TFlite model: %.2f bytes" % (get_gzipped_model_size(quantized_and_pruned_tflite_file)))
```

- 이전 tflite convert 코드에서 ``converter.optimizations = [tf.lite.Optimize.DEFAULT]`` 만 추가되었다. 그런데 결과는 78.121kb 에서 7.8kb 로 10배 줄었다.



---



### 압축된 모델 사용하기

> https://www.tensorflow.org/lite/guide/inference#load_and_run_a_model_in_python

- 압축된 모델을 사용하려면 아래와 같은 귀찮은 과정을 거쳐야 한다.

#### Running a model

Running a TensorFlow Lite model involves a few simple steps:

1. Load the model into memory.
2. Build an `Interpreter` based on an existing model.
3. Set input tensor values. (Optionally resize input tensors if the predefined sizes are not desired.)
4. Invoke inference.
5. Read output tensor values.

Following sections describe how these steps can be done in each language.

```python
# Load the TFLite model and allocate tensors
#interpreter = tf.lite.Interpreter(model_content=quantized_and_pruned_tflite_model)
interpreter = tf.lite.Interpreter(model_path="/tmp/tmpkq91mpm8.tflite")
interpreter.allocate_tensors()

# Get input and output tensors
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

input_index = interpreter.get_input_details()[0]["index"]
output_index = interpreter.get_output_details()[0]["index"]

# Test the model
test_image = np.expand_dims(test_X[0], axis=0).astype(np.float32)
interpreter.set_tensor(input_index, test_image)

interpreter.invoke()

# Post-processing: remove batch dimension and find the digit with highest probability.
output = interpreter.tensor(output_index)
print(output())
digit = np.argmax(output()[0])
print(digit)
```


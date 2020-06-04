import tensorflow as tf
import numpy as np

x = tf.constant(np.random.rand(32).astype(np.float32))
y = tf.constant([1,2,3])

print(x)
print(y)
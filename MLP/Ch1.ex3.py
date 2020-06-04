import tensorflow as tf
import numpy as np

sess = tf.compat.v1.Session()
x_data = np.array([[1.,2.,3.],[3.,2.,6.]])
x = tf.convert_to_tensor(x_data, dtype=tf.float32)
print(x)
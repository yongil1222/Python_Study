import tensorflow as tf

a = tf.constant(1)
b = tf.constant(2)
c = tf.add(a, b)

sess = tf.Session()

print (sess.run(c))
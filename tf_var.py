import tensorflow as tf

a = tf.Variable(5)
b = tf.Variable(3)
c = tf.multiply(a, b)
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)
print(sess.run(c))

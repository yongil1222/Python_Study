import tensorflow as tf

input = [1, 3, 5, 7, 9]

x = tf.placeholder(dtype=tf.float32)
y = x * 5

sess = tf.Session()

print(sess.run(y, feed_dict={x: input}))
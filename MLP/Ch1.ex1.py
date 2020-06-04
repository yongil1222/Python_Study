import tensorflow as tf

ses = tf.compat.v1.Session()
tens1 = tf.constant([[[1,2],[2,3]],[[3,4],[5,6]]])
print(ses.run(tens1)[1,1,0])


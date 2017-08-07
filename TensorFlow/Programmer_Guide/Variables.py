import tensorflow as tf

weights = tf.Variable(tf.random_normal([784,200], stddev=0.35), name = "weight")
biases = tf.Variable(tf.zeros([200]), name = "biases")

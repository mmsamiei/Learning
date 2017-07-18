import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets("MNIST_data", one_hot=True)
# one_hot attribute is for lable form 0 to 9
x = tf.placeholder(tf.float32, [None, 784])
# 784 = 28 * 28
W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))
y = tf.nn.softmax(tf.matmul(x, W) + b)
# this line define model for us
# note that y is an 10x1 matrix
y_ = tf.placeholder(tf.float32, [None, 10])
# this placeholder keep correct answers
cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y), reduction_indices=[1]))
# reduce sum, sum element in second dimension and then reduce it due to reduction indecis
train_step = tf.train.GradientDescentOptimizer(0.05).minimize(cross_entropy)
# it is only an optimization algorithms
sess = tf.InteractiveSession()
tf.global_variables_initializer().run()
for _ in range(1000):
    batch_xs, batch_ys = mnist.train.next_batch(100)
    # Each step of the loop we get batch of one hundred random data points from out training set
    sess.run(train_step, feed_dict={x: batch_xs, y_:batch_ys})
correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
# cast because the correct_prediction is boolean matrix
print(sess.run(accuracy, feed_dict={x: mnist.test.images, y_:mnist.test.labels}))


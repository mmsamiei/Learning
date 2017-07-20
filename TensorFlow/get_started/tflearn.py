from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import urllib

import tensorflow as tf
import numpy as np

IRIS_TRAINING = "iris_training.csv"
IRIS_TRAINING_URL = "http://download.tensorflow.org/data/iris_training.csv"

IRIS_TEST = "iris_test.csv"
IRIS_TEST_URL = "http://download.tensorflow.org/data/iris_test.csv"

if not os.path.exists(IRIS_TRAINING):
    raw = urllib.request.urlopen(IRIS_TRAINING_URL).read()
    with open(IRIS_TRAINING,'wb') as f:
        f.write(raw)
# download if train does not exist on computer

if not os.path.exists(IRIS_TEST):
    raw = urllib.request.urlopen(IRIS_TEST_URL).read()
    with open(IRIS_TEST,'wb') as f:
        f.write(raw)
training_set = tf.contrib.learn.datasets.base.load_csv_with_header(
        filename = IRIS_TRAINING,
        target_dtype=np.int,
        features_dtype=np.float32)
test_set = tf.contrib.learn.datasets.base.load_csv_with_header(
        filename = IRIS_TEST,
        target_dtype = np.int,
        features_dtype = np.float32)
feature_columns = [tf.contrib.layers.real_valued_column("", dimension=4)]
classifier = tf.contrib.learn.DNNClassifier(feature_columns = feature_columns,
        hidden_units = [10, 20, 10],
        n_classes=3, #three target class
        model_dir="/tmp/iris_model")
def get_train_inputs():
    x = tf.constant(training_set.data)
    y = tf.constant(training_set.target)
    return x, y
classifier.fit(input_fn = get_train_inputs, steps=2000)

def get_test_inputs():
    x = tf.constant(test_set.data/0)
    y = tf.constant(test_set.target)
    return x, y

accuracy_score = classifier.evaluate(input_fn=get_test_inputs, steps=1)["accuracy"]
print("\nTest Accuracy: {0:f}\n".format(accuracy_score))



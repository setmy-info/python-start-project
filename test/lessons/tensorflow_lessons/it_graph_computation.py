import unittest

import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow import keras


def prepare_iris_dataset():
    iris = load_iris()
    iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    iris_df['target'] = iris.target
    iris_df.to_csv('iris_dataset.csv', index=False)


class Test(unittest.TestCase):

    def test_graph_computation(self):
        print("Tensorflow: " + tf.__version__)
        graph = tf.Graph()
        graph_dir = "./graph"
        with graph.as_default() as g:
            # Constant 1-D Tensor from a python list. Setting the name and type.
            tensor_1_d = tf.constant([1, 2, 3, 4, 5, 6], name='tensor_1_d', dtype=tf.int32)
            print("1-D tensor: " + str(tensor_1_d))
            print("1-D tensor shape: " + str(tensor_1_d.shape))
            print("1-D tensor shape: " + str(tensor_1_d.shape[0]))
            # Belongs to graph
            assert tensor_1_d.graph is graph

            # Constant 2-D Tensor from a numpy array. With automatic name.
            numpy_array_2_d = np.array([[1, 2, 3], [4, 5, 6]])
            tensor_2_d = tf.constant(numpy_array_2_d)
            print("2-D tensor: " + str(tensor_2_d))
            print("2-D tensor shape: " + str(tensor_2_d.shape))
            print("2-D tensor shape: " + str(tensor_2_d.shape[0]))
            print("2-D tensor shape: " + str(tensor_2_d.shape[1]))
            # Belongs to graph
            assert tensor_2_d.graph is graph

            float_tensor = tf.constant([1, 2, 3, 4, 5, 6], name="float_tensor", dtype=tf.float64)
            print("1-D floats tensor: " + str(float_tensor))

            var_a = tf.Variable([1.0], name="var_a_tensor")
            print("1-D floats variable: " + str(var_a))

            var_b = tf.Variable(1.0, name="var_b_tensor")
            print("floats variable b: " + str(var_b))

            # Define operations and tensors in `graph`.
            a = tf.constant(2.2, name="a")
            b = tf.constant(3.3, name="b")
            c = tf.add(a, b)
            # c = a + b
            print("a is tensor: " + str(a) + ", b is tensor: " + str(b) + ", c is tensor: " + str(c))
            assert a.graph is graph
            assert b.graph is graph
            assert c.graph is graph
            # a_value = a.numpy()
            # b_value = b.numpy()
            # c_value = c.numpy()
            print("c=", c)

    def test_graph_computation_2(self):
        graph_name = "c.h5"
        a = tf.Variable(2.0, name="a", dtype=tf.float64)
        b = tf.constant(3.0, name="b", dtype=tf.float64)

        class GraphModel(tf.Module):
            def __init__(self, a, b):
                super(GraphModel, self).__init__()
                self.a = a
                self.b = b
                self.c = self.a + self.b

        model = GraphModel(a, b)
        print(model.c)
        tf.saved_model.save(model, graph_name)

    def test_iris_training(self):
        # prepare_iris_dataset()
        iris_df = pd.read_csv('test/lessons/tensorflow_lessons/iris_dataset.csv')
        X = iris_df.drop('target', axis=1).values
        y = iris_df['target'].values
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        scaler = StandardScaler()
        X_train = scaler.fit_transform(X_train)
        X_test = scaler.transform(X_test)

        model = keras.Sequential([
            keras.layers.Input(shape=(4,)),
            keras.layers.Dense(64, activation='relu'),
            keras.layers.Dense(64, activation='relu'),
            keras.layers.Dense(64, activation='relu'),
            keras.layers.Dense(3, activation='softmax')
        ])
        model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
        model.fit(X_train, y_train, epochs=100, batch_size=32, validation_split=0.2)
        model.save('keras_iris_model.h5')
        loaded_model = keras.models.load_model('keras_iris_model.h5')
        loss, accuracy = loaded_model.evaluate(X_test, y_test)
        print(f'Accuracy with test data: {accuracy * 100}%')


if __name__ == "__main__":
    unittest.main()

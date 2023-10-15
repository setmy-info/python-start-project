import unittest

import numpy as np
import tensorflow as tf


class Test(unittest.TestCase):

    def test_graph_computation(self):
        print("Tensorflow: " + tf.__version__)
        graph = tf.Graph()
        g = graph
        with graph.as_default():
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

            # Define operations and tensors in `graph`.
            a = tf.constant(2.2, name="a")
            b = tf.constant(3.3, name="b")
            c = tf.add(a, b)
            print("a is tensor: " + str(a) + ", b is tensor: " + str(b) + ", c is tensor: " + str(c))
            a_value = a.numpy()
            b_value = b.numpy()
            c_value = c.numpy()
            print("a=", a_value, ", b=", b_value, ", c=", c_value)
            assert a.graph is graph
            assert b.graph is graph
            assert c.graph is graph


if __name__ == "__main__":
    unittest.main()

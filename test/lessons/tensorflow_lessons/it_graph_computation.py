import unittest

import numpy as np
import tensorflow as tf


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


if __name__ == "__main__":
    unittest.main()

import unittest
import numpy as np
import os
import PIL
import PIL.Image
import tensorflow as tf
import tensorflow_datasets as tfds
import tensorflow_transform as tft
import tensorflow_transform.beam as tft_beam

from tensorflow_transform.tf_metadata import dataset_metadata
from tensorflow_transform.tf_metadata import schema_utils

from tfx_bsl.public import tfxio
import pathlib


# https://colab.research.google.com/github/tensorflow/docs/blob/master/site/en/tutorials/quickstart/beginner.ipynb
# https://www.tensorflow.org/tutorials/keras/classification
# https://github.com/zalandoresearch/fashion-mnist
# https://www.tensorflow.org/tutorials/load_data/images
# https://www.tensorflow.org/guide/keras/sequential_model
# https://www.tensorflow.org/tutorials/load_data/csv
# https://archive.ics.uci.edu/ml/datasets/abalone
# https://blog.tensorflow.org/2019/02/introducing-tensorflow-datasets.html
# https://www.tensorflow.org/datasets/overview
class Test(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_name(self):
        print("Tensorflow: " + tf.__version__)

    def test_dataset_names_list(self):
        data_sets = tfds.list_builders()
        print(str(data_sets))
        pass

    def test_download_flower_pics(self):
        dataset_url = "https://storage.googleapis.com/download.tensorflow.org/example_images/flower_photos.tgz"
        archive = tf.keras.utils.get_file(origin=dataset_url, extract=True)
        # C:\Users\USERNAME\.keras\datasets\flower_photos
        data_dir = pathlib.Path(archive).with_suffix('')
        self.assertEqual('TF Test', 'TF Test')

    def test_download_mnist(self):
        # http://yann.lecun.com/exdb/mnist/
        datasets = tfds.load("mnist")
        # C:\Users\USERNAME\tensorflow_datasets
        train_dataset, test_dataset = datasets["train"], datasets["test"]
        self.assertEqual('TF Test', 'TF Test')


if __name__ == "__main__":
    unittest.main()

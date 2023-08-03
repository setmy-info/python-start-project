# python-start-project

## Notes

For [Tensorflow 2.11.0 (at the moment the latest version)](https://pypi.org/project/tensorflow/) Python version should
be 3.10.x

Currently, Python 3.9 version (Rocky Linux has that version of Python).

TF table with components versions:

https://www.tensorflow.org/tfx/transform/install

```shell
py -3.9 -m venv ./.venv
.\.venv\Scripts\activate
python --version
python -m pip install --upgrade pip

# Flask etc
pip install click colorama Flask itsdangerous Jinja2 MarkupSafe Markdown PyYAML Werkzeug

# Additional tools Vol 1
pip install jupyterlab notebook voila matplotlib seaborn

# Additional tools Vol 2 (Will be installed by tensorflow installation)
pip install numpy pandas

# Tensorflow
# pyarrow, numpy and pandas will be reinstalled by requirements
pip install tensorboard
pip install tensorflow
pip install tensorflow-datasets
pip install tensorflow-estimator
pip install tensorflow-io-gcs-filesystem
pip install tensorflow-metadata
# ...raise RuntimeError('Python version 2.7 or 3.4+ is required.') - Bad (already downgraded and loosing language new features).
pip install tensorflow-transform

#PyTorch (CPU version)
pip install torch torchvision torchaudio torchtext

# Take installed software list
pip freeze > requirements.txt
```

## PyCharm setup

Virtual environment setup:

![img.png](docs/pycharm-venv.png)

## TODO

1. Refactor Flask related code (web_app) by layers example code (application, layer_example, log, resources).
2. Falsk app gives an error at startup.
3. Problem: The TensorFlow library was compiled to use AVX instructions, but these aren't available on your machine.

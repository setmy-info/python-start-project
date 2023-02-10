# python-start-project

## Notest

For [Tensorflow 2.11.0 (at the moment the latest version)](https://pypi.org/project/tensorflow/) Python version should
be 3.10.x

```shell
py -3.10 -m venv ./.venv
.\.venv\Scripts\activate
python --version
pip install --upgrade pip

# Flask etc
pip install click colorama Flask itsdangerous Jinja2 MarkupSafe PyYAML Werkzeug

# Additional tools
pip install jupyterlab notebook voila numpy pandas matplotlib seaborn

# Tensorflow
pip install pyarrow
pip install tensorflow
pip install tensorflow-estimator
pip install tensorflow-io-gcs-filesystem
pip install tensorflow-metadata
# ...raise RuntimeError('Python version 2.7 or 3.4+ is required.') - Bad (already downgraded and loosing language new features).
# pip install tensorflow-transform

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

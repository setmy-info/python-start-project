from setuptools import setup, find_packages

setup(
    name=NAME,
    version=VERSION,
    description='Python start project',
    long_description='Python start project.',
    author='Imre Tabur',
    author_email='info@setmy.info',
    license='MIT',
    url='https://github.com/setmy-info/python-start-project',
    packages=find_packages(),
    install_requires=[
        "smi-python-runner==1.3.0"
    ],
)

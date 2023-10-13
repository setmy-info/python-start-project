from setuptools import setup, find_packages

from python_start_project.project import NAME, VERSION

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
        "Flask==3.0.0"
        "Werkzeug==3.0.0"
        "gunicorn==21.2.0"
        "gevent==23.9.1"
    ],
)

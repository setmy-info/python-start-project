import argparse

from application import Application

application = Application(
    __name__,
    "1.0.0",
    argparse.ArgumentParser(description='Layers example.')
)

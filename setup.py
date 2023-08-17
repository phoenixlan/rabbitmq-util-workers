import os
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md')) as f:
    README = f.read()

requires = [
    'requests',
    'pika'
]

setup(name='phoenixMailService',
    install_requires=requires,
)
import re
from os import path

from setuptools import setup, find_packages


with open(path.join(path.dirname(__file__), 'minibox', '__init__.py')) as f:
    _version = re.match(r'.*__version__ = \'(.*?)\'', f.read(), re.S).group(1)


dependencies = [
    'easycli',
]


setup(
    name='minibox',
    version=_version,
    author='Azim Hatami',
    discription='File synchronization tool',
    url='https://github.com/azimhatami/minibox',
    packages=find_packages(),
    install_requires=dependencies,
    license='MIT',
    entry_points={
        'console_scripts': [
            'minibox = minibox:Minibox.quickstart',
        ]
    },
)

from setuptools import setup, find_packages


dependencies = [
    'easycli',
]


setup(
    name='minibox',
    version='0.1.0',
    author='Azim Hatami',
    discription='File synchronization tool',
    url='https://github.com/azimhatami/minibox',
    packages=find_packages(),
    install_requires=dependencies
)

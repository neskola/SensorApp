# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='sensorapp',
    version='0.1',
    description='Sensor application for pluggable sensor code.',
    long_description=readme,
    author='Niki Eskola',
    author_email='neskola@gmail.com',
    url='https://github.com/neskola/SensorApp',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)


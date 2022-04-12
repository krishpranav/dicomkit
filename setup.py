#!/usr/bin/env python3

from setuptools import setup

setup(
    name='dicomkit',
    version='1.0',
    description='A Simple Python Tool To Convert Dicom File To Image',
    url='https://github.com/krishpranav/dicomkit',
    author='Krisna Pranav',
    author_email='krisna.pranav@gmail.com',
    license='MIT',
    install_requires=[
        'pypng',
        'pydicom>=1.0.0',
        'numpy'
    ],
)
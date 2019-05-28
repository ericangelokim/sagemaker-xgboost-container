from __future__ import absolute_import
import os
from glob import glob
from os.path import basename
from os.path import splitext

from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='sagemaker_xgboost_framework',
    version='1.0',
    description='Open source library for creating XGBoost containers to run on Amazon SageMaker.',

    packages=find_packages(where='src', exclude=('test',)),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],

    long_description=read('README.rst'),
    author='Amazon Web Services',
    license='Apache License 2.0',

    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        'Programming Language :: Python :: 3.5',
    ],

    install_requires=['matplotlib', 'numpy', 'pandas', 'psutil', 'retrying==1.3.3', 'scikit-learn',
                      'sagemaker-containers >= 2.2.5'],

    extras_require={
        'test': ['tox', 'flake8', 'coverage', 'pytest', 'pytest-cov', 'pytest-xdist', 'mock', 'Flask', 'boto3>=1.4.8',
                 'docker-compose', 'sagemaker>=1.3.0']
    }
)
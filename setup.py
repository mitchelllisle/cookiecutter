#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""
from setuptools import setup

with open('requirements.txt') as f:
    requirements = f.read().splitlines()


with open('requirements/test.txt') as f:
    test_requirements = f.read().splitlines()


setup(
    author='Mitchell Lisle',
    author_email='m.lisle90@gmail.com',
    description='A minimal cookicutter for new projects',
    install_requires=requirements,
    include_package_data=True,
    keywords='cookiecutterml',
    name='cookiecutterml',
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/mitchelllisle/cookiecutter',
    version='1.1.1',
    zip_safe=False,
)

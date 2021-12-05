#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""
from setuptools import find_packages, setup

with open('requirements.txt') as f:
    requirements = f.read().splitlines()


with open('requirements/test.txt') as f:
    test_requirements = f.read().splitlines()


setup(
    author='{{cookiecutter.full_name}}',
    author_email='{{cookiecutter.email}}',
    description='{{cookiecutter.project_description}}',
    install_requires=requirements,
    include_package_data=True,
    keywords='{{cookiecutter.project_slug}}',
    name='{{cookiecutter.project_slug}}',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}',
    version='{{cookiecutter.version}}',
    zip_safe=False,
)

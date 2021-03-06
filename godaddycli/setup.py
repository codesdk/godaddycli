#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

with open('VERSION.rst') as version_file:
    version = version_file.read()

requirements = [
    "pygodaddy"
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='godaddycli',
    version=version,
    description="Command Line Interface to GoDaddy.com based on PyGoDaddy Library",
    long_description=readme + '\n\n' + history,
    author="Wojciech A. Koszek",
    author_email='wojciech@koszek.com',
    url='https://github.com/wkoszek/godaddycli',
    packages=[
        'godaddycli',
    ],
    entry_points = {'console_scripts': ['godaddycli=godaddycli.godaddycli:main']},
    package_dir={'godaddycli':
                 'godaddycli'},
    include_package_data=True,
    install_requires=requirements,
    license="BSD",
    zip_safe=False,
    keywords='godaddycli',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
    tests_require=test_requirements
)

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
from textwrap import dedent

with open('README.rst') as readme_file:
    readme = readme_file.read()

requirements = [
    'click>=6.7',
    'astropy>=2.0',
    'numpy>=1.13'
]

description = dedent("""\
    Calculate the number of particles, particle mass,
    or volume of a cosmological N-body simulation given
    two of the three values.""")

setup(
    name='nbody_stats',
    py_modules=['nbody_stats'],
    version='0.1',
    description=description,
    long_description=readme,
    author="Simon Mutch",
    author_email='smutch.astro@gmail.com',
    url='https://github.com/smutch/nbody_stats',
    entry_points={
        'console_scripts': [
            'nbody-stats=nbody_stats:cli'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=True,
    keywords=['nbody simulation', 'astronomy'],
    classifiers=[
        'Development Status :: 3 - Alpha'
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
    ],
)

#!/usr/bin/env python
#
# This file is part of the smartcontainer package.
# For copyright and licensing information about this package, see the
# LICENSE file in its top-level directory; it is also
# available at https://github.com/crcresearch/orcidfind
#
# This Source Code Form is subject to the terms of the Apache License, version 2.0.
# If a copy of the ALv2 was not distributed with this file, You can obtain one at
# http://www.apache.org/licenses/LICENSE-2.0.

import os
from setuptools import setup, find_packages

base_dir = os.path.dirname(__file__)

version = {}
with open(os.path.join(base_dir, 'orcidfind', '__version__.py')) as f:
    exec(f.read(), version)
__version__ = version['VERSION']
__author__ = 'cwilli34'

setup(
    name='orcidfind',
    version=__version__,
    packages=['orcidfind', 'orcidsearch'],
    package_data={
        'orcidfind':['Dockerfile', '__version__.py','__init__.py']
    },
    entry_points={
        'console_scripts':['orcidfind = orcidfind.find:search_type']
    },
    url='https://crc.nd.edu',
    download_url='https://github.com/crcresearch/orcidfind/tarball/0.1-alpha.6',
    platforms='Linux',
    license='ALv2',
    author='cwilli34',
    author_email='cwilli34@nd.edu',
    description='Python script to allow an interactive TTY for searching the Orcid API',
    keywords=['orcid', 'python-orcid', 'pubic', 'API'],
    install_requires=[
        'click==4.1',
        'colorama==0.3.3',
        'orcid==0.5.1',
        'pprintpp==0.2.3',
        'requests==2.7.0'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Utilities',
    ]
)

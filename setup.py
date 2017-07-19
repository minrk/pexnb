#!/usr/bin/env python3
# coding: utf-8

# Copyright (c) Min RK.
# Distributed under the terms of the MIT License.

from setuptools import setup
import time

setup_args = dict(
    name                = 'pexnb',
    version             = '0.1.0',
    py_modules          = ['pexnb'],
    description         = "Provide PEX-compatible entrypoint for Jupyter notebooks",
    author              = "Min RK",
    author_email        = "benjaminrk@gmail.com",
    url                 = "https://github.com/minrk/pexnb",
    install_requires    = ["jupyter_client", "notebook"],
    license             = "MIT",
    classifiers         = [
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ],
)
if __name__ == '__main__':
    setup(**setup_args)

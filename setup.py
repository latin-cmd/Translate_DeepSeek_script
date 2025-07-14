#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Setup file for Translation Toolkit
"""

from setuptools import setup, find_packages
import os

# Read requirements from requirements.txt
with open('requirements.txt', 'r', encoding='utf-8') as f:
    requirements = [line.strip() for line in f if line.strip() and not line.startswith('#')]

# Read README for long description
with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='translation-toolkit',
    version='1.0.0',
    description='A Python toolkit for processing Markdown document translation',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Translation Toolkit Team',
    python_requires='>=3.6',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'translate-toolkit=main:main',
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Text Processing :: Markup',
        'Topic :: Utilities',
    ],
)
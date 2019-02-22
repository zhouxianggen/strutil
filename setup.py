#!/usr/bin/env python
#coding=utf8

try:
    from  setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

setup(
        name = 'strutil',
        version = '1.0',
        install_requires = [], 
        description = 'python string utils',
        url = 'https://github.com/zhouxianggen/strutil', 
        author = 'zhouxianggen',
        author_email = 'zhouxianggen@gmail.com',
        classifiers = [ 'Programming Language :: Python :: 3.7',],
        packages = ['strutil'],
        data_files = [ ],  
        entry_points = { }   
        )

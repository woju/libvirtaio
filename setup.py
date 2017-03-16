#!/usr/bin/python3 -O
# vim: fileencoding=utf-8

import setuptools

setuptools.setup(
    name='libvirtaio',
    version='1.0',
    author='Wojtek Porczyk',
    author_email='woju@invisiblethingslab.com',
    description='Libvirt event loop implementation using asyncio',
    license='Apache-2.0',
    url='https://github.com/woju/libvirtaio',
    py_modules=['libvirtaio'])

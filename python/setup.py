#!/usr/bin/python

from distutils.core import setup
import os
import fnmatch

MOUDLE_LIST=[]

for root, dirs, files in os.walk('.'):
    if 'build' in dirs:
        continue
    if 'dist' in dirs:
        continue

    for file in fnmatch.filter(files, '*.py'):
        if file != '__init__.py' and file != 'setup.py':
            MOUDLE_LIST.append(os.path.join(root, file).replace('./', '').replace('.py', ''))
print MOUDLE_LIST

setup(
    name="itest",
    version="0.1",
    description="itest module for automation testing",
    author="David Gu",
    url="https://github.com/nuangua/itest",
    py_modules=['ATDevice', 'Log','Generic','Ping','FTP','UDP','Call'],
        )

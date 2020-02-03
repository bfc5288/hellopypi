import os
from setuptools import setup

# read in README                                                                                     
this_dir = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_dir, 'README.md'), 'rb') as f:
    long_description = f.read().decode().strip()

setup(
    name='hellopypi_bfc',
    packages=['hellopypi_bfc'],
    description='Hello world for pypi',
    #version='v0.1.2',
    setup_requires = ['setuptools_scm'],
    use_scm_version = {
        'write_to': '/hellopypi_bfc/_version.py'},
    #url='http://github.com/example/hellopypi',
    author='bfc5288',
    keywords=['pip','helloworld']
    )


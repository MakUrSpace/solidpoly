from setuptools import setup, Extension


# read the contents of README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()


setup(
    name='solidpoly',
    version='0.0.0.1',
    author='musingsole',
    author_email='musingsole@gmail.com',
    description='Library of desciptive code for various volumes',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://gitlab.com/makurspace/solidpoly',
    install_requires=[],
    packages=["solidpoly"],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)

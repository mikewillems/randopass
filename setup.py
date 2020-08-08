# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='randopass',
    version='0.0.5',
    description='Generate easy but secure passphrases',
    long_description=readme,
    author='Mike Willems',
    author_email='themikewillems@gmail.com',
    url='https://github.com/mikewillems/randopass',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    entry_points={
        'console_scripts': ['randopass=command_line:main'],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
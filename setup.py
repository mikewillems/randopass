# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


# with open('README.md') as f:
#     readme = f.read()

# with open('LICENSE') as f:
    # license = f.read()

setup(
    name='randopass',
    version='0.0.3',
    description='Generate easy but secure passphrases',
    long_description=readme,
    author='Mike Willems',
    author_email='themikewillems@gmail.com',
    url='https://github.com/mikewillems/randopass',
    license='MIT',
    packages=find_packages(exclude=('tests', 'docs'))
)
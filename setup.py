# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

# with open('LICENSE') as f:
    # license = f.read()

setup(
    name='randopass',
    version='0.0.4',
    description='Generate easy but secure passphrases',
    long_description=readme,
    long_description_content_type='text/markdown',
    author='Mike Willems',
    author_email='themikewillems@gmail.com',
    url='https://github.com/mikewillems/randopass',
    packages=find_packages(exclude=('tests', 'docs')),
    python_requires='>=3.5, <4',
    entry_points={
        'console_scripts':[
            'randopass=command_line:main',
        ],
    },
)

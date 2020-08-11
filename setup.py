# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import re
from os import getcwd, path
import pathlib

# here = pathlib.Path(__file__).parent.resolve()

package_dir = getcwd()+path.sep

# with open(package_dir + 'README.md') as f:
#     readme = f.read()
    
with open(package_dir + 'LICENSE') as f:
    license = f.read()

with open('randopass/randopass.py') as f:
    version = re.search(
    '^__version__\s*=\s*"(.*)"',
    f.read(),
    re.M
    ).group(1).strip('\n')

setup(
    name='randopass',
    version=version,
    description='Generate easy but secure passphrases',
    long_description='The long description isn\'t working, so please checkout the github page: (https://github.com/mikewillems/randopass/) for full instructions.',
    # long_description = (here / 'README.md').read_text(encoding='utf-8'),
    # long_description_content_type='text/markdown',
    author='Mike Willems',
    author_email='themikewillems@gmail.com',
    url='https://github.com/mikewillems/randopass',
    license='MIT',
    packages=find_packages(exclude=('tests', 'docs')),
    include_package_data = True,
    entry_points={
        'console_scripts': ['randopass=randopass.randopass:main'],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
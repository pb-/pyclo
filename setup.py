from setuptools import find_packages, setup

setup(
    name='pyclo',
    version='0.1.0',
    author='Paul Baecher',
    description='Immutable manipulation of Python data structures, Clojure style',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/pb-/pyclo',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)

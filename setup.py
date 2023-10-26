#This file will be responsible in creating the ML application as a package with the help of Python PyPi.

from setuptools import find_packages, setup 

#find_package will find all the packages present in the ML project. 

#Do the setup
setup(
    name = 'mlproject',
    version = '0.0.1',
    author = 'Grace',
    author_email= 'gitomegracie@gmail.com',
    packages = find_packages(),
    install_requires = ['pandas', 'numpy', 'seaborn']
    
    )

#This file will be responsible in creating the ML application as a package with the help of Python PyPi.

from setuptools import find_packages, setup 
from typing import List

#find_package will find all the packages present in the ML project. 

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements
    '''
    get_requirements= []
    with open(file_path) as file_obj: #open the file as a temporary object
        requirements = file_obj.readlines()
        #the for loop in order to prevent a new line (\n) being added after readlines function is implement as each line is being read
        [req.replace("\n", "")for req in requirements]
        
        #For loop to mitigate printing of the '-e .' present in the requirements.txt file
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
            
           
            return requirements
            
            
        

        
#Do the setup
setup(
    name = 'mlproject',
    version = '0.0.1',
    author = 'Grace',
    author_email= 'gitomegracie@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
        
    )

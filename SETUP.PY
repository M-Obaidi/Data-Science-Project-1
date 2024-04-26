from setuptools import find_packages, setup
from typing import List

hpene = '-e .'
def get_requirements(file_path:str)->List[str]:
    requirements =[]
    with open(file_path) as file_obj:
        requirements= file_obj.readlines()
        requirements = [req.replace("\n"," ") for req in requirements]
        if hpene in requirements:
            requirements.remove(hpene)
    return requirements

setup(    name = 'Project1',
    version = '0.0.1', 
    author = 'obaid',  
    author_email = "mobaid@cs.qau.edu.pk",
    packages = find_packages(),
    install_requires = get_requirements('requirement.txt')
)
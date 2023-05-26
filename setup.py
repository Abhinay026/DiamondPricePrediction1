from setuptools import find_packages,setup
from typing import List

def get_requirements(filepath:str)->List[str]:
    requirements = []
    with open(filepath) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        return requirements


setup (
    name = 'DiamondPricePrediction',
    version = '0.0.1',
    author = 'abhi026',
    author_email = 'abhinay.026@gmail.com',
    install_requires = get_requirements('requirements.txt'),
    packages = find_packages()

)

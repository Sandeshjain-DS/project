from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    """
    This function will return the list of requirements
    """
    requirements = []
    with open(file_path) as file_obj:
        # Use `readlines()` to read all lines from the file
        requirements = file_obj.readlines()
        # Remove newline characters from each line
        requirements = [req.strip() for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name='tpproject',
    version='0.0.1',
    author='Sandesh',
    author_email='sandeshjain960@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirement.txt')
)

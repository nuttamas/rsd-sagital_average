from setuptools import setup
from setuptools import find_packages

setup(
    name="sagital_average",
    version="0.0.1",
    packages=find_packages(exclude=['*test']),
    entry_points={ 'console_scripts': ['sagverage = sagital_average.command:process']},
)
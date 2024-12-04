from setuptools import setup, find_packages

setup(
    name='deepview-classes',
    version='0.2.0',
    packages=find_packages(include=['v1', 'v1.*', 'v2', 'v2.*']),
    install_requires=[
        'pydantic',
    ],
)

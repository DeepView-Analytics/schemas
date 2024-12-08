from setuptools import setup, find_packages

setup(
    name='deepview-classes',
    version='0.3.1',
    packages=find_packages(include=['v1', 'v1.*', 'v2', 'v2.*', 'v3', 'v3.*']),
    install_requires=[
        'pydantic',
    ],
)

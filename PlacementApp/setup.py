from setuptools import setup

setup(
    name='PlacementApp',
    packages=['app'],
    include_package_data=True,
    install_requires=[
        'flask',
        'sqlalchemy',
        'openpyxl',
        'passlib'
    ],
)
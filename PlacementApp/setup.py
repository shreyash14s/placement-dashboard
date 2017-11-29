from setuptools import setup

setup(
    name='PlacementApp',
    packages=['app'],
    include_package_data=True,
    install_requires=[
        'flask',
        'sqlalchemy',
        'Flask-SQLAlchemy',
        'sqlalchemy_utils',
        'openpyxl',
        'passlib',
        'PyMySQL'
    ],
)
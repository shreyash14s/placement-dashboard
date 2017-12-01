from setuptools import setup

setup(
    name='PlacementApp',
    version='1.1.2',
    packages=['app'],
    include_package_data=True,
    install_requires=[
        'flask',
        'sqlalchemy',
        'Flask-SQLAlchemy',
        'sqlalchemy_utils',
        'openpyxl',
        'passlib',
        'PyMySQL',
        'requests',
        'numpy',
        'matplotlib'
    ],
)
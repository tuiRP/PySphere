# pysphere/setup.py

from setuptools import setup, find_packages

setup(
    name='pysphere',
    version='0.1',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        # Listar as dependências aqui
    ],
    entry_points={
        'console_scripts': [
            'pysphere=pysphere:main',
        ],
    },
)


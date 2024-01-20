from setuptools import setup

setup(
    name='fancy',
    version='1.0.0a4',
    py_modules=['fancy'],
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'fancy = fancy:fancy',
        ],
    },
)
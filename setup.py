from setuptools import setup, find_packages

with open('README.md') as f:
    long_description = f.read()


test_deps = [
    'coverage',
    'pytest',
]

setup(
    name='fanpi',
    version='1.0.0',
    url='https://github.com/richievos/fanpi',
    license='BSD-3-Clause',
    maintainer='Richie Vos',
    maintainer_email='vosrichie@gmail.com',
    description='An app for controlling a fan from a Raspberry Pi',
    long_description=long_description,
    long_description_content_type='text/markdown',

    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Flask>=1.1.2',
        'gpiozero>=1.5.1'
    ],

    tests_require=test_deps,
    extras_require={
        'test': test_deps,
    }
)

#!/usr/bin/env python
"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

with open('requirements.txt') as requirements_file:
    require = requirements_file.read()
    requirements = require.split()

setup_requirements = ['pytest-runner']

test_requirements = [
    'pytest>=3',
]

setup(
    author="Juncheng E",
    author_email='juncheng.e@xfel.eu',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description=
    "The core package of the SIMEX platform providing the calculator interfaces.",
    entry_points={
        'console_scripts': [
            'SimExLite=SimExLite.cli:main',
        ],
    },
    install_requires=requirements,
    license="GNU General Public License v3",
    long_description=readme + '\n\n' + history,
    long_description_content_type='text/x-rst',
    include_package_data=True,
    keywords='SimEx-Lite',
    name='SimEx-Lite',
    packages=find_packages(include=['SimExLite', 'SimExLite.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/PaNOSC-ViNYL/SimEx-Lite',
    version='1.0.0',
    zip_safe=False,
)

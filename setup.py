import sys
from setuptools import setup, find_packages

if sys.version_info < (3, 6):
    raise RuntimeError("Asmdiff requires Python 3.6 or higher")

with open('README.md', 'r') as readme:
    long_description = readme.read()

setup(
    name='asmdiff',
    version='1.0.0',
    description='A tool for comparing the output of "objdump" for before/after pairs of .o files.',
    author='Dmitry Mikushin',
    author_email='dmitry@kernelgen.org',
    url='https://github.com/dmikushin/asmdiff',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Testing',
    ],
    install_requires=['demangler'],
    packages = find_packages(exclude=["test"]),
    entry_points={
        'console_scripts': [
            'asmdiff=asmdiff:main',
        ],
    },
)

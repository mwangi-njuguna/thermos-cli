"""Packaging settings."""


from codecs import open
from os.path import abspath, dirname, join
from subprocess import call

from setuptools import Command, find_packages, setup

from thermos import __version__


this_dir = abspath(dirname(__file__))
with open(join(this_dir, 'README.rst'), encoding='utf-8') as file:
    long_description = file.read()

class RunTests(Command):
    """Run all tests."""
    description = 'run tests'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        """Run all tests!"""
        errno = call(['py.test', '--cov=thermos', '--cov-report=term-missing'])
        raise SystemExit(errno)

setup(
    name = 'thermos',
    version = __version__,
    description = 'A command line program in Python for creating flask standard application structure, blueprints and templates.',
    long_description = long_description,
    url = 'https://github.com/mwangi-njuguna/thermos-cli',
    author = 'Mwangi Njuguna',
    author_email = 'mwanginjuguna59@gmail.com',
    license = 'UNLICENSE',
    classifiers = [
        'Intended Audience :: Flask Developers',
        'Topic :: Utilities',
        'License :: Public Domain',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.6',
    ],
    keywords = 'cli',
    packages = find_packages(exclude=['docs', 'tests*']),
    package_dir = {'': 'lib'},
    install_requires = ['docopt'],
    extras_require = {
        'test': ['coverage', 'pytest', 'pytest-cov'],
    },
    entry_points = {
        'console_scripts': [
            'thermos=thermos.cli:main',
        ],
    },
    cmdclass = {'test': RunTests},
)

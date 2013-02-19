import os
import sys
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

from mutagenwrapper import version


# Utility function to read the README file.
# Used for the long_description.  It"s nice, because now 1) we have a top level
# README file and 2) it"s easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


class PyTest(TestCommand):

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)


setup(
    name = "mutagenwrapper",
    version = version,
    author = "Choongmin Lee",
    author_email = "choongmin@me.com",
    description = "A wrapper for mutagen that uses consistent keys among various tagging formats",
    keywords = "audio metadata tags",
    license = "MIT License",
    url = "https://github.com/clee704/mutagenwrapper",
    packages = find_packages(),
    install_requires = ["mutagen >= 1.2.1"],
    long_description = read("README.rst"),
    classifiers = [
        # Full list is here: http://pypi.python.org/pypi?%3Aaction=list_classifiers
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Topic :: Multimedia :: Sound/Audio",
        "Topic :: Utilities",
    ],
    tests_require = ["pytest"],
    cmdclass = {"test": PyTest},
)

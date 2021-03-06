from setuptools import setup, find_packages
from codecs import open  # To use a consistent encoding
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
  name = 'markdown-swiss',
  packages = find_packages(),
  version = '0.0.1',
  description = 'This is an extension to Python-Markdown which provides a variety of functions for running python code',
  long_description = long_description,
  author = 'Chris Jefferson',
  author_email = 'chris@bubblescope.net',
  url = 'https://github.com/ChrisJefferson/markdown-swiss', 
  download_url = 'https://github.com/ChrisJefferson/markdown-swiss/tarball/v0.0.1',
  keywords = ['Markdown', 'typesetting', 'include', 'plugin', 'extension'],
  classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Internet :: WWW/HTTP :: Site Management',
        'Topic :: Software Development :: Documentation',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing :: Filters',
        'Topic :: Text Processing :: Markup :: HTML',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],
  install_requires = ['markdown']
)

"""
hexacolors
~~~~~~~~~~~~~~~~~~~

A simple library that converts string to hexadecimal understandable by python

:(c) 2022-present Marciel404
:license: MIT, see LICENSE for more details.
"""

__title__ = "Hexacolors"
__author__ = "Marciel404"
__license__ = "MIT"
__copyright__ = "2022-present Marciel404"
__version__ = "0.3.5"

__path__ = __import__("pkgutil").extend_path(__path__, __name__)

from .convertingcolor import hexacolor, stringcolor
from .listcolors import (
    listblack,
    listblue,
    listcyan,
    listgreen,
    listbrown,
    listpurple,
    listpink,
    listred,
    listorange,
    listyellow,
    listlight,
    listall
    )
"""
Hexacolors
~~~~~~~~~~~~~~~~~~~~

:A simple library that converts string to hexadecimal understandable by python
:A simple library that converts RGB to hexadecimal understandable by python
:A simple library that converts CMYK to hexadecimal understandable by python
:A simple library that converts CMYK to hexadecimal understandable by python
:A simple library that converts hexadecimal understandable by python

:(c) 2022-present Marciel404
:license: MIT, see LICENSE for more details.
:I created this library to use as with the pycord integration so I don't know if it works elsewhere

"""

__title__ = "Hexacolors"
__author__ = "Marciel404"
__license__ = "MIT"
__copyright__ = "2022-present Marciel404"
__version__ = "0.4.5"

__path__ = __import__("pkgutil").extend_path(__path__, __name__)

from .str import string
from .autodetect import autodetect

from .api import (
    hexadecimal, 
    rgb,
    cmyk,
    hsl
)

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
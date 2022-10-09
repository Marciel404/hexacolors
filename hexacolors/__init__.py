"""
hexacolors
~~~~~~~~~~~~~~~~~~~

A simple library that converts string to hexadecimal understandable by python

:(c) 2022-present Marciel404
:license: MIT, see LICENSE for more details.

I created this library more to use as pycord integration

Using StringColor:

    >>> import hexacolors
    >>>
    >>> hexacolors.stringcolor('Blue')
    >>>
    >>> print(hexacolors.listall) #List all colors availables

Using HexaColor:

    >>> import hexacolors
    >>>
    >>> hexacolors.hexacolor('#0000FF') #Convert Hexadecimal Color for Python understand

"""

__title__ = "Hexacolors"
__author__ = "Marciel404"
__license__ = "MIT"
__copyright__ = "2022-present Marciel404"
__version__ = "0.3.6"

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
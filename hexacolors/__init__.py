"""
hexacolors
~~~~~~~~~~~~~~~~~~~

A simple library that converts string to hexadecimal understandable by python

A simple library that converts RGB to hexadecimal understandable by python

A simple library that converts CMYK to hexadecimal understandable by python

A simple library that converts hexadecimal understandable by python

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

Using rgb:

    >>> import hexacolors
    >>>
    >>> hexacolors.rgb('255,255,255')

Using cmyk:

    >>> import hexacolors
    >>>
    >>> hexacolors.rgb('423,522,4,244')

Using AutoDetect:

    >>> import hexacolors
    >>>
    >>> hexacolors.autodetect('Blue') Identify string
    >>>
    >>> hexacolors.autodetect('#fff000') Identify Hexadecimal
    >>>
    >>> hexacolors.autodetect('255,255,255') Identify RGB
    >>>
    >>> hexacolors.autodetect('423,522,4,244') Identify CMYK

"""

__title__ = "Hexacolors"
__author__ = "Marciel404"
__license__ = "MIT"
__copyright__ = "2022-present Marciel404"
__version__ = "0.3.7"

__path__ = __import__("pkgutil").extend_path(__path__, __name__)

from .str import stringcolor
from .api import hexacolor, rgb, cmyk
from .autodetect import autodetect

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
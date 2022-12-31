import string

from .api import hexadecimal, hsl, rgb, cmyk
from ..offline.str import stringColor


def autodetect(args: str) -> int:
    """
    Using AutoDetect:

    Alert It only works if you are connected to the internet
    >>>
    >>> import hexacolors
    >>> hexacolors.autodetect('Blue') #Identify string
    >>> hexacolors.autodetect('#fff000') #Identify Hexadecimal
    >>> hexacolors.autodetect('255,255,255') #Identify RGB
    >>> hexacolors.autodetect('423,522,4,244') #Identify CMYK
    >>> hexacolors.autodetect('255,75%,64%') #Identify HSL
    """

    if args[0] == '#':
        hexadecimal(args)
    elif args.count('%') > 0:
        hsl(args)
    elif args.count(',') == 2:
        rgb(args)
    elif args.count(',') == 3:
        cmyk(args)
    elif args[0] in list(string.digits):
        hexadecimal(args)
    elif args[0] in list(string.ascii_letters):
        try:
            stringColor(args)
        except:
            hexadecimal(args)
    else:
        print('ERROR: Not indentify the type')

import requests

def hexadecimaloff(hexa:str) -> str:

    '''
    Using HexaColor:

    >>> import hexacolors
    >>> hexacolors.hexadecimaloff('#0000FF') #Convert Hexadecimal Color for Python understand
    '''

    if hexa[0] == '#':hexa = hexa[1::]

    return int(f"0x{hexa}",16)

def rgboff(r:int,g:int,b:int) -> int:

    '''
    Using rgb:

    >>> import hexacolors
    >>> hexacolors.rgboff(255,255,255)
    '''

    return int('0x{:X}{:X}{:X}'.format(r, g, b),16)

def cmykoff(c:int,m:int,y:int,k:int) -> str:

    '''
    Using cmyk:

    >>> import hexacolors
    >>> hexacolors.cmykoff('423,522,4,244')
    '''

    return int('0x{:X}{:X}{:X}{:X}'.format(c, m, y, k),16)
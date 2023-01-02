import asyncio
from .client.clientlogin import ClientGet

def hexadecimal(hexa:str) -> int:

    '''
    Using HexaColor:

    >>> import hexacolors
    >>> hexacolors.hexadecimal('#0000FF') #Convert Hexadecimal Color for Python understand
    '''

    if hexa[0] == '#':hexa = hexa[1::]
    
    request = asyncio.run(ClientGet(f'hex', hexa).request())

    return int(f"0x{request}",16)

def rgb(rgb) -> int:

    '''
    Using rgb:

    >>> import hexacolors
    >>> hexacolors.rgb('255,255,255')
    '''
    
    request = asyncio.run(ClientGet(f'rgb', rgb).request())
    
    return int(f"0x{request}",16)

def cmyk(cmyk) -> int:

    '''
    Using cmyk:

    >>> import hexacolors
    >>> hexacolors.cmyk('423,522,4,244')
    '''

    request = asyncio.run(ClientGet(f'cmyk', cmyk).request())

    return int(f"0x{request}",16)

def hsl(hsl:str) -> int:

    '''
    Using hsl:

    >>> import hexacolors
    >>> hexacolors.hsl('423,60%,70%')
    '''

    request = asyncio.run(ClientGet(f'hsl', hsl).request())

    return int(f"0x{request}",16)
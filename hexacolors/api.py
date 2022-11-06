import requests

def hexadecimal(hexa:str) -> str:

    '''
    Using HexaColor:

    >>> import hexacolors
    >>>
    >>> hexacolors.hexadecimal('#0000FF') #Convert Hexadecimal Color for Python understand
    '''

    if hexa[0] == '#':

        hexa = hexa[1::]

    p = requests.get(f'https://www.thecolorapi.com/id?hex={hexa}')

    colour = int(f"0x{p.json()['hex']['clean']}",16)

    return colour

def rgb(rgb:str) -> str:

    '''
    Using rgb:

    >>> import hexacolors
    >>>
    >>> hexacolors.rgb('255,255,255')
    '''

    p = requests.get(f'https://www.thecolorapi.com/id?rgb={rgb}')

    colour = int(f"0x{p.json()['hex']['clean']}",16)

    return colour

def cmyk(cmyk:str) -> str:

    '''
    Using cmyk:

    >>> import hexacolors
    >>>
    >>> hexacolors.cmyk('423,522,4,244')
    '''

    p = requests.get(f'https://www.thecolorapi.com/id?cmyk={cmyk}')

    colour = int(f"0x{p.json()['hex']['clean']}",16)

    return colour

def hsl(hsl:str) -> str:

    '''
    Using hsl:

    >>> import hexacolors
    >>>
    >>> hexacolors.hsl('423,60%,70%')
    '''

    p = requests.get(f'https://www.thecolorapi.com/id?hsl={hsl}')

    colour = int(f"0x{p.json()['hex']['clean']}",16)

    return colour
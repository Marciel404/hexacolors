import requests

def hexadecimal(hexa: str) -> int:

    """
    Using HexaColor:

    >>> import hexacolors
    >>> hexacolors.hexadecimal('#0000FF') #Convert Hexadecimal Color for Python understand
    """

    if hexa[0] == '#':
        hexa = hexa[1::]
    
    p = requests.get(f'https://www.thecolorapi.com/id?hex={hexa}')

    return int(f"0x{p.json()['hex']['clean']}",  16)


def rgb(rgb: str) -> int:

    """
    Using rgb:

    >>> import hexacolors
    >>> hexacolors.rgb('255,255,255')
    """
    
    p = requests.get(f'https://www.thecolorapi.com/id?rgb={rgb}')
    
    return int(f"0x{p.json()['hex']['clean']}", 16)

def cmyk(cmyk: str) -> int:

    """
    Using cmyk:

    >>> import hexacolors
    >>> hexacolors.cmyk('423,522,4,244')
    """

    p = requests.get(f'https://www.thecolorapi.com/id?cmyk={cmyk}')

    return int(f"0x{p.json()['hex']['clean']}", 16)

def hsl(hsl: str) -> int:

    """
    Using hsl:

    >>> import hexacolors
    >>> hexacolors.hsl('423,60%,70%')
    """

    p = requests.get(f'https://www.thecolorapi.com/id?hsl={hsl}')

    return int(f"0x{p.json()['hex']['clean']}", 16)

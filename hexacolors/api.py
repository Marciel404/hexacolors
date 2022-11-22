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
    
    try: #Use if online

        p = requests.get(f'https://www.thecolorapi.com/id?hex={hexa}')

        colour = int(f"0x{p.json()['hex']['clean']}",16)
    
    except: #USe if offline

        colour = int(f"0x{hexa}",16)

    return colour

def rgb(r:int,g:int,b:int) -> int:

    '''
    Using rgb:

    >>> import hexacolors
    >>>
    >>> hexacolors.rgb(255,255,255)
    '''

    try: #Use if online

        p = requests.get(f'https://www.thecolorapi.com/id?rgb={r},{g},{b}')

        colour = int(f"0x{p.json()['hex']['clean']}",16)
    
    except: #USe if offline

        colour = int('0x{:X}{:X}{:X}'.format(r, g, b),16)

    return colour

def cmyk(c:int,m:int,y:int,k:int) -> str:

    '''
    Using cmyk:

    >>> import hexacolors
    >>>
    >>> hexacolors.cmyk('423,522,4,244')
    '''

    try:

        p = requests.get(f'https://www.thecolorapi.com/id?cmyk={c},{m},{y},{k}')

        colour = int(f"0x{p.json()['hex']['clean']}",16)
    
    except: #USe if offline

        colour = int('0x{:X}{:X}{:X}{:X}'.format(c, m, y, k),16)

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
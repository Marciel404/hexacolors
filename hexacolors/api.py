import requests

def hexacolor(hexa:str) -> str:

    if hexa[0] == '#':

        hexa = hexa[1::]

    p = requests.get(f'https://www.thecolorapi.com/id?hex={hexa}')

    colour = int(f"0x{p.json()['hex']['clean']}",16)

    return colour

def rgb(rgb:str) -> str:

    p = requests.get(f'https://www.thecolorapi.com/id?rgb={rgb}')

    colour = int(f"0x{p.json()['hex']['clean']}",16)

    return colour

def cmyk(cmyk:str) -> str:

    p = requests.get(f'https://www.thecolorapi.com/id?cmyk={cmyk}')

    colour = int(f"0x{p.json()['hex']['clean']}",16)

    return colour
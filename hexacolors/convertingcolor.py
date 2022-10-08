import requests

from .colors.gray import *
from .colors.blue import *
from .colors.cyan import *
from .colors.brown import *
from .colors.purple import *
from .colors.pink import *
from .colors.green import *
from .colors.red import *
from .colors.orange import *
from .colors.yellow import *
from .colors.ligthcolors import *

def hexacolor(hexa:str) -> str:

    if hexa[0] == '#':

        hexa = hexa[1::]

    p = requests.get(f'https://www.thecolorapi.com/id?hex={hexa}')

    colour = int(f"0x{p.json()['hex']['clean']}",16)

    return colour

def stringcolor(cor:str) -> str:

    if cor.lower().replace(' ','') == 'black': 

        color = black()

    elif cor.lower().replace(' ','') == 'gray1':

        color = grey11()
    
    elif cor.lower().replace(' ','') == 'gray2':

        color = grey21()
    
    elif cor.lower().replace(' ','') == 'gray3':

        color = grey31()
    
    elif cor.lower().replace(' ','') == 'dimgray': 

        color = dimgray()

    elif cor.lower().replace(' ','') == 'gray':

        color = gray()
    
    elif cor.lower().replace(' ','') == 'darkgray':

        color = darkgray()
    
    elif cor.lower().replace(' ','') == 'silver':

        color = silver()
    
    elif cor.lower().replace(' ','') == 'ligthgrey':

        color = ligthgrey()
    
    elif cor.lower().replace(' ','') == 'gainsboro':

        color = gainsboro()
    
    elif cor.lower().replace(' ','') == 'slateblue':

        color = slateblue()
    
    elif cor.lower().replace(' ','') == 'slateblue1': 

        color = slateblue1()

    elif cor.lower().replace(' ','') == 'slateblue2':

        color = slateblue3()
    
    elif cor.lower().replace(' ','') == 'darkslateblue':

        color = darkslateblue()
    
    elif cor.lower().replace(' ','') == 'midnightblue':

        color = midnightblue()
    
    elif cor.lower().replace(' ','') == 'navy':

        color = navy()
    
    elif cor.lower().replace(' ','') == 'darkblue':

        color = darkblue()
    
    elif cor.lower().replace(' ','') == 'mediumblue':

        color = mediumblue()
    
    elif cor.lower().replace(' ','') == 'blue': 

        color = blue()

    elif cor.lower().replace(' ','') == 'cornflowerblue':

        color = cornflowerblue()
    
    elif cor.lower().replace(' ','') == 'royalblue':

        color = royalblue()
    
    elif cor.lower().replace(' ','') == 'dodgerblue':

        color = dodgerblue()
    
    elif cor.lower().replace(' ','') == 'deepskyblue':

        color = deepskyblue()
    
    elif cor.lower().replace(' ','') == 'lightskyblue':

        color = lightskyblue()
    
    elif cor.lower().replace(' ','') == 'skyblue':

        color = skyblue()
    
    elif cor.lower().replace(' ','') == 'lightblue': 

        color = lightblue()

    elif cor.lower().replace(' ','') == 'steelblue':

        color = steelblue()
    
    elif cor.lower().replace(' ','') == 'lightsteelblue':

        color = lightsteelblue()
    
    elif cor.lower().replace(' ','') == 'slategray':

        color = slategray()
    
    elif cor.lower().replace(' ','') == 'lightslategray':

        color = lightslategray()
    
    elif cor.lower().replace(' ','') == 'cyan':

        color = cyan()
    
    elif cor.lower().replace(' ','') == 'darkturquoise':

        color = darkturquoise()
    
    elif cor.lower().replace(' ','') == 'turquoise': 

        color = turquoise()

    elif cor.lower().replace(' ','') == 'mediumturquoise':

        color = mediumturquoise()
    
    elif cor.lower().replace(' ','') == 'lightseagreen':

        color = lightseagreen()
    
    elif cor.lower().replace(' ','') == 'darkcyan':

        color = darkcyan()

    elif cor.lower().replace(' ','') == 'teal':

        color = teal()
    
    elif cor.lower().replace(' ','') == 'aquamarine':

        color = aquamarine()
    
    elif cor.lower().replace(' ','') == 'mediumaquamarine':

        color = mediumaquamarine()
    
    elif cor.lower().replace(' ','') == 'cadetblue': 

        color = cadetblue()

    elif cor.lower().replace(' ','') == 'darkkhaki':

        color = darkkhaki()
    
    elif cor.lower().replace(' ','') == 'goldenrod':

        color = goldenrod()
    
    elif cor.lower().replace(' ','') == 'darkgoldenrod':

        color = darkgoldenrod()

    elif cor.lower().replace(' ','') == 'saddlebrown':

        color = saddlebrown()
    
    elif cor.lower().replace(' ','') == 'sienna':

        color = sienna()
    
    elif cor.lower().replace(' ','') == 'rosybrown':

        color = rosybrown()
    
    elif cor.lower().replace(' ','') == 'peru': 

        color = peru()

    elif cor.lower().replace(' ','') == 'chocolate':

        color = chocolate()
    
    elif cor.lower().replace(' ','') == 'sandybrown':

        color = sandybrown()
    
    elif cor.lower().replace(' ','') == 'navajowhite':

        color = navajowhite()
    
    elif cor.lower().replace(' ','') == 'wheat':

        color = wheat()
    
    elif cor.lower().replace(' ','') == 'burlywood':

        color = burlywood()
    
    elif cor.lower().replace(' ','') == 'tan':

        color = tan()
    
    elif cor.lower().replace(' ','') == 'mediumslateBllue': 

        color = mediumslateBllue()

    elif cor.lower().replace(' ','') == 'mediumpurple':

        color = mediumpurple()
    
    elif cor.lower().replace(' ','') == 'blueviolet':

        color = blueviolet()
    
    elif cor.lower().replace(' ','') == 'indigo':

        color = indigo()
    
    elif cor.lower().replace(' ','') == 'darkviolet':

        color = darkviolet()
    
    elif cor.lower().replace(' ','') == 'darkorchid':

        color = darkorchid()
    
    elif cor.lower().replace(' ','') == 'mediumorchid':

        color = mediumorchid()
    
    elif cor.lower().replace(' ','') == 'purple': 

        color = purple()

    elif cor.lower().replace(' ','') == 'darkmagenta':

        color = darkmagenta()
    
    elif cor.lower().replace(' ','') == 'magenta':

        color = magenta()
    
    elif cor.lower().replace(' ','') == 'violet':

        color = violet()
    
    elif cor.lower().replace(' ','') == 'orchid':

        color = orchid()
    
    elif cor.lower().replace(' ','') == 'plum':

        color = plum()
    
    elif cor.lower().replace(' ','') == 'mediumvioletred':

        color = mediumvioletred()
    
    elif cor.lower().replace(' ','') == 'deeppink': 

        color = deeppink()

    elif cor.lower().replace(' ','') == 'hotpink':

        color = hotpink()
    
    elif cor.lower().replace(' ','') == 'palevioletred':

        color = palevioletred()
    
    elif cor.lower().replace(' ','') == 'lightpink':

        color = lightpink()
    
    elif cor.lower().replace(' ','') == 'pink':

        color = pink()
    
    elif cor.lower().replace(' ','') == 'lightcoral':

        color = lightcoral()
    
    elif cor.lower().replace(' ','') == 'indianred':

        color = indianred()
    
    elif cor.lower().replace(' ','') == 'crimson': 

        color = crimson()

    elif cor.lower().replace(' ','') == 'darkslategreen':

        color = darkslategreen()
    
    elif cor.lower().replace(' ','') == 'mediumspringgreen':

        color = mediumspringgreen()
    
    elif cor.lower().replace(' ','') == 'springgreen':

        color = springgreen()
    
    elif cor.lower().replace(' ','') == 'palegreen':

        color = palegreen()
    
    elif cor.lower().replace(' ','') == 'lightgreen':

        color = lightgreen()
    
    elif cor.lower().replace(' ','') == 'darkseagreen':

        color = darkseagreen()
    
    elif cor.lower().replace(' ','') == 'mediumseagreen': 

        color = mediumseagreen()

    elif cor.lower().replace(' ','') == 'seagreen':

        color = seagreen()
    
    elif cor.lower().replace(' ','') == 'darkgreen':

        color = darkgreen()
    
    elif cor.lower().replace(' ','') == 'green':

        color = green()

    elif cor.lower().replace(' ','') == 'forestgreen':

        color = forestgreen()
    
    elif cor.lower().replace(' ','') == 'limegreen':

        color = limegreen()
    
    elif cor.lower().replace(' ','') == 'lime':

        color = lime()
    
    elif cor.lower().replace(' ','') == 'lawngreen': 

        color = lawngreen()

    elif cor.lower().replace(' ','') == 'chartreuse':

        color = chartreuse()
    
    elif cor.lower().replace(' ','') == 'greenyellow':

        color = greenyellow()
    
    elif cor.lower().replace(' ','') == 'yellowgreen':

        color = yellowgreen()

    elif cor.lower().replace(' ','') == 'olivedrab':

        color = olivedrab()
    
    elif cor.lower().replace(' ','') == 'darkolivegreen':

        color = darkolivegreen()
    
    elif cor.lower().replace(' ','') == 'olive':

        color = olive()
    
    elif cor.lower().replace(' ','') == 'maroon': 

        color = maroon()

    elif cor.lower().replace(' ','') == 'darkred':

        color = darkred()
    
    elif cor.lower().replace(' ','') == 'firebrick':

        color = firebrick()
    
    elif cor.lower().replace(' ','') == 'brown':

        color = brown() 
    
    elif cor.lower().replace(' ','') == 'salmon':

        color = salmon()
    
    elif cor.lower().replace(' ','') == 'darksalmon':

        color = darksalmon()
    
    elif cor.lower().replace(' ','') == 'lightsalmon':

        color = lightsalmon()
    
    elif cor.lower().replace(' ','') == 'coral': 

        color = coral()

    elif cor.lower().replace(' ','') == 'tomato':

        color = tomato()
    
    elif cor.lower().replace(' ','') == 'red':

        color = red()
    
    elif cor.lower().replace(' ','') == 'orangered':

        color = orangered()
    
    elif cor.lower().replace(' ','') == 'darkorange':

        color = darkorange()
    
    elif cor.lower().replace(' ','') == 'orange':

        color = orange()
    
    elif cor.lower().replace(' ','') == 'gold':

        color = gold()
    
    elif cor.lower().replace(' ','') == 'yellow': 

        color = yellow()

    elif cor.lower().replace(' ','') == 'khaki':

        color = khaki()
    
    elif cor.lower().replace(' ','') == 'white': 

        color = white()

    elif cor.lower().replace(' ','') == 'aliceblue':

        color = aliceblue()
    
    elif cor.lower().replace(' ','') == 'ghostwhite':

        color = ghostwhite()
    
    elif cor.lower().replace(' ','') == 'snow':

        color = snow()
    
    elif cor.lower().replace(' ','') == 'seashell':

        color = seashell()
    
    elif cor.lower().replace(' ','') == 'floralwhite':

        color = floralwhite()
    
    elif cor.lower().replace(' ','') == 'whitesmoke':

        color = whitesmoke()
    
    elif cor.lower().replace(' ','') == 'beige': 

        color = beige()

    elif cor.lower().replace(' ','') == 'oldlace':

        color = oldlace()
    
    elif cor.lower().replace(' ','') == 'ivory':

        color = ivory()
    
    elif cor.lower().replace(' ','') == 'linen':

        color = linen()
    
    elif cor.lower().replace(' ','') == 'cornsilk':

        color = cornsilk()
    
    elif cor.lower().replace(' ','') == 'antiquewhite':

        color = antiquewhite()
    
    elif cor.lower().replace(' ','') == 'blanchedalmond':

        color = blanchedalmond()
    
    elif cor.lower().replace(' ','') == 'bisque': 

        color = bisque()

    elif cor.lower().replace(' ','') == 'lightyellow':

        color = lightyellow()
    
    elif cor.lower().replace(' ','') == 'lemonchiffon':

        color = lemonchiffon()
    
    elif cor.lower().replace(' ','') == 'lightgoldenrodyellow':

        color = lightgoldenrodyellow()

    elif cor.lower().replace(' ','') == 'papayawhip':

        color = papayawhip()
    
    elif cor.lower().replace(' ','') == 'peachpuff':

        color = peachpuff()
    
    elif cor.lower().replace(' ','') == 'moccasin':

        color = moccasin()
    
    elif cor.lower().replace(' ','') == 'palegoldenrod': 

        color = palegoldenrod()

    elif cor.lower().replace(' ','') == 'mistyrose':

        color = mistyrose()
    
    elif cor.lower().replace(' ','') == 'lavenderblush':

        color = lavenderblush()
    
    elif cor.lower().replace(' ','') == 'lavender':

        color = lavender()

    elif cor.lower().replace(' ','') == 'thistle':

        color = thistle()
    
    elif cor.lower().replace(' ','') == 'azure':

        color = azure()
    
    elif cor.lower().replace(' ','') == 'lightcyan':

        color = lightcyan()
    
    elif cor.lower().replace(' ','') == 'powderblue': 

        color = powderblue()

    elif cor.lower().replace(' ','') == 'paleturquoise':

        color = paleturquoise()
    
    elif cor.lower().replace(' ','') == 'honeydew':

        color = honeydew()
    
    elif cor.lower().replace(' ','') == 'mintcream':

        color = mintcream()

    return color
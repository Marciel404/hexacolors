import string

from .api import hexacolor, rgb, cmyk
from .str import stringcolor

def autodetect(args:str) -> str:

    if args[0] == '#':

        hexacolor(args)
    
    elif args[0] in list(string.digits):

        hexacolor(args)
    
    elif args[0] in list(string.ascii_letters):

        try:

            stringcolor(args)
        
        except:

            hexacolor(args)

    elif args.count(',') == 2:

        rgb(args)
    
    elif args.count(',') == 3:

        cmyk(args)

    else:

        print('ERROR: Not indentify the type')

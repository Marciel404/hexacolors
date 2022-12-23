# Hexacolors

A simple library that converts string to hexadecimal understandable by python

A simple library that converts RGB to hexadecimal understandable by python

A simple library that converts CMYK to hexadecimal understandable by python

A simple library that converts HSL to hexadecimal understandable by python

A simple library that converts hexadecimal understandable by python

I created this library more to use as pycord integration

## Usage:
### install with pip

```shell
pip install hexacolors
```

### Import on your code:

```python
import hexacolors
```
### Run it
```python

Run if online:

    Using StringColor:

        >>> import hexacolors
        >>> hexacolors.string('Blue')
        >>> print(hexacolors.listall) #List all colors availables
        
    Using HexaColor:

        >>> import hexacolors
        >>> hexacolors.hexadecimal('#0000FF') #Convert Hexadecimal Color for Python understand

    Using rgb:

        >>> import hexacolors
        >>> hexacolors.rgb("255,255,255")

    Using cmyk:

        >>> import hexacolors
        >>> hexacolors.cmyk("423,522,4,244")

    Using hsl:

        >>> import hexacolors
        >>> hexacolors.hsl('423,60%,70%')

    Using AutoDetect:
    
        >>> import hexacolors
        >>> hexacolors.autodetect('Blue') #Identify string
        >>> hexacolors.autodetect('#fff000') #Identify Hexadecimal
        >>> hexacolors.autodetect('255,255,255') #Identify RGB
        >>> hexacolors.autodetect('423,522,4,244') #Identify CMYK
        >>> hexacolors.autodetect('255,75%,64%') #Identify HSL


Run if offline:

    sing StringColor:

        >>> import hexacolors
        >>>
        >>> hexacolors.string('Blue')
        >>>
        >>> print(hexacolors.listall) #List all colors availables
        
    Using HexaColor:

        >>> import hexacolors
        >>>
        >>> hexacolors.hexadecimaloff('#0000FF') #Convert Hexadecimal Color for Python understand

    Using rgb:

        >>> import hexacolors
        >>>
        >>> hexacolors.rgboff(255,255,255)

    Using cmyk:

        >>> import hexacolors
        >>>
        >>> hexacolors.cmykoff(423,522,4,244)
```

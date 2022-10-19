# hexacolors

A simple library that converts string to hexadecimal understandable by python
A simple library that converts RGB to hexadecimal understandable by python
A simple library that converts CMYK to hexadecimal understandable by python
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
#or
from hexacolors import hexacolor, stringcolor, cmyk, rgb, autodetect
```
### Run it
```python
'''
Using StringColor:

    >>> import hexacolors
    >>>
    >>> hexacolors.stringcolor('Blue')
    >>>
    >>> print(hexacolors.listall) #List all colors availables

Using HexaColor:

    >>> import hexacolors
    >>>
    >>> hexacolors.hexacolor('#0000FF') #Convert Hexadecimal Color for Python understand

Using rgb:

    >>> import hexacolors
    >>>
    >>> hexacolors.rgb('255,255,255')

Using cmyk:

    >>> import hexacolors
    >>>
    >>> hexacolors.rgb('423,522,4,244')

Using AutoDetect:

    >>> import hexacolors
    >>>
    >>> hexacolors.autodetect('Blue') Identify string
    >>>
    >>> hexacolors.autodetect('#fff000') Identify Hexadecimal
    >>>
    >>> hexacolors.autodetect('255,255,255') Identify RGB
    >>>
    >>> hexacolors.autodetect('423,522,4,244') Identify CMYK
'''
```

convert this string for hexadecimal understandable by python

### Using in py-cord

```python

import discord, hexacolors

from discord.ext import commands

intents = discord.Intents.all()

client = commands.Bot(
command_prefix = '!',
help_command = None,
case_insensitive = True,
intents = intents
)

@client.event
async def on_ready():
    print("i'm logged with {}".format(client.user))

@client.event
async def on_message(msg):
    if msg.author == client.user: return

    if msg.author.bot: return

    await client.process_commands(msg)

@client.command()
async def ping(ctx):

    ping = client.latency * 1000

    e = discord.Embed(
    title ='Ping',
    description = 'My ping is {}'.format(int(ping)),
    color = hexacolors.hexacolor('#2f005c')
    )

    await ctx.send(embed = e)

#or

@client.command()
async def ping(ctx):

    ping = client.latency * 1000

    e = discord.Embed(
    title ='Ping',
    description = 'My ping is {}'.format(int(ping)),
    color = hexacolors.stringcolor('Blue')
    )

    await ctx.send(embed = e)

client.run('Token bot here')

```
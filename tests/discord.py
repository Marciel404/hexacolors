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
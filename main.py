import discord
import os
from discord.role import Role
from discord.utils import get
from discord.ext import commands
import asyncio

token = os.environ["TOKEN"]

client = commands.Bot(command_prefix='!')
role = Role
Client = discord.Client()

@client.event
async def on_ready():
    print('Ушао у ', client.user, 'ко циган у сестру')
    activity = discord.Game(name="Молим се аллаху")
    await client.change_presence(status=discord.Status.online, activity=activity)

@client.command()
async def on_message(ctx, message):
    if message.author == client.user:
        return

@client.command()
async def test(message):
    test = '{0.author.mention} не '.format(message)
    await message.channel.send(test)
    print("""|      test	    |
|---------------|""")

@client.command()
async def status(ctx):
    id = client.get_guild(689559413555593235)
    embed = discord.Embed(
        title="Статус",
        description= f"""Број муслимана у серверу је: {id.member_count}""",
        color=discord.Color.green(),
    )
    await ctx.send(embed=embed)
    print("""|     status	|
|---------------|""")

@client.command()
@discord.ext.commands.has_role('Аллахов ходочасник - Бошњотека')
@discord.ext.commands.has_role('Бот')
@discord.ext.commands.has_role('Кул дете')
@discord.ext.commands.has_role('Јевреј')
async def spuf(ctx, arg):
    await ctx.send(arg)
    
@client.event
async def on_member_join(member):
    ment = member.mention
    await client.get_channel(689573767969767533).send(f"{ment} је ушао у сервер!")
    role = get(member.guild.roles, name="Обичан геј")
    await member.add_roles(role)
    print(f"""{member} је ушао у сервер и добио је "Чланови" рол!""")

client.run(token)

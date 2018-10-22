import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from discord import Game


Client = discord.client
client = commands.Bot(command_prefix = '!')
Clientdiscord = discord.Client()


@client.event
async def on_member_join(member):
    await client.change_presence(game=Game(name='www.routersmac.club'))
    await client.send_message(member, 'Welcome to RouterSmacs Official Discord, do >help to see all of our bot commands ect!')
    print('Sent message to ' + member.name)
async def on_ready():
    await client.change_presence(game=Game(name='      '))
    print('Ready, Freddy') 


@client.event
async def on_message(message):
    if message.content == '>website':
        await client.send_message(message.channel,'**Check out our Stresser at** http://www.routersmac.club/register.php !')
    if message.content == '>support':
        await client.send_message(message.channel,'@support I need help!')
client.run('NTA0MDE4NzE5NTc2NTU1NTIw.Dq-74A.tqJ2DnlUqGjNbkFuaG1L1zPWZeg')

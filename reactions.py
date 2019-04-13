from random import randint
from utils.client import client, send_message
from discord.utils import get
import re
import string

async def react(message):
    """
    Add all reactions functions in this function which is called in main before executing commands
    """
    await funny(message)
    await bite(message)
    await pd(message)

async def funny(message):
    reactions = ['mdrrrrrrr indeed',
            'c\'est tres marrant mdrr',
            'MDRRR',
            'ptdrrrr',
            ':joy:',
            'LOL',
    ]

    rand = randint(0, 100)
    msg = reactions[rand % len(reactions)]

    values = {
        'mdr': 5,
        'mdrrr': 80,
        'MDR': 70,
        'MDRRR': 99,
        'ptdr': 10,
        }

    limit = 0
    for lol in values:
        if lol in message.content or lol.capitalize() in message.content:
            if values[lol] > limit:
                limit = values[lol]
    if rand < limit:
        await send_message(msg)

async def bite(message):
    tmp = message.content.replace(' ', '')
    for char in string.punctuation:
        tmp = tmp.replace(char, '')
    msg = tmp

    bite = re.compile('b+i+t+e+')
    chibre = re.compile('c+h+i+b+r+e+')

    regexp = [bite, chibre]

    for exp in regexp:
        result = exp.match(msg.lower())
        if result:
            await message.delete()

async def allah(message):
    tmp = message.content.lower().replace(' ', '')
    for char in string.punctuation:
        tmp = tmp.replace(char, '')
    msg = tmp

    print(msg)

    if 'allah' in msg:
        await send_message('Pas de terrorisme ici.')
        await message.delete()

async def pd(message):
    tmp = message.content.lower()
    for char in string.punctuation:
        if char != ' ':
            tmp = tmp.replace(char, '')

    emoji = get(client.emojis, name='kappapride')
    msg = tmp
    if 'pd' in msg:
        return await message.add_reaction(message, emoji)

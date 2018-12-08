from random import randint
from bot.client import client, send_message
import re
import string

async def react(message):
    """
    Add all reactions functions in this function which is called in main before executing commands
    """
    await funny(message)
    await bite(message)

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
            await client.delete_message(message)


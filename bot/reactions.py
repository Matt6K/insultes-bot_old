from random import randint
from bot.client import send_message

async def react(message):
    """
    Add all reactions functions in this function which is called in main before executing commands
    """
    await funny(message)

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
        'mdrrr': 50,
        'MDR': 70,
        'MDRRR': 99,
        'ptdr': 10,
        }

    limit = 0
    for lol in values:
        if lol in message.content and values[lol] > limit:
            limit = values[lol]
    if rand < limit:
        await send_message(msg)

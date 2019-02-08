import json
import random
import discord

from bot.client import client, send_message

def subparser_install(subparser):
    parser_random = subparser.add_parser(
        'random',
        help='Random generator',
    )
    parser_random.set_defaults(func=random_gen)
    parser_random.add_argument('choices', default=None, nargs='*', help='The random')

async def random_gen(choices=None, **kwargs):
    if choices:
        await send_message(random.choice(choices))
    else:
        await send_message(str(random.randint(0, 100)))

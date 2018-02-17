import json
import random

from bot.client import send_message

def subparser_install(subparser):
    parser_insult = subparser.add_parser(
        'insult',
        help='Insult someone',
    )
    parser_insult.set_defaults(func=insult)
    parser_insult.add_argument('username', type=str, help='The user to insult')


async def insult(username, **kwargs):
    insult = 'No insult generator yet, <@291303759018065927> is playing Diablo3 instead of programming it'
    await send_message(insult)

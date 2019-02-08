import json
import random
import discord

from bot.client import client, send_message, change_nickname, get_user

def subparser_install(subparser):
    parser_rename = subparser.add_parser(
        'test',
        help='For testing',
    )
    parser_rename.set_defaults(func=test)
    parser_rename.add_argument('username', nargs='*', type=str, help='The user to test')

async def test(username, **kwargs):
    user = get_user(username)
    msg = 'Yo <@{}>'.format(user.id)
    await send_message(msg)

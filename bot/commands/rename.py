import json
import random
import discord

from bot.client import client, send_message, change_nickname

def subparser_install(subparser):
    parser_rename = subparser.add_parser(
        'rename',
        help='Rename someone',
    )
    parser_rename.set_defaults(func=rename)
    parser_rename.add_argument('username', nargs='*', type=str, help='The user to rename')
    parser_rename.add_argument('--nickname', nargs='*', type=str, help='The nickname to use')

async def rename(username, nickname, **kwargs):
    try:
        username = ' '.join(username)
        nickname = ' '.join(nickname)
    except:
        return {'msg': 'You need a username and a nickname'}

    user = client.server.get_member_named(username)
    if not user:
        await send_message('No user')
        return

    try:
        await change_nickname(user, nickname)
        msg = '{} is now called {} :D'.format(username, nickname)
        await send_message(msg)
    except discord.errors.Forbidden as e:
        await send_message(e.text)

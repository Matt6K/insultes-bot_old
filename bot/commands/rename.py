import json
import random
import discord

from bot.client import client, send_message, change_nickname, get_user
from bot.commands.insult import gen_insult

def subparser_install(subparser):
    parser_rename = subparser.add_parser(
        'rename',
        help='Rename someone',
    )
    parser_rename.set_defaults(func=rename)
    parser_rename.add_argument('username', nargs='*', type=str, help='The user to rename')

async def rename(username, **kwargs):
    user = get_user(username)
    if not user:
        await send_message('No user')
        return

    nickname = gen_insult()

    try:
        await change_nickname(user, nickname)
    except discord.errors.Forbidden as e:
        await send_message(e.text)

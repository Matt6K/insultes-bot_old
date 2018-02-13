import json
import random

def subparser_install(subparser):
    parser_rename = subparser.add_parser(
        'rename',
        help='Rename someone',
    )
    parser_rename.set_defaults(func=rename)
    parser_rename.add_argument('username', nargs='*', type=str, help='The user to rename')
    parser_rename.add_argument('--nickname', nargs='*', type=str, help='The nickname to use')

def rename(username, nickname, client, message, server, **kwargs):
    try:
        username = ' '.join(username)
        nickname = ' '.join(nickname)
    except:
        return {'msg': 'You need a username and a nickname'}

    user = server.get_member_named(username)
    if str(user) == 'Lunkwill#7801':
        return {'msg': 'Je ne peux pas rename le grand maitre createur'}

    return {
        'rename': user,
        'new_nick': nickname,
        'msg': '{} is now called {} :D'.format(username, nickname)}

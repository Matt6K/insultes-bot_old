from random import randint

from bot.client import client, send_message
from bot.commands.insults_table import NAMES, ADJECTIVES


def subparser_install(subparser):
    parser_insult = subparser.add_parser(
        'insult',
        help='Insult someone',
    )
    parser_insult.set_defaults(func=insult)
    parser_insult.add_argument('username', nargs='*', type=str, help='The user to insult')


async def insult(username, **kwargs):
    # insult = 'No insult generator yet, <@291303759018065927> is playing Diablo3 instead of programming it'

    username = ' '.join(username)
    user = client.server.get_member_named(username)

    m = False                   # masculin
    f = False                   # féminin

    name = NAMES[randint(0, 100) % len(NAMES)]
    adj = ADJECTIVES[randint(0, 100) % len(ADJECTIVES)]

    if name['masculin'] and not name['féminin']:
        m = True
    elif not name['masculin'] and name['féminin']:
        f = True
    else:
        if randint(0, 1) == 0:
            m = True
        else:
            f = True

    #use user id if found
    if user:
        insult = '<@{}> '.format(user.id)
    else:
        insult = '{} '.format(username)

    if m == True:
        insult += '{} {}'.format(adj['masculin'], name['masculin'])
    elif f == True:
        insult += '{} {}'.format(adj['féminin'], name['féminin'])

    await send_message(insult)

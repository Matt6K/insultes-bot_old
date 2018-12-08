from random import randint

from bot.client import client, send_message, get_user
from bot.commands.insults_table import NAMES, ADJECTIVES

def gen_insult():
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

    if m == True:
        insult = '{} {}'.format(adj['masculin'], name['masculin'])
    elif f == True:
        insult = '{} {}'.format(adj['féminin'], name['féminin'])

    return insult


def subparser_install(subparser):
    parser_insult = subparser.add_parser(
        'insult',
        help='Insult someone',
    )
    parser_insult.set_defaults(func=send_insult)
    parser_insult.add_argument('username', nargs='*', type=str, help='The user to insult')

async def send_insult(username, message, **kwargs):
    username = ' '.join(username)
    user = get_user(username)

    #use user id if found
    if user:
        insult = '<@{}> '.format(user.id)
    else:
        insult = '{} '.format(username)
    
    insult += gen_insult()

    await client.delete_message(message)
    await send_message(insult)

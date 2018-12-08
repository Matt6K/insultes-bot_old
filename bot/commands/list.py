from bot.client import send_message
from bot.commands.insults_table import NAMES, ADJECTIVES

def subparser_install(subparser):
    parser_list = subparser.add_parser(
        'list',
        help='List a list of words used by the bot, either names or adjectives',
    )
    parser_list.set_defaults(func=list)
    parser_list.add_argument('dict_type', type=str, help='The dict of objects to display', choices=['names', 'adjectives', 'all'])

async def list(dict_type, **kwargs):
    if dict_type == 'names':
        await send_message(['**The names used to form the insults**:',
                            words_object_to_str(NAMES)])
    elif dict_type == 'adjectives':
        await sned_message(['**The adjectives used to form the insults**:',
                            words_object_to_str(ADJECTIVES)])
    else:
        await send_message(['**The names and adjectives used to form the insults**:',
                            '**Names:**',
                            words_object_to_str(NAMES),
                            '**Adjectives:**',
                            words_object_to_str(ADJECTIVES)])

def words_object_to_str(words_object):
    insult_str = ''
    for name in words_object:
        masculin = name['masculin']
        feminin = name['féminin']
        poids = name['poids']
        if masculin is not None and feminin is not None:
            if masculin != feminin:
                insult_str = '{0}\n{1}\t\tpoids:{2}\n{3}\t\tpoids:{4}'.format(insult_str, masculin, poids, feminin, poids)
            else:
                insult_str = '{0}\n{1}\t\tpoids:{2}'.format(insult_str, masculin, poids)
        if masculin is not None and feminin is None:
            insult_str = '{0}\n{1}\t\tpoids:{2}'.format(insult_str, masculin, poids)
        if masculin is None and feminin is not None:
            insult_str = '{0}\n{1}\t\tpoids:{2}'.format(insult_str, feminin, poids)
    return insult_str

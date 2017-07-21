import json
import random

def subparser_install(subparser):
    parser_insult = subparser.add_parser(
        'insult',
        help='Insult someone',
    )
    parser_insult.set_defaults(func=insult)
    parser_insult.add_argument('username', type=str, help='The user to insult')

NAMES = [{'masculin':'enculé', 'féminin':'enculée', 'poids': 50},
         {'masculin':'bâtard', 'féminin':'bâtarde', 'poids': 50},
         {'masculin':'connard', 'féminin':'connasse', 'poids': 50},
         {'masculin':None, 'féminin':'pute', 'poids': 50},
         {'masculin':'FDP', 'féminin':'FDP', 'poids': 50},
         {'masculin':'nazi', 'féminin':'nazi', 'poids': 50},
         {'masculin':'juif', 'féminin':'juive', 'poids': 50},
         {'masculin':None, 'féminin':'chiennasse', 'poids': 50},
         {'masculin':'chien', 'féminin':'chienne', 'poids': 50},
         {'masculin':'con', 'féminin':'conne', 'poids': 50},
         {'masculin':'gitan', 'féminin':'gitane', 'poids': 50},
         {'masculin':'manouche', 'féminin':'manouche', 'poids': 50},
         {'masculin':'pécore', 'féminin':'pécore', 'poids': 50},
         {'masculin':'péglan', 'féminin':None, 'poids': 50},
         {'masculin':'suceur', 'féminin':'suceuse', 'poids': 50},
         {'masculin':'suceur de bites', 'féminin':'suceuse de bites', 'poids': 50},
         {'masculin':'suceur de chibres', 'féminin':'suceuse de chibres', 'poids': 50},
         {'masculin':'casse-couilles', 'féminin':'casse-couilles', 'poids': 50},
         {'masculin':'abruti', 'féminin':'abrutie', 'poids': 50},
         {'masculin':'bouffon', 'féminin':'bouffone', 'poids': 50},
         {'masculin':'branleur', 'féminin':'branleuse', 'poids': 50},
         {'masculin':'sac à foutre', 'féminin':'sac à foutre', 'poids': 50},
         {'masculin':'tas de merde', 'féminin':'tas de merde', 'poids': 50},
         {'masculin':None, 'féminin':'raclure', 'poids': 50},
         {'masculin':None, 'féminin':'catin', 'poids': 50},
         {'masculin':'bougnoule', 'féminin':'bougnoule', 'poids': 50},
         {'masculin':None, 'féminin':'chaudasse', 'poids': 50},
         {'masculin':None, 'féminin':'coche', 'poids': 50},
         {'masculin':'crétin', 'féminin':'crétine', 'poids': 50},
         {'masculin':None, 'féminin':'lopette', 'poids': 50},
         {'masculin':'pd', 'féminin':None, 'poids': 50},
         {'masculin':'trans', 'féminin':'trans', 'poids': 50},
         {'masculin':'monstre', 'féminin':None, 'poids': 50},
         {'masculin':'gland', 'féminin':None, 'poids': 50},
         {'masculin':'glandu', 'féminin':'glandu', 'poids': 50},
         {'masculin':'mongole', 'féminin':'mongole', 'poids': 50},
         {'masculin':'mongolito', 'féminin':'mongolito', 'poids': 50},
         {'masculin':None, 'féminin':'merde', 'poids': 50},
         {'masculin':'handicapé', 'féminin':'handicapée', 'poids': 50},
         {'masculin':'michto', 'féminin':'michto', 'poids': 50},
         {'masculin':'débile', 'féminin':'débile', 'poids': 50},
         {'masculin':'sodomite', 'féminin':'sodomite', 'poids': 50},
         {'masculin':'emmerdeur', 'féminin':'emmerdeuse', 'poids': 50},
         {'masculin':None, 'féminin':'tarlouze', 'poids': 50},
         {'masculin':None, 'féminin':'putain', 'poids': 50}]
ADJECTIVES = [{'masculin':'sale', 'féminin':'sale', 'poids': 10},
              {'masculin':'immonde', 'féminin':'immonde', 'poids': 10},
              {'masculin':'gros', 'féminin':'grosse', 'poids': 10},
              {'masculin':'abject', 'féminin':'abjecte', 'poids':10},
              {'masculin':'affligeant', 'féminin':'affligeante', 'poids':10},
              {'masculin':'merdique', 'féminin':'merdique', 'poids':10},
              {'masculin':'minable', 'féminin':'minable', 'poids':10},
              {'masculin':'passable', 'féminin':'passable', 'poids':10},
              {'masculin':'dégueulasse', 'féminin':'dégeulasse', 'poids':10},
              {'masculin':'giga', 'féminin':'giga', 'poids':10},
              {'masculin':'horrible', 'féminin':'horrible', 'poids':10},
              {'masculin':'innommable', 'féminin':'innommable', 'poids':10},
              {'masculin':'infernal', 'féminin':'infernaleê', 'poids':10},
              {'masculin':'vulgaire', 'féminin':'vulgaire', 'poids':10},
              {'masculin':'épouvantable', 'féminin':'épouvantable', 'poids':10},
              {'masculin':'sombre', 'féminin':'sombre', 'poids':10},
              {'masculin':'effroyable', 'féminin':'effroyable', 'poids':10},
              {'masculin':'terrible', 'féminin':'terrible', 'poids':10},]

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

def insult(username, client, message, **kwargs):
    return {'msg': ['{0}: sale batard'.format(username),
                    'Immonde salope <@291303759018065927>',
                    words_object_to_str(NAMES),
                    words_object_to_str(ADJECTIVES)]}

def list_subparser_install(subparser):
    parser_list = subparser.add_parser(
        'list',
        help='List a list of words used by the bot, either names or adjectives',
    )
    parser_list.set_defaults(func=list)
    parser_list.add_argument('dict_type', type=str, help='The dict of objects to display', choices=['names', 'adjectives', 'all'])

def list(dict_type, client, message, **kwargs):
    if dict_type == 'names':
        return {'msg': ['**The names used to form the insults**:\n',
                        words_object_to_str(NAMES)]}
    elif dict_type == 'adjectives':
        return {'msg': ['**The adjectives used to form the insults**:\n',
                        words_object_to_str(ADJECTIVES)]}
    else:
        return {'msg': ['**The names and adjectives used to form the insults**:\n',
                        words_object_to_str(NAMES),
                        words_object_to_str(ADJECTIVES)]}

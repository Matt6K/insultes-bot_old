import random

def subparser_install(subparser):
    parser_insult = subparser.add_parser(
        'insult',
        help='Insult someone',
    )
    parser_insult.set_defaults(func=insult)
    parser_insult.add_argument('username', type=str, help='The user to insult')

INSULTS = [{'masculin':'enculé', 'féminin':'enculée', 'poids': 50},
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
           {'masculin':None, 'féminin':'tarlouze', 'poids': 50}]
ADJECTIVES = ['']

def insult(username, client, message, **kwargs):
    return {'msg': ['{0}: sale batard'.format(username),
                    ' '.join(INSULTS),
                    ' '.join(ADJECTIVES)]}

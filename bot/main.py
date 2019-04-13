#!/opt/python3/bin/python3.5

import os
import argparse
import discord


from bot.client import (
    client,
    send_message,
    change_game,
)

from bot.reactions import react
from bot.commands.insult import subparser_install as insult_subparser
from bot.commands.list import subparser_install as list_subparser
from bot.commands.rename import subparser_install as rename_subparser
from bot.commands.test import subparser_install as test_subparser
from bot.commands.random import subparser_install as random_subparser


def help_subparser(subparser):
    parser_help = subparser.add_parser(
        'help',
        help='Help',
    )
    parser_help.set_defaults(func=helper)

async def helper(**kwargs):
    helps = '**'
    for command in SIMPLE_COMMANDS:
        helps += '/' + command[0] + '\n'
    helps += '**'

    await send_message(helps)


def ping_subparser(subparser):
    parser_ping = subparser.add_parser(
        'ping',
        help='Ping',
    )
    parser_ping.set_defaults(func=ping)

async def ping(**kwargs):
    await send_message('pong')


def cute_chat_subparser(subparser):
    parser_cute_chat = subparser.add_parser(
        'cute',
        help='Cute chat dafranAYAYA',
    )
    parser_cute_chat.set_defaults(func=cute_chat)

async def cute_chat(**kwargs):
    await send_message('CUTE CHAT <:dafranAYAYA:462648524706676750> CUTE CHAT <:dafranAYAYA:462648524706676750> CUTE CHAT <:dafranAYAYA:462648524706676750> CUTE CHAT <:dafranAYAYA:462648524706676750> CUTE CHAT <:dafranAYAYA:462648524706676750> CUTE CHAT <:dafranAYAYA:462648524706676750> CUTE CHAT <:dafranAYAYA:462648524706676750>')


def printf_subparser(subparser):
    parser_printf = subparser.add_parser(
        'printf',
        help='How long since Frazou said he will upload his printf "tonight"',
    )
    parser_printf.set_defaults(func=printf)

async def printf(message, **kwargs):
    from datetime import datetime, timedelta

    time1 = datetime.strptime('Nov 10 2018 4:00PM', '%b %d %Y %I:%M%p')
    time2 = datetime.now()
    diff = time2 - time1
    hours = diff / timedelta(hours=1)

    await client.delete_message(message)
    await send_message('On attend le printf de frazou depuis {} heures. DECEPTION, FRAZOU LACHEUR'.format(int(hours)))

SIMPLE_COMMANDS = [
    ('help', help_subparser),
    ('test', test_subparser),
    ('ping', ping_subparser),
    ('cute', cute_chat_subparser),
    ('printf', printf_subparser),
    ('insult', insult_subparser),
    ('list', list_subparser),
    ('rename', rename_subparser),
    ('random', random_subparser),
]

COMMANDS = [
#('abuse', abuse_subparser)
]

# Override error class (not exiting anymore)
class ArgumentParser(argparse.ArgumentParser):
    def error(self, message):
        raise ValueError(message)


# Generating parser
parser = ArgumentParser()

subparser = parser.add_subparsers(dest='main_command', help='The main command')
subparser.required = True

for command in SIMPLE_COMMANDS:
    command[1](subparser)

for command in COMMANDS:
    cmd_parser = subparser.add_parser(command[0])
    cmd_subparser = cmd_parser.add_subparsers(dest='sub_command', help='The {0} sub-command'.format(command[0]))
    command[1](cmd_subparser)

async def execute_command(message):
    try:
        cmd = message.content[1:].split(' ')

        commands = []
        for item in SIMPLE_COMMANDS:
            commands.append(item[0])
        for item in COMMANDS:
            commands.append(item[0])
        if cmd[0] not in commands:
            usage = 'Command "{}" not found.\nUse /help to see available commands'.format(cmd[0])
            await send_message(usage)
            return

        try:
            argument = parser.parse_args(cmd)
        except ValueError as e:
            await send_message('Exception was thrown cos of arguments: {}'.format(e))
            return
        except:
            await send_message('Unknown error, niquez vous jsais pas ce que c\'est')
            return

        argument.message = message
        await argument.func(**vars(argument))
    except Exception as e:
        await send_message(e)
        return

async def on_event(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
    client.channel = message.channel
    client.server = list(client.servers)[0]

    await react(message)

    if message.content.startswith('/'):
        await execute_command(message)


@client.event
async def on_message(message):
    await on_event(message)

@client.event
async def on_message_edit(before, after):
    await on_event(after)

@client.event
async def on_ready():
    f = open('/tmp/insults.pid', 'w')
    f.write(str(os.getpid()))
    f.close()
    print(client.user.name, ' ready !')
    print('------')

    now_playing = discord.Game(name='Overwatch')
    await change_game(game=now_playing)

client.run('')
client.logout()

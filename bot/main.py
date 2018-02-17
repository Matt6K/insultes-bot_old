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


def help_subparser(subparser):
    parser_help = subparser.add_parser(
        'help',
        help='Help',
    )
    parser_help.set_defaults(func=helper)

def helper(**kwargs):
    helps = '**'
    for command in SIMPLE_COMMANDS:
        helps += '/' + command[0] + '\n'
    helps += '**'

    return {'msg': helps}

SIMPLE_COMMANDS = [
    ('help', help_subparser),
    ('insult', insult_subparser),
    ('list', list_subparser),
    ('rename', rename_subparser),
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

        argument = parser.parse_args(cmd)
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

    now_playing = discord.Game(name='eating your deads')
    await change_game(game=now_playing)

def main():
    client.run('MzM3OTAyMzg1NDU4NDQ2MzQ2.DFNt4g.NOXenryxEq5IvDdhs44Ijd--a8U')
    client.logout()
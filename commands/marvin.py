def subparser_install(subparser):
    parser_reboot = subparser.add_parser(
        'reboot',
        help='Reboot the bot',
    )
    parser_reboot.set_defaults(func=reboot)

    parser_say_hello = subparser.add_parser(
        'say_hello',
        help='The bot will say hello in this channel',
    )
    parser_say_hello.set_defaults(func=say_hello)
    parser_say_hello.add_argument('channel', help='The channel')

def reboot(client, **kwargs):
    msg = 'Marvin rebooted (it\'s a fake, not implemented yet)'
    return {'msg': msg}

def say_hello(client, channel, message, **kwargs):
    channels = client.get_all_channels()
    for chan in channels:
        if chan.name == channel:
            return {'channel': chan, 'msg': 'Hello !'}
    return {'msg': 'Can\'t find or write in this channel'}


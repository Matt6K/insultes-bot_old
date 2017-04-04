def subparser_install(subparser):
    parser_hello = subparser.add_parser(
        'hello',
        help='Say hello'
    )
    parser_hello.set_defaults(func=hello)

def hello(message, **kwargs):
    return {'msg': 'Hello {0.author.mention}'.format(message)}

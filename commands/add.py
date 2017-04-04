def subparser_install(subparser):
    parser_add = subparser.add_parser(
        'add',
        help='Do an addition',
    )
    parser_add.set_defaults(func=add)
    parser_add.add_argument('number1', type=int, help='The first number')
    parser_add.add_argument('number2', type=int, help='The second number')

def add(number1, number2, **kwargs):
    return {'msg': number1 + number2}

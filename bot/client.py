import discord

client = discord.Client()

async def send_message(message, channel=None):
    if type(message) != list:
        messages = []
        messages.append(message)
    else:
        messages = message
    for msg in messages:

        #for christmas
        msg = ':snowboarder: ' + msg + ' :skier:'

        if channel:
            await client.send_message(channel, msg)
        else:
            await client.send_message(client.channel, msg)

async def change_game(game):
    await client.change_presence(game=game)

async def change_nickname(user, nickname):
    try:
        await client.change_nickname(user, nickname)
    except discord.errors.Forbidden:
        raise

def get_user(username):
    user = None
    username = ' '.join(username)
    if username[0] == '<':
        username = username[3:-1]

    members = client.server.members
    for member in members:
        if username == member.id or username == member.nick:
            user = member

    return user

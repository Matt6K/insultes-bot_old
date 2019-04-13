import discord

client = discord.Client()

async def send_message(message, channel=None):
    if type(message) != list:
        messages = []
        messages.append(message)
    else:
        messages = message

    for msg in messages:
        if channel:
            await channel.send(msg)
        else:
            await client.channel.send(msg)

async def change_game(game):
    await client.change_presence(activity=game)

async def change_nickname(user, nickname):
    try:
        await user.edit(nickname)
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
